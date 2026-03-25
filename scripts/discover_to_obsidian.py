#!/usr/bin/env python3
"""
Google Discover JSONL → Obsidian 마크다운 변환기

Tasker + AutoNotification으로 수집한 Google 알림 추천 기사를
날짜별 Obsidian 노트로 변환합니다.

Usage:
    python discover_to_obsidian.py
    python discover_to_obsidian.py --input /path/to/google_discover.jsonl
    python discover_to_obsidian.py --dry-run
"""

import json
import argparse
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Paths
VAULT_DIR = Path(__file__).resolve().parent.parent
DISCOVER_DIR = VAULT_DIR / "Google Discover"
MOC_FILE = DISCOVER_DIR / "_index.md"
DEFAULT_INPUT = Path.home() / "sync" / "tasker" / "google_discover.jsonl"
PROCESSED_FILE = DISCOVER_DIR / ".processed_hashes"


def load_processed_hashes() -> set:
    """이미 처리된 항목의 해시를 로드."""
    if PROCESSED_FILE.exists():
        return set(PROCESSED_FILE.read_text().strip().splitlines())
    return set()


def save_processed_hashes(hashes: set):
    """처리된 해시 저장."""
    PROCESSED_FILE.write_text("\n".join(sorted(hashes)) + "\n")


def compute_hash(entry: dict) -> str:
    """항목의 고유 해시 생성 (중복 방지)."""
    key = f"{entry.get('date', '')}{entry.get('time', '')}{entry.get('title', '')}"
    return hashlib.md5(key.encode()).hexdigest()[:12]


def parse_jsonl(filepath: Path) -> list[dict]:
    """JSONL 파일을 파싱."""
    entries = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                entries.append(entry)
            except json.JSONDecodeError as e:
                print(f"⚠️  Line {line_num} 파싱 실패: {e}")
    return entries


