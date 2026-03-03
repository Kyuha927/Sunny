#!/usr/bin/env python3
"""Project intelligence updater for Obsidian project cards.

Collects recent signals from web feeds and writes:
1) Per-project update note
2) Auto-intel block in each project card
"""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ProjectIntelBot/1.0"
AUTO_BLOCK_START = "<!-- AUTO_INTEL:START -->"
AUTO_BLOCK_END = "<!-- AUTO_INTEL:END -->"


@dataclass
class IntelItem:
    title: str
    link: str
    summary: str
    published: dt.datetime | None
    source: str
    score: float = 0.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update Obsidian project intelligence notes.")
    parser.add_argument("--config", required=True, help="Path to project_intel_sources.json")
    parser.add_argument("--lookback-days", type=int, default=None, help="Override lookback window in days")
    parser.add_argument("--max-items", type=int, default=None, help="Override max items per project")
    parser.add_argument("--dry-run", action="store_true", help="Print result without writing files")
    return parser.parse_args()


def load_config(config_path: Path) -> dict:
    return json.loads(config_path.read_text(encoding="utf-8"))


def fetch_text(url: str, timeout_sec: int = 20) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def strip_ns(tag: str) -> str:
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def first_text(elem: ET.Element, names: set[str]) -> str:
    for child in list(elem):
        if strip_ns(child.tag) in names and child.text:
            return child.text.strip()
    return ""


def first_link(elem: ET.Element) -> str:
    for child in list(elem):
        tag = strip_ns(child.tag)
        if tag == "link":
            href = (child.attrib.get("href") or "").strip()
            rel = (child.attrib.get("rel") or "").strip()
            if href and (rel in ("", "alternate")):
                return href
            if child.text and child.text.strip():
                return child.text.strip()
    return ""


def parse_datetime(raw: str) -> dt.datetime | None:
    value = (raw or "").strip()
    if not value:
        return None

    # RFC2822 (RSS pubDate)
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed is not None:
            if parsed.tzinfo is None:
                return parsed.replace(tzinfo=dt.timezone.utc)
            return parsed.astimezone(dt.timezone.utc)
    except Exception:
        pass

    # ISO8601 variants
    iso = value.replace("Z", "+00:00")
    try:
        parsed = dt.datetime.fromisoformat(iso)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=dt.timezone.utc)
        return parsed.astimezone(dt.timezone.utc)
    except Exception:
        return None


def parse_feed_items(xml_text: str, source: str) -> list[IntelItem]:
    out: list[IntelItem] = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return out

    entries: list[ET.Element] = []
    for elem in root.iter():
        tag = strip_ns(elem.tag)
        if tag in ("item", "entry"):
            entries.append(elem)

    for entry in entries:
        title = first_text(entry, {"title"}) or "(untitled)"
        link = first_link(entry)
        summary = first_text(entry, {"description", "summary", "content"}) or ""
        published_raw = first_text(entry, {"pubDate", "published", "updated", "date"})
        published = parse_datetime(published_raw)
        if not link:
            continue

        out.append(
            IntelItem(
                title=clean_text(title),
                link=link.strip(),
                summary=clean_text(summary),
                published=published,
                source=source,
            )
        )

    return out


def clean_text(value: str) -> str:
    cleaned = re.sub(r"<[^>]+>", " ", value)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def build_google_news_url(query: str) -> str:
    encoded = urllib.parse.quote_plus(query)
    return f"https://news.google.com/rss/search?q={encoded}&hl=ko&gl=KR&ceid=KR:ko"


