#!/usr/bin/env python3
"""
Ontology Enricher: AI 기반 노트 보강 모듈

Gemini 2.5 Flash API를 사용하여:
1. 1~2줄 핵심 요약 생성 → frontmatter summary 필드
2. 핵심 엔티티(기술/도구/인물/개념) 5~10개 추출
3. 본문 내 엔티티를 [[WikiLink]]로 자동 치환
4. Entities/ 폴더에 Entity 노트 자동 생성
5. type 재분류 (외부 기사 → reference, 학습 → lesson)
"""

import os
import re
import json
import time
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    print("⚠️  pip install requests 필요")
    raise

VAULT_DIR = Path("/home/khyha/projects/Sunny")
ENTITIES_DIR = VAULT_DIR / "Entities"
REGISTRY_FILE = VAULT_DIR / "scripts" / "entity_registry.json"

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

# ────────────────────────────────────────
# Gemini API 호출
# ────────────────────────────────────────

def call_gemini(prompt: str, max_retries: int = 3) -> str:
    """Gemini Flash API 호출. JSON 응답 기대."""
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY 환경변수가 설정되지 않았습니다.")

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 2048,
            "responseMimeType": "application/json"
        }
    }

    for attempt in range(max_retries):
        try:
            resp = requests.post(GEMINI_URL, json=payload, timeout=30)
            if resp.status_code == 429:
                wait = 2 ** (attempt + 1)
                print(f"  ⏳ Rate limit, {wait}초 대기...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            data = resp.json()
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            return text
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"  ❌ Gemini API 호출 실패: {e}")
                return ""
            time.sleep(1)
    return ""

# ────────────────────────────────────────
# Entity Registry 관리
# ────────────────────────────────────────

def load_registry() -> dict:
    if REGISTRY_FILE.exists():
        with open(REGISTRY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"entities": {}, "_meta": {"version": 1}}

def save_registry(registry: dict):
    registry["_meta"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    with open(REGISTRY_FILE, 'w', encoding='utf-8') as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)

def normalize_entity_name(name: str) -> str:
    """엔티티명 정규화: 앞뒤 공백 제거, 첫 글자 대문자"""
    name = name.strip()
    if name and name[0].isalpha() and name[0].islower():
        name = name[0].upper() + name[1:]
    return name

# ────────────────────────────────────────
# Entity 노트 생성
# ────────────────────────────────────────

def ensure_entity_note(entity_name: str, aliases: list = None, domain: str = "general"):
    """Entities/ 폴더에 해당 엔티티 노트가 없으면 생성"""
    ENTITIES_DIR.mkdir(exist_ok=True)
    safe_name = re.sub(r'[\\/?*:"<>|]', "", entity_name).strip()
    filepath = ENTITIES_DIR / f"{safe_name}.md"

    if filepath.exists():
        return  # 이미 존재

    aliases_str = ""
    if aliases:
        aliases_str = "\naliases:\n" + "\n".join(f"  - {a}" for a in aliases)

    content = f"""---
type: entity
tags:
  - entity
  - {domain}{aliases_str}
created: {datetime.now().strftime("%Y-%m-%d")}
summary: ""
---
# {entity_name}

> 이 노트는 AI에 의해 자동 생성된 엔티티 노트입니다.
> Backlink를 통해 이 개념이 등장하는 모든 문서를 확인할 수 있습니다.
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  🏷️  Entity 노트 생성: {safe_name}.md")

# ────────────────────────────────────────
# Frontmatter 파싱/수정
# ────────────────────────────────────────

def parse_frontmatter(content: str) -> tuple:
    """(frontmatter_dict, body) 반환. frontmatter 없으면 ({}, content)"""
    if not content.startswith("---"):
        return {}, content

    end_idx = content.find("---", 3)
    if end_idx == -1:
        return {}, content

    fm_text = content[3:end_idx].strip()
    body = content[end_idx + 3:].strip()

    # 간단한 YAML 파싱 (key: value 기반)
    fm = {}
    current_key = None
    current_list = None
    for line in fm_text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("- ") and current_key:
            if current_list is None:
                current_list = []
            current_list.append(stripped[2:].strip().strip('"'))
            fm[current_key] = current_list
        elif ": " in stripped or stripped.endswith(":"):
            if current_list is not None:
                current_list = None
            parts = stripped.split(": ", 1)
            current_key = parts[0].strip()
            val = parts[1].strip().strip('"') if len(parts) > 1 and parts[1].strip() else ""
            if val.startswith("[") and val.endswith("]"):
                fm[current_key] = [v.strip().strip('"') for v in val[1:-1].split(",")]
            else:
                fm[current_key] = val
            current_list = None if not isinstance(fm.get(current_key), list) else fm[current_key]

    return fm, body

def rebuild_frontmatter(fm: dict) -> str:
    """dict → YAML frontmatter 문자열"""
    lines = ["---"]
    for key, val in fm.items():
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {item}")
        else:
            if val and (" " in str(val) or ":" in str(val)):
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines)

def update_frontmatter_field(content: str, field: str, value) -> str:
    """파일 내용의 frontmatter 특정 필드를 업데이트. 프론트매터가 없으면 무시."""
    fm, body = parse_frontmatter(content)
    if not fm:
        return content
    fm[field] = value
    return rebuild_frontmatter(fm) + "\n" + body

# ────────────────────────────────────────
# 핵심: AI Enrichment
# ────────────────────────────────────────

ENRICH_PROMPT = """다음은 Obsidian 노트의 내용입니다. 분석하여 JSON으로 응답하세요.

