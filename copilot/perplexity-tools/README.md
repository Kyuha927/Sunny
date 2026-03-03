# Perplexity Copy-Paste Tools

## Build packets
```powershell
python build_perplexity_packets.py --vault "C:\Users\jhk92\OneDrive\문서\Obsidian Vault"
```

## Build packets for current open-tab style files
```powershell
python build_perplexity_packets.py --vault "C:\Users\jhk92\OneDrive\문서\Obsidian Vault" --patterns "enhanced_*.md" "sections_dump.md" "copilot/copilot-custom-prompts/*.md"
```

## Output
- `out/*.prompt.md` : paste each file to Perplexity
- `out/QUEUE.md` : processing order checklist
