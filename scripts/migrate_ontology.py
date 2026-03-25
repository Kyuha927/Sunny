#!/usr/bin/env python3
"""
기존 Obsidian 노트 마이그레이션 스크립트

기존 ~280개 노트에 대해:
1. summary 가 비어있거나 "Auto-generated" → AI 요약으로 교체
2. 본문 내 Entity WikiLink 자동 삽입
3. type 재분류 (외부 출처 기사 → reference)

실행 전 반드시 git commit으로 백업할 것!
"""

import sys
import os
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from ontology_enricher import enrich_folder

VAULT_DIR = Path("/home/khyha/projects/Sunny")

SKIP_DIRS = {".obsidian", ".git", ".agent", "__pycache__", "scripts", "copilot", "Entities"}

def main():
    parser = argparse.ArgumentParser(description="기존 Obsidian 노트 일괄 온톨로지 마이그레이션")
    parser.add_argument("--dry-run", action="store_true", help="수정 없이 분석 결과만 출력")
    parser.add_argument("--folder", type=str, default=None, help="특정 폴더만 처리 (예: 'Google Discover/Articles')")
    parser.add_argument("--limit", type=int, default=0, help="처리할 최대 노트 수 (0=무제한)")
    args = parser.parse_args()

    if args.folder:
        target = VAULT_DIR / args.folder
        if not target.exists():
            print(f"❌ 폴더 없음: {target}")
            return
        print(f"📂 폴더 마이그레이션: {target}")
        results = enrich_folder(str(target), dry_run=args.dry_run)
    else:
        print(f"📦 전체 볼트 마이그레이션: {VAULT_DIR}")
        print(f"   스킵 폴더: {', '.join(SKIP_DIRS)}")
        
        total = {"enriched": 0, "skipped": 0, "errors": 0}
        processed = 0
        
        for root, dirs, files in os.walk(VAULT_DIR):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
            
            md_files = [f for f in files if f.endswith('.md') and not f.startswith('00_') and not f.startswith('.')]
            if not md_files:
                continue
                
            rel = os.path.relpath(root, VAULT_DIR)
            print(f"\n📁 {rel} ({len(md_files)}개 노트)")
            
            for md_file in sorted(md_files):
                if args.limit and processed >= args.limit:
                    print(f"\n⏹️  Limit 도달 ({args.limit}개)")
                    break
                    
                filepath = os.path.join(root, md_file)
                print(f"\n  📄 {md_file}")
                
                from ontology_enricher import enrich_note
                result = enrich_note(filepath, dry_run=args.dry_run)
                
                if result.get("skipped"):
                    total["skipped"] += 1
                    print(f"    ⏭️  스킵: {result.get('reason')}")
                elif result.get("error"):
                    total["errors"] += 1
                    print(f"    ❌ {result.get('error')}")
                else:
                    total["enriched"] += 1
                    
                processed += 1
                
            if args.limit and processed >= args.limit:
                break
                
        results = total
    
    mode_str = "[DRY RUN] " if args.dry_run else ""
    print(f"\n✨ {mode_str}마이그레이션 완료!")
    print(f"   보강: {results['enriched']}개")
    print(f"   스킵: {results['skipped']}개")
    print(f"   에러: {results['errors']}개")

if __name__ == "__main__":
    main()
