#!/usr/bin/env bash
set -euo pipefail
cd /home/khyha/projects/Sunny
PROMPT_CONTENT="$(</home/khyha/projects/Sunny/codex-handoffs/20260322_233434_agent-next-steps/relay_prompt.txt)"
exec /home/khyha/.local/bin/codex exec -C /home/khyha/projects/Sunny --skip-git-repo-check --add-dir /home/khyha/projects/Sunny/codex-handoffs/20260322_233434_agent-next-steps --json --ephemeral -o /home/khyha/projects/Sunny/codex-handoffs/20260322_233434_agent-next-steps/final.md "$PROMPT_CONTENT" > /home/khyha/projects/Sunny/codex-handoffs/20260322_233434_agent-next-steps/events.jsonl 2> /home/khyha/projects/Sunny/codex-handoffs/20260322_233434_agent-next-steps/relay.stderr
