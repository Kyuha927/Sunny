---
type: concept
tags:
  - workspace-links
created: 2026-03-25
summary: ""
---
# Studio Structure

> **🤖 [AGENT QUICKSTART & RULES]** 
> If you are an AI Agent (Antigravity, Codex, or Claude Code) reading this, your tasks are divided by comparative advantage:
> - **Antigravity (GUI)**: Creative Design, UI/UX, Master Planning, Orchestration.
> - **Codex CLI**: Very fast Terminal execution, Multi-threaded file discovery, Background parallel jobs.
> - **Claude Code CLI**: Deep codebase refactoring, heavy logic synthesis, architectural modifications.
> -> **SSOT (Single Source of Truth)**: `/home/khyha/codex-agentic-instructions.md` & `STUDIO.md`

Antigravity × Codex × Claude Code 3각 편대 비교우위 기반 프로젝트 역할 분담 체계입니다.

## 모델별 역할

| 역할 | Antigravity (GUI) | Codex CLI (GPT-5.4) | Claude Code CLI (Claude 3.7) |
|---|---|---|---|
| 기획/설계/비전 | ✅ 최우선 | | |
| 터미널/빌드 자동화 | | ✅ 최우선 | |
| 병렬 디스커버리 | | ✅ 최우선 (8스레드) | |
| 딥 리팩토링/아키텍트 | | | ✅ 최우선 |
| 검증/리뷰 | 판단/Critique | ✅ 빠른 Lint/Test | ✅ 깊은 로직 Review |
| 크리에이티브/UX | ✅ 최우선 | | |
| Obsidian 지식 관리 | ✅ 최우선 | | |

## 프로젝트별 주력

| 프로젝트 | 주력 | 경로 |
|---|---|---|
| 미연시 | Antigravity | `~/projects/미연시` |
| pixel-agents | 둘 다 | `~/다운로드/Windows_Projects/pixel-agents` |
| pixel-world | Codex | `~/다운로드/External_Backup_Projects/pixel-world` |
| msw2 | Codex | `~/다운로드/Windows_Projects/msw2` |
| comfyUI | Codex | `~/다운로드/External_Backup_Projects/comfyUI` |
| Sunny | Antigravity | `~/projects/Sunny` |

## 워크플로우 (The Sprint Cycle)
gstack의 7단계 검증된 스프린트 사이클(Think → Plan → Build → Review → Test → Ship → Reflect)을 따릅니다. 각 워크플로우는 다음 단계로 컨텍스트를 넘겨줍니다.

| Phase (단계) | 커맨드 (유사 gstack 역할) |
|---|---|
| **1. Think (기획)** | `/brainstorm`, `/design-review` (CEO/Product Manager) |
| **2. Plan (설계)** | `/sprint-plan`, `/tech-debt` (Eng Manager) |
| **3. Build (구현)** | `/claude-delegation`, 수동 코딩 (Engineer) |
| **4. Review (검토)** | `/code-review`, `/asset-audit` (Reviewer) |
| **5. Test (검증)** | `/verify-before-done`, `/build-check` (QA) |
| **6. Ship (배포)** | `/release-checklist`, `/git-push-policy` (Release Manager) |
| **7. Reflect (회고)** | `/weekly-review`, `/handover`, `/sync-obsidian` (Doc Engineer) |

*공통/인프라: `/start`, `/status`, `/fold1-check`*

## 기존 에이전트 (건드리지 않음)
- 미연시: `~/projects/미연시/agents/` (7개)
- Codex: `~/.codex/agents/` (3개: docs_researcher, reviewer, verifier)
