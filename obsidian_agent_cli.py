#!/usr/bin/env python3
import argparse
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from obsidian_agent_tools import read_moc, write_lesson_learned

VAULT_DIR = "/home/khyha/projects/Sunny"

def main():
    parser = argparse.ArgumentParser(description="Obsidian Agentic RAG CLI Tool for OpenClaw/VSCode")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Command: read
    read_parser = subparsers.add_parser("read", help="Read Map of Contents (MOC) for a specific keyword")
    read_parser.add_argument("--keyword", required=True, help="Folder or domain keyword (e.g., 'OpenClaw')")

    # Command: write
    write_parser = subparsers.add_parser("write", help="Write a lesson learned and update the MOC")
    write_parser.add_argument("--dir", required=True, help="Relative target directory (e.g., 'OpenClaw/Lessons')")
    write_parser.add_argument("--title", required=True, help="Title of the lesson/note")
    write_parser.add_argument("--content", required=True, help="Markdown content of the note")
    write_parser.add_argument("--tags", default="", help="Comma-separated tags (e.g., 'ai, automation')")
    write_parser.add_argument("--type", default="lesson",
                             choices=["lesson", "reference", "concept", "project", "daily-log"],
                             help="Note type (default: lesson)")
    write_parser.add_argument("--summary", default="", help="1-2 line summary")
    write_parser.add_argument("--auto-enrich", action="store_true",
                             help="AI로 자동 보강 (summary, WikiLink, Entity)")

    # Command: enrich
    enrich_parser = subparsers.add_parser("enrich", help="AI로 기존 노트 보강 (summary, entities, WikiLinks)")
    enrich_parser.add_argument("--path", required=True, help="보강할 노트 파일 경로 또는 폴더 경로")
    enrich_parser.add_argument("--folder", action="store_true", help="폴더 내 모든 노트 일괄 보강")
    enrich_parser.add_argument("--dry-run", action="store_true", help="수정 없이 분석 결과만 출력")

    # Command: entities
    entities_parser = subparsers.add_parser("entities", help="Entity Registry 관리")
    entities_parser.add_argument("--list", action="store_true", help="등록된 엔티티 목록 출력")

    args = parser.parse_args()

    if args.command == "read":
        print(read_moc(args.keyword))
    
    elif args.command == "write":
        tag_list = [tag.strip() for tag in args.tags.split(",")] if args.tags else []
        result = write_lesson_learned(
            args.dir, args.title, args.content, tags=tag_list,
            note_type=args.type, summary=args.summary,
            auto_enrich=getattr(args, 'auto_enrich', False)
        )
        print(result)

    elif args.command == "enrich":
        sys.path.insert(0, os.path.join(VAULT_DIR, "scripts"))
        from ontology_enricher import enrich_note, enrich_folder
        if args.folder:
            print(f"📂 폴더 일괄 보강: {args.path}")
            results = enrich_folder(args.path, dry_run=args.dry_run)
            print(f"\n✨ 완료! 보강: {results['enriched']}, 스킵: {results['skipped']}, 에러: {results['errors']}")
        else:
            print(f"📄 단일 노트 보강: {args.path}")
            import json
            result = enrich_note(args.path, dry_run=args.dry_run)
            print(f"\n결과: {json.dumps(result, ensure_ascii=False, indent=2)}")

    elif args.command == "entities":
        sys.path.insert(0, os.path.join(VAULT_DIR, "scripts"))
        from ontology_enricher import load_registry
        registry = load_registry()
        entities = registry.get("entities", {})
        if not entities:
            print("📋 등록된 엔티티가 없습니다.")
        else:
            print(f"📋 등록된 엔티티: {len(entities)}개\n")
            for name, meta in sorted(entities.items()):
                aliases = meta.get("aliases", [])
                domain = meta.get("domain", "")
                alias_str = f" (aka: {', '.join(aliases)})" if aliases else ""
                print(f"  • {name}{alias_str} [{domain}]")

if __name__ == "__main__":
    main()
