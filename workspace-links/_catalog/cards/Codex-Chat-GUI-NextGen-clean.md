---
type: project-card
project_name: "Codex-Chat-GUI-NextGen-clean"
display_name: "Codex Chat GUI NextGen"
entry_link: "[[workspace-links/projects/Codex-Chat-GUI-NextGen-clean/README|Codex Chat GUI NextGen]]"
domain: agent-ui
artifact_type:
  - codebase
  - migration-handoff
  - ops-runbook
execution_mode: build
phase: active
review_cycle: weekly
priority: p1
risk_level: medium
workflow_stage: "Migration Cleanup"
sequence_order: 14
kanban_lane: "This Week"
plan_start: 2026-03-18
plan_end: 2026-03-25
progress_pct: 78
status_now: "Ubuntu ext4 기준 fresh clone 작업본으로 기준선을 교체했고, 꼭 필요한 로컬 파일만 재적용한 상태"
major_issues:
  - "기존 dirty 작업본 히스토리가 커서 Git 기준 완전 클린 상태와는 분리 관리가 필요함"
  - "Windows /mnt/c 직접 복사는 작은 파일 메타데이터 비용 때문에 매우 느림"
  - "`.env`와 외부 시크릿은 Git 밖에서 계속 관리해야 함"
next_actions:
  - "로컬 전용 9개 파일의 커밋 여부를 결정"
  - "Ubuntu 복원 후 smoke, route, codex store 검증 재실행"
  - "Obsidian 프로젝트 링크와 업데이트 루틴을 주간 점검 흐름에 편입"
last_review: 2026-03-18
relationship_tags:
  - same-domain
  - cross-domain
relations:
  - target: "[[workspace-links/_catalog/cards/Antigravity-Brain]]"
    kind: documentation-source
    direction: in
    strength: high
    reason: "에이전트 운영 규칙과 인계 체계를 직접 참조함"
  - target: "[[workspace-links/_catalog/cards/Copilot-Prompts]]"
    kind: prompt-support
    direction: bi
    strength: medium
    reason: "프롬프트 자산과 실사용 GUI 작업 흐름이 연결됨"
---

# Codex-Chat-GUI-NextGen-clean

## 목적
- 기존 Codex Chat GUI 계열 기능을 NextGen Web UI 기준으로 정리하고, Ubuntu ext4 기준의 안정적인 작업 기준선을 유지합니다.

## 분류 근거
- `domain`: agent-ui
- `artifact_type`: codebase + migration-handoff + ops-runbook
- `execution_mode`: build

## 연관 프로젝트
- [[workspace-links/_catalog/cards/Antigravity-Brain]] - documentation-source
- [[workspace-links/_catalog/cards/Copilot-Prompts]] - prompt-support

## 현황
- fresh clone 기준선으로 표준 작업 경로를 교체했고, commit 기준으로는 원격 최신과 동기화되어 있습니다.

## 문제
- 작업 중 누적된 dirty 워크트리와 Git 추적 외 파일이 많아, clean clone과 local continuity 자료를 분리 관리해야 합니다.

## 다음 할 일
- migration 전용 문서와 스크립트를 Git에 포함할지 결정하고, Ubuntu 복원 검증을 다시 실행합니다.
