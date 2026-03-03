# OpenClaw Know-How Pack (2026-02-28)

This file summarizes high-impact OpenClaw practices from official docs and current local runtime checks.

## 0) Current runtime reality (local check)

- OpenClaw default model: `ollama/qwen3:8b`
- Fallback models: `[]` (none configured)
- Active session model (status --deep): `qwen3:8b`
- WSL CLI issue: current WSL node is `v20.20.0`, but OpenClaw requires Node `>=22.12.0` (CLI cannot run in current WSL shell).
- Windows runtime is fine (Node `v24.13.1` via `C:\Program Files\nodejs\node.exe`).

## 1) Why replies feel weak right now

- `qwen3:8b` is a small local model with no fallback chain. When it underperforms, there is no automatic model upgrade path.
- Official model docs say selection order is:
  1. `agents.defaults.model.primary`
  2. `agents.defaults.model.fallbacks` (in order)
  3. auth-profile rotation inside provider before next model

## 2) Immediate quality fix (10 minutes)

Use high-quality primary + explicit fallbacks, then verify:

```powershell
& "C:\Program Files\nodejs\node.exe" "C:\Users\jhk92\AppData\Roaming\npm\node_modules\openclaw\openclaw.mjs" models set openai-codex/gpt-5.3-codex
& "C:\Program Files\nodejs\node.exe" "C:\Users\jhk92\AppData\Roaming\npm\node_modules\openclaw\openclaw.mjs" models fallbacks add google/gemini-2.5-pro
& "C:\Program Files\nodejs\node.exe" "C:\Users\jhk92\AppData\Roaming\npm\node_modules\openclaw\openclaw.mjs" models fallbacks add google/gemini-2.5-flash
& "C:\Program Files\nodejs\node.exe" "C:\Users\jhk92\AppData\Roaming\npm\node_modules\openclaw\openclaw.mjs" models status --json
```

Note: if `agents.defaults.models` is set, it is an allowlist. A model outside allowlist can cause "model is not allowed" and feel like no reply.

## 3) Session-level quality controls (chat side)

- Use `/model` and `/model list` to switch quickly.
- Use `/model status` to inspect auth candidates and provider endpoint info.
- Use `/new` or `/reset` to clear stale context when behavior degrades.

## 4) Auth health and failover hygiene

- Use machine-checkable auth health:

```bash
openclaw models status --check
```

Exit codes:
- `0`: ok
- `1`: missing/expired credential
- `2`: expiring soon (within 24h)

- Keep multiple auth profiles per provider only when needed, and pin order when behavior must be stable:
  - `auth.order[provider] = ["provider:profileId"]`

## 5) Cron + heartbeat orchestration pattern

- Heartbeat: best for batched/context-aware periodic checks.
- Cron: best for exact timing, isolated runs, per-job model overrides.
- Best practice from official docs: combine both:
  - heartbeat for routine monitoring
  - isolated cron for precise reports/reminders

## 6) Tool policy tuning (large quality/safety impact)

- Define a base profile with `tools.profile` (`minimal`, `coding`, `messaging`, `full`).
- Use `tools.byProvider` to narrow risky tools for weaker models/providers.
- Deny wins over allow (`tools.deny` has priority).
- Recommended pattern:
  - strong model: broader tool profile
  - small model: narrower profile (or no web/browser/exec)

## 7) Security hardening (must-do)

- Run audits regularly:

```bash
openclaw security audit
openclaw security audit --deep
openclaw security audit --fix
```

- Official guidance warns small models with broad tools are risky; pair small models with sandbox + strict tool deny.
- Keep gateway loopback/private, enforce pairing/allowlists for channels, tighten file permissions on `~/.openclaw`.

## 8) Browser reliability tips

- Prefer managed `openclaw` profile over extension relay for deterministic automation.
- Linux CDP launch issues: set `browser.executablePath`, and use `noSandbox`/attach-only when needed.
- For browser failures, first ladder:
  - `openclaw browser status`
  - `openclaw browser start --browser-profile openclaw`
  - `openclaw logs --follow`
  - `openclaw doctor`

## 9) Troubleshooting ladder (automation/model stalls)

```bash
openclaw status
openclaw gateway status
openclaw logs --follow
openclaw doctor
openclaw channels status --probe
openclaw cron status
openclaw cron list
openclaw system heartbeat last
```

This is the official troubleshooting command ladder for cron/heartbeat delivery issues.

## 10) Environment consistency checklist

- Keep both host and WSL on supported Node (>=22.12.0) so CLI behavior is consistent.
- In this environment:
  - WSL node upgrade needed
  - Windows runtime already supported
- Update available was reported by local status:
  - `openclaw update` (recommended before deeper tuning)

## Sources (official)

- https://docs.openclaw.ai/concepts/models
- https://docs.openclaw.ai/concepts/model-failover
- https://docs.openclaw.ai/concepts/model-providers
- https://docs.openclaw.ai/tools/slash-commands
- https://docs.openclaw.ai/tools
- https://docs.openclaw.ai/automation/cron-jobs
- https://docs.openclaw.ai/automation/cron-vs-heartbeat
- https://docs.openclaw.ai/automation/troubleshooting
- https://docs.openclaw.ai/automation/auth-monitoring
- https://docs.openclaw.ai/gateway/security
- https://docs.openclaw.ai/tools/browser
- https://docs.openclaw.ai/tools/browser-linux-troubleshooting
- https://raw.githubusercontent.com/openclaw/openclaw/main/README.md