### 요청사항:
1. "summary": 이 글의 핵심 내용을 한국어 1~2문장으로 요약
2. "entities": 이 글에서 핵심 기술/도구/인물/개념 키워드를 5~10개 추출 (배열)
   - 일반적인 단어("방법", "내용")가 아니라 고유명사나 전문 용어만
   - 예: "WebAssembly", "Claude Code", "React", "Transformer"
3. "type": 이 글의 성격 분류 (하나만 선택)
   - "reference": 외부 기사/블로그 스크래핑
   - "lesson": 직접 학습한 내용/경험
   - "concept": 개념 설명/정의
   - "project": 프로젝트 문서

### 노트 내용 (처음 3000자):
{content}

### JSON 형식으로만 응답:
{{"summary": "...", "entities": ["...", "..."], "type": "..."}}"""


def enrich_note(filepath: str, dry_run: bool = False) -> dict:
    """노트를 AI로 보강: summary, entities, WikiLinks, type"""
    path = Path(filepath)
    if not path.exists():
        return {"error": f"파일 없음: {filepath}"}

    content = path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(content)

    # 이미 enriched인 경우 스킵 (summary가 비어있지 않고 Auto-generated가 아닌 경우)
    existing_summary = fm.get("summary", "")
    if existing_summary and existing_summary not in ("", "Auto-generated by Agent", '""'):
        return {"skipped": True, "reason": "이미 보강됨"}

    # 본문이 너무 짧으면 스킵
    if len(body) < 50:
        return {"skipped": True, "reason": "본문 너무 짧음"}

    # Gemini 호출
    prompt = ENRICH_PROMPT.replace("{content}", body[:3000])
    raw_response = call_gemini(prompt)

    if not raw_response:
        return {"error": "Gemini 응답 없음"}

    try:
        # Gemini가 markdown fence로 감싸는 경우 제거
        cleaned = raw_response.strip()
        if cleaned.startswith("```"):
            cleaned = re.sub(r'^```(?:json)?\s*', '', cleaned)
            cleaned = re.sub(r'\s*```$', '', cleaned)
        result = json.loads(cleaned)
    except json.JSONDecodeError as e:
        # JSON 파싱 실패 시 정규식으로 추출 시도
        try:
            match = re.search(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', raw_response, re.DOTALL)
            if match:
                result = json.loads(match.group())
            else:
                return {"error": f"JSON 파싱 실패 ({e}): {raw_response[:300]}"}
        except Exception:
            return {"error": f"JSON 파싱 실패: {raw_response[:300]}"}

    summary = result.get("summary", "")
    entities = result.get("entities", [])
    note_type = result.get("type", "")

    if dry_run:
        return {"summary": summary, "entities": entities, "type": note_type, "dry_run": True}

    # 1. Summary 업데이트
    if summary:
        fm["summary"] = summary

    # 2. Type 업데이트
    if note_type and note_type in ("reference", "lesson", "concept", "project"):
        fm["type"] = note_type

    # 3. Entity WikiLink 삽입 (본문 내 첫 등장만)
    registry = load_registry()
    linked_entities = []

    for entity in entities:
        entity = normalize_entity_name(entity)
        if not entity or len(entity) < 2:
            continue

        # Registry에 등록
        if entity not in registry["entities"]:
            registry["entities"][entity] = {
                "aliases": [],
                "domain": "general",
                "created": datetime.now().strftime("%Y-%m-%d")
            }

        # 본문에서 엔티티 첫 등장을 WikiLink로 치환
        # 이미 [[Entity]] 형태인 경우는 건너뜀
        if f"[[{entity}]]" not in body:
            # 정확한 단어 경계 매칭 (대소문자 무시)
            pattern = re.compile(re.escape(entity), re.IGNORECASE)
            match = pattern.search(body)
            if match:
                # 첫 등장만 치환
                original = match.group()
                body = body[:match.start()] + f"[[{entity}|{original}]]" + body[match.end():]
                linked_entities.append(entity)

        # Entity 노트 생성
        ensure_entity_note(entity)

    save_registry(registry)

    # 재조립
    new_content = rebuild_frontmatter(fm) + "\n" + body
    path.write_text(new_content, encoding='utf-8')

    print(f"  ✅ 보강 완료: {path.name}")
    print(f"     요약: {summary[:60]}...")
    print(f"     엔티티: {', '.join(entities[:5])}{'...' if len(entities) > 5 else ''}")
    print(f"     WikiLink 삽입: {len(linked_entities)}개")

    return {
        "summary": summary,
        "entities": entities,
        "linked": linked_entities,
        "type": note_type
    }


def enrich_folder(folder_path: str, dry_run: bool = False) -> dict:
    """폴더 내 모든 .md 파일을 일괄 보강"""
    folder = Path(folder_path)
    if not folder.exists():
        return {"error": f"폴더 없음: {folder_path}"}

    results = {"enriched": 0, "skipped": 0, "errors": 0}

    for md_file in sorted(folder.rglob("*.md")):
        # MOC 파일과 Entity 파일은 스킵
        if md_file.name.startswith("00_") or md_file.name.startswith("."):
            continue
        if "Entities" in str(md_file):
            continue

        print(f"\n📄 처리 중: {md_file.name}")
        result = enrich_note(str(md_file), dry_run=dry_run)

        if result.get("skipped"):
            results["skipped"] += 1
            print(f"  ⏭️  스킵: {result.get('reason')}")
        elif result.get("error"):
            results["errors"] += 1
            print(f"  ❌ 에러: {result.get('error')}")
        else:
            results["enriched"] += 1

        # Rate limit 방지 (무료 티어: 15 RPM, 즉 4초당 1회)
        time.sleep(4.5)

    return results


# ────────────────────────────────────────
# CLI
# ────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Ontology Enricher: AI 기반 노트 보강")
    parser.add_argument("target", help="보강할 노트 파일 경로 또는 폴더 경로")
    parser.add_argument("--dry-run", action="store_true", help="실제 수정 없이 AI 분석 결과만 출력")
    parser.add_argument("--folder", action="store_true", help="타겟을 폴더로 취급하여 일괄 처리")

    args = parser.parse_args()

    if args.folder:
        print(f"📂 폴더 일괄 보강: {args.target}")
        results = enrich_folder(args.target, dry_run=args.dry_run)
        print(f"\n✨ 완료! 보강: {results['enriched']}, 스킵: {results['skipped']}, 에러: {results['errors']}")
    else:
        print(f"📄 단일 노트 보강: {args.target}")
        result = enrich_note(args.target, dry_run=args.dry_run)
        print(f"\n결과: {json.dumps(result, ensure_ascii=False, indent=2)}")