def build_arxiv_url(query: str, max_results: int = 8) -> str:
    encoded = urllib.parse.quote_plus(query)
    return (
        "https://export.arxiv.org/api/query?"
        f"search_query=all:{encoded}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    )


def count_topic_hits(item: IntelItem, topics: Iterable[str]) -> tuple[int, int]:
    body = f"{item.title} {item.summary} {item.source}".lower()
    title = item.title.lower()
    topics_l = [t.lower() for t in topics]
    body_hits = sum(1 for t in topics_l if t and t in body)
    title_hits = sum(1 for t in topics_l if t and t in title)
    return body_hits, title_hits


def relevance_score(item: IntelItem, topics: Iterable[str], lookback_days: int, now_utc: dt.datetime) -> float:
    topic_hits, title_hits = count_topic_hits(item, topics)
    title = item.title.lower()

    recency = 0.0
    if item.published:
        age_days = max(0.0, (now_utc - item.published).total_seconds() / 86400.0)
        recency = max(0.0, 1.0 - (age_days / max(1, lookback_days)))

    release_words = ("release", "changelog", "update", "version", "preview", "beta", "breaking", "deprecation")
    release_bonus = 1.5 if any(w in title for w in release_words) else 0.0

    source_l = item.source.lower()
    source_bonus = 0.0
    if source_l.startswith("githubfeed:"):
        source_bonus += 1.0
    if source_l.startswith("googlenews:"):
        source_bonus += 0.8
    if source_l.startswith("rss:"):
        source_bonus += 0.5
    if "arxiv:" in source_l:
        source_bonus -= 0.2

    return title_hits * 4.0 + topic_hits * 2.5 + recency * 1.2 + release_bonus + source_bonus


def dedupe_items(items: list[IntelItem]) -> list[IntelItem]:
    seen: set[str] = set()
    out: list[IntelItem] = []
    for item in items:
        key = item.link.strip().lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def collect_project_items(project: dict, lookback_days: int, max_items: int, now_utc: dt.datetime) -> tuple[list[IntelItem], list[str]]:
    collected: list[IntelItem] = []
    errors: list[str] = []
    cutoff = now_utc - dt.timedelta(days=lookback_days)

    feed_requests: list[tuple[str, str]] = []
    for query in project.get("google_news_queries", []):
        feed_requests.append((build_google_news_url(query), f"GoogleNews: {query}"))
    for url in project.get("rss_feeds", []):
        feed_requests.append((url, f"RSS: {url}"))
    for url in project.get("github_release_feeds", []):
        feed_requests.append((url, f"GitHubFeed: {url}"))
    for query in project.get("arxiv_queries", []):
        feed_requests.append((build_arxiv_url(query), f"arXiv: {query}"))

    for url, source in feed_requests:
        try:
            xml_text = fetch_text(url)
            items = parse_feed_items(xml_text, source)
        except Exception as exc:  # noqa: BLE001 - keep going if one feed fails
            errors.append(f"{source} -> {exc}")
            continue

        for item in items:
            if item.published and item.published < cutoff:
                continue
            collected.append(item)

    collected = dedupe_items(collected)
    topics = project.get("topics", [])
    filtered: list[IntelItem] = []
    for item in collected:
        item.score = relevance_score(item, topics, lookback_days, now_utc)
        body_hits, title_hits = count_topic_hits(item, topics)
        source_l = item.source.lower()

        # Keep high-confidence sources even with low keyword overlap,
        # but suppress weak/noisy items.
        min_score = 0.8
        if source_l.startswith("githubfeed:"):
            min_score = 0.5
        if source_l.startswith("arxiv:"):
            min_score = 2.5

        if (body_hits + title_hits) == 0 and source_l.startswith("arxiv:"):
            continue
        if item.score < min_score:
            continue
        filtered.append(item)

    if not filtered and collected:
        # Fallback: if strict filtering removed everything, keep recent top items.
        filtered = list(collected)

    filtered.sort(key=lambda x: (x.score, x.published or dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc)), reverse=True)
    return filtered[:max_items], errors


def make_update_note(project: dict, items: list[IntelItem], errors: list[str], lookback_days: int, now_utc: dt.datetime) -> str:
    date_str = now_utc.date().isoformat()
    generated_at = now_utc.replace(microsecond=0).isoformat()
    project_id = project["id"]

    top = items[:3]
    recommended = list(project.get("suggested_next_actions", []))
    for item in top[:2]:
        recommended.append(f"소스 검토: {item.title[:80]} -> 카드 next_actions 반영 여부 결정")
    if not recommended:
        recommended = ["신규 신호가 적어 기존 백로그 우선순위를 유지"]

    def item_line(idx: int, item: IntelItem) -> str:
        date_tag = item.published.date().isoformat() if item.published else "date-unknown"
        return f"{idx}. [{item.title}]({item.link}) ({item.source}, {date_tag})"

    if top:
        top_block = "\n".join(item_line(i + 1, item) for i, item in enumerate(top))
    else:
        top_block = "1. 신규 신호 없음"

    recommend_block = "\n".join(f"{i + 1}. {act}" for i, act in enumerate(recommended[:5]))

    rows: list[str] = []
    for item in items:
        date_tag = item.published.date().isoformat() if item.published else "date-unknown"
        title = item.title.replace("|", "\\|")
        source = item.source.replace("|", "\\|")
        rows.append(f"| {date_tag} | {source} | {item.score:.1f} | {title} | [link]({item.link}) |")

    table = "\n".join(rows) if rows else "| - | - | - | 신규 항목 없음 | - |"
    error_block = "\n".join(f"- {e}" for e in errors) if errors else "- 없음"

    lines = [
        "---",
        "type: project-intel-update",
        f'project_id: "{project_id}"',
        f"generated_at: {generated_at}",
        f"lookback_days: {lookback_days}",
        f"item_count: {len(items)}",
        "---",
        f"# {project_id} 최신 인텔리전스 ({date_str})",
        "",
        "## 핵심 시그널",
        top_block,
        "",
        "## 권장 액션",
        recommend_block,
        "",
        "## 수집 상세",
        "| Date | Source | Score | Title | Link |",
        "| --- | --- | ---: | --- | --- |",
        table,
        "",
        "## 수집 에러",
        error_block,
        "",
    ]
    return "\n".join(lines)


