from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

DEFAULT_SYSTEM_PROMPT = """Role: Technical documentation enhancement editor.
Goal: Improve the markdown document using current, evidence-backed research.
Rules:
- Add source URLs for factual claims.
- Use absolute dates (YYYY-MM-DD) for recent facts.
- Remove duplication and improve structure.
Output:
1) Top 10 improvement points
2) Research summary with sources
3) Final integrated markdown ready to paste
""".strip()


def read_text_fallback(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "cp949", "euc-kr", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except Exception:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def resolve_patterns(root: Path, patterns: Iterable[str]) -> list[Path]:
    found: list[Path] = []
    seen: set[str] = set()
    for pat in patterns:
        for p in root.rglob(pat):
            if not p.is_file():
                continue
            key = str(p.resolve()).lower()
            if key in seen:
                continue
            seen.add(key)
            found.append(p)
    return sorted(found)


def build_prompt_packet(vault_root: Path, md_path: Path) -> str:
    rel = md_path.resolve().relative_to(vault_root.resolve())
    content = read_text_fallback(md_path)
    return (
        f"# File\n{rel.as_posix()}\n\n"
        f"# Prompt\n{DEFAULT_SYSTEM_PROMPT}\n\n"
        "Document source:\n"
        "```markdown\n"
        f"{content}\n"
        "```\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Perplexity copy-paste packets from Obsidian markdown files")
    parser.add_argument("--vault", required=True, help="Obsidian Vault root path")
    parser.add_argument("--patterns", nargs="+", default=["enhanced_*.md", "sections_dump.md"], help="Glob patterns under vault")
    parser.add_argument("--out", default="copilot/perplexity-tools/out", help="Output folder relative to vault")
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.exists() or not vault.is_dir():
        print(f"[FAIL] vault not found: {vault}")
        return 1

    targets = resolve_patterns(vault, args.patterns)
    if not targets:
        print("[FAIL] no markdown files matched patterns")
        print("patterns:", ", ".join(args.patterns))
        return 1

    out_dir = (vault / args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    index_lines = ["# Perplexity Copy-Paste Queue", ""]
    for idx, md in enumerate(targets, start=1):
        packet = build_prompt_packet(vault, md)
        filename = f"{idx:03d}_{md.stem}.prompt.md"
        packet_path = out_dir / filename
        packet_path.write_text(packet, encoding="utf-8")
        rel_md = md.resolve().relative_to(vault)
        rel_packet = packet_path.resolve().relative_to(vault)
        index_lines.append(f"- [{idx:03d}] `{rel_md.as_posix()}` -> `{rel_packet.as_posix()}`")

    (out_dir / "QUEUE.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"[OK] packets: {len(targets)}")
    print(f"[OK] out dir: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