def normalize_date(date_str: str) -> str:
    """Tasker 날짜 형식을 YYYY-MM-DD로 변환."""
    # Tasker %DATE는 보통 MM-DD-YY 또는 YYYY-MM-DD
    for fmt in ("%Y-%m-%d", "%m-%d-%y", "%m.%d.%y", "%Y.%m.%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return date_str  # 변환 실패 시 원본 반환


def normalize_time(time_str: str) -> str:
    """시간 형식을 HH:MM으로 정규화."""
    for fmt in ("%H.%M", "%H:%M:%S", "%H:%M", "%I:%M %p", "%I.%M%p"):
        try:
            return datetime.strptime(time_str, fmt).strftime("%H:%M")
        except ValueError:
            continue
    return time_str


def extract_domain(url: str) -> str:
    """URL에서 도메인 추출."""
    if not url:
        return "—"
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path
        # www. 제거
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except Exception:
        return "—"


def generate_daily_note(date: str, entries: list[dict]) -> str:
    """일별 Obsidian 마크다운 노트 생성."""
    lines = [
        "---",
        "type: discover-archive",
        f"date: {date}",
        "tags:",
        "  - google-discover",
        "  - archive",
        f"article_count: {len(entries)}",
        "---",
        f"# Google Discover — {date}",
        "",
        f"> 총 **{len(entries)}**개의 추천 기사",
        "",
        "| 시간 | 제목 | 출처 | 링크 |",
        "|------|------|------|------|",
    ]

    for entry in sorted(entries, key=lambda e: e.get("time", "")):
        time = normalize_time(entry.get("time", "—"))
        title = entry.get("title", "(제목 없음)").replace("|", "\\|")
        url = entry.get("url", "")
        domain = extract_domain(url)

        if url:
            link = f"[열기]({url})"
        else:
            link = "—"

        lines.append(f"| {time} | {title} | {domain} | {link} |")

    # 본문/요약이 있는 항목은 아래에 상세 추가
    details = [e for e in entries if e.get("body")]
    if details:
        lines.extend(["", "## 상세", ""])
        for entry in sorted(details, key=lambda e: e.get("time", "")):
            time = normalize_time(entry.get("time", "—"))
            title = entry.get("title", "(제목 없음)")
            body = entry.get("body", "")
            lines.extend([
                f"### {title}",
                f"_{time}_",
                "",
                body,
                "",
            ])

    lines.extend(["", "---", f"_자동 생성: {datetime.now().strftime('%Y-%m-%d %H:%M')}_", ""])
    return "\n".join(lines)


def update_moc(dates: list[str]):
    """MOC (_index.md) 의 최근 아카이브 섹션 업데이트."""
    if not MOC_FILE.exists():
        return

    content = MOC_FILE.read_text(encoding="utf-8")

    # 최근 아카이브 섹션 교체
    marker_start = "## 최근 아카이브"
    marker_end = "## 사용법"

    if marker_start in content and marker_end in content:
        before = content[:content.index(marker_start)]
        after = content[content.index(marker_end):]

        # 최근 30일분 링크 생성
        sorted_dates = sorted(dates, reverse=True)[:30]
        links = "\n".join(f"- [[Google Discover/{d}|{d}]]" for d in sorted_dates)

        new_section = f"{marker_start}\n\n{links}\n\n"
        content = before + new_section + after
        MOC_FILE.write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Google Discover JSONL → Obsidian 변환기")
    parser.add_argument("--input", "-i", type=Path, default=DEFAULT_INPUT,
                        help="JSONL 입력 파일 경로")
    parser.add_argument("--dry-run", action="store_true",
                        help="실제 파일 생성 없이 미리보기만")
    parser.add_argument("--force", action="store_true",
                        help="이미 처리된 항목도 다시 처리")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"❌ 입력 파일 없음: {args.input}")
        print("   Tasker에서 데이터를 수집한 후 동기화하세요.")
        return

    # JSONL 파싱
    entries = parse_jsonl(args.input)
    if not entries:
        print("ℹ️  처리할 항목이 없습니다.")
        return

    print(f"📥 {len(entries)}개 항목 로드됨")

    # 중복 필터링
    processed = set() if args.force else load_processed_hashes()
    new_entries = []
    new_hashes = set()
    for entry in entries:
        h = compute_hash(entry)
        if h not in processed:
            new_entries.append(entry)
            new_hashes.add(h)

    if not new_entries:
        print("ℹ️  새로운 항목이 없습니다.")
        return

    print(f"🆕 {len(new_entries)}개 새 항목 처리 예정")

    # 날짜별 그룹핑
    by_date = defaultdict(list)
    for entry in new_entries:
        date = normalize_date(entry.get("date", datetime.now().strftime("%Y-%m-%d")))
        by_date[date].append(entry)

    # 노트 생성
    DISCOVER_DIR.mkdir(parents=True, exist_ok=True)

    for date, day_entries in sorted(by_date.items()):
        note_path = DISCOVER_DIR / f"{date}.md"

        if note_path.exists() and not args.force:
            # 기존 노트에 새 항목 병합
            existing_content = note_path.read_text(encoding="utf-8")
            # 기존 항목 수 카운트 (테이블 행)
            existing_rows = existing_content.count("\n|") - 1  # 헤더 제외
            print(f"  📝 {date}: 기존 {existing_rows}개 + 새 {len(day_entries)}개")

            # 기존 노트의 JSONL을 다시 읽어서 합쳐야 하지만,
            # 단순히 새 데이터로 전체 재생성 (해시로 중복 방지됨)
            all_date_entries = [e for e in entries if normalize_date(e.get("date", "")) == date]
            content = generate_daily_note(date, all_date_entries)
        else:
            content = generate_daily_note(date, day_entries)

        if args.dry_run:
            print(f"\n{'='*60}")
            print(f"📄 {note_path}")
            print(f"{'='*60}")
            print(content[:500])
            if len(content) > 500:
                print(f"  ... (총 {len(content)}자)")
        else:
            note_path.write_text(content, encoding="utf-8")
            print(f"  ✅ {note_path.name} 생성 ({len(day_entries)}개 기사)")

    if not args.dry_run:
        # 처리 해시 저장
        processed.update(new_hashes)
        save_processed_hashes(processed)

        # MOC 업데이트
        all_dates = [p.stem for p in DISCOVER_DIR.glob("????-??-??.md")]
        update_moc(all_dates)

        print(f"\n✨ 완료! {len(new_entries)}개 기사 → {len(by_date)}개 일별 노트")


if __name__ == "__main__":
    main()