def report_rel_link(vault_root: Path, report_path: Path) -> str:
    rel = report_path.relative_to(vault_root).as_posix()
    if rel.endswith(".md"):
        rel = rel[:-3]
    return f"[[{rel}]]"


def make_card_auto_block(
    report_link: str,
    items: list[IntelItem],
    lookback_days: int,
    now_utc: dt.datetime,
) -> str:
    date_time = now_utc.strftime("%Y-%m-%d %H:%M UTC")
    top = items[:3]
    if top:
        top_lines = []
        for item in top:
            date_tag = item.published.date().isoformat() if item.published else "date-unknown"
            top_lines.append(f"- [{item.title}]({item.link}) ({item.source}, {date_tag})")
        top_block = "\n".join(top_lines)
    else:
        top_block = "- 신규 신호 없음"

    lines = [
        AUTO_BLOCK_START,
        "## 자동 인텔리전스",
        f"- 마지막 업데이트: {date_time}",
        f"- 수집 범위: 최근 {lookback_days}일",
        f"- 수집 건수: {len(items)}건",
        f"- 리포트: {report_link}",
        "",
        "### 핵심 시그널",
        top_block,
        AUTO_BLOCK_END,
    ]
    return "\n".join(lines)


def update_card_file(card_path: Path, auto_block: str, review_date: str, dry_run: bool) -> None:
    text = card_path.read_text(encoding="utf-8")

    if re.search(r"(?m)^last_review:\s*.+$", text):
        text = re.sub(r"(?m)^last_review:\s*.+$", f"last_review: {review_date}", text)

    block_pattern = re.compile(re.escape(AUTO_BLOCK_START) + r".*?" + re.escape(AUTO_BLOCK_END), re.DOTALL)
    if block_pattern.search(text):
        text = block_pattern.sub(auto_block, text)
    else:
        text = text.rstrip() + "\n\n" + auto_block + "\n"

    if not dry_run:
        card_path.write_text(text, encoding="utf-8")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def main() -> int:
    args = parse_args()
    config_path = Path(args.config).resolve()
    cfg = load_config(config_path)

    vault_root = Path(cfg["vault_root"]).resolve()
    updates_root = (vault_root / cfg["updates_root"]).resolve()
    lookback_days = args.lookback_days or int(cfg.get("default_lookback_days", 7))
    max_items = args.max_items or int(cfg.get("default_max_items", 10))

    now_utc = dt.datetime.now(tz=dt.timezone.utc)
    review_date = now_utc.date().isoformat()

    summary_lines: list[str] = []
    for project in cfg.get("projects", []):
        project_id = project["id"]
        card_path = (vault_root / project["card_file"]).resolve()
        project_update_dir = updates_root / project_id
        ensure_dir(project_update_dir)
        report_path = project_update_dir / f"{review_date}.md"

        items, errors = collect_project_items(project, lookback_days, max_items, now_utc)
        note_text = make_update_note(project, items, errors, lookback_days, now_utc)
        auto_block = make_card_auto_block(
            report_link=report_rel_link(vault_root, report_path),
            items=items,
            lookback_days=lookback_days,
            now_utc=now_utc,
        )

        if not args.dry_run:
            report_path.write_text(note_text, encoding="utf-8")
            update_card_file(card_path, auto_block, review_date, dry_run=False)
        else:
            update_card_file(card_path, auto_block, review_date, dry_run=True)

        summary_lines.append(
            f"- {project_id}: items={len(items)}, errors={len(errors)}, report={report_path}"
        )

    print("Project intelligence update complete")
    print(f"vault_root={vault_root}")
    print(f"lookback_days={lookback_days}, max_items={max_items}, dry_run={args.dry_run}")
    for line in summary_lines:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
