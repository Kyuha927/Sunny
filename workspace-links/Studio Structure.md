# Studio Structure

Antigravity × Codex 비교우위 기반 역할 분담.
SSOT: `~/다운로드/.agent/agents/STUDIO.md`

## 모델별 역할

| 역할 | Antigravity (Claude) | Codex (GPT-5.4) |
|---|---|---|
| 설계/비전 | ✅ | |
| 터미널/빌드 | | ✅ (Terminal-Bench 75%) |
| 병렬 실행 | | ✅ (8스레드) |
| 검증/리뷰 | | ✅ (reviewer/verifier) |
| 크리에이티브 | ✅ | |
| Obsidian | ✅ | |

## 프로젝트별 주력

| 프로젝트 | 주력 | 경로 |
|---|---|---|
| 미연시 | Antigravity | `~/projects/미연시` |
| pixel-agents | 둘 다 | `~/다운로드/Windows_Projects/pixel-agents` |
| pixel-world | Codex | `~/다운로드/External_Backup_Projects/pixel-world` |
| msw2 | Codex | `~/다운로드/Windows_Projects/msw2` |
| comfyUI | Codex | `~/다운로드/External_Backup_Projects/comfyUI` |
| Sunny | Antigravity | `~/projects/Sunny` |

## 워크플로우 (슬래시 커맨드)

| 분류 | 커맨드 |
|---|---|
| 관리 | `/start`, `/sprint-plan`, `/status` |
| 코드 | `/code-review`, `/tech-debt`, `/perf-profile` |
| 크리에이티브 | `/brainstorm`, `/design-review`, `/asset-audit` |
| 배포 | `/build-check`, `/release-checklist` |
| 지식 | `/sync-obsidian`, `/handover`, `/weekly-review` |
| 인프라 | `/fold1-check` |

## 기존 에이전트 (건드리지 않음)
- 미연시: `~/projects/미연시/agents/` (7개)
- Codex: `~/.codex/agents/` (3개: docs_researcher, reviewer, verifier)
