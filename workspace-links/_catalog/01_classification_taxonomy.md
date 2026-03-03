# 프로젝트 분류 체계

## 1) Domain
- `game-dev`
- `agent-ops`
- `knowledge-rnd`
- `prompt-ops`

## 2) Artifact Type
- `codebase`
- `design-doc`
- `research-notes`
- `ops-logs`
- `prompt-library`
- `automation`

## 3) Execution Mode
- `build`
- `operate`
- `research`
- `archive`

## 4) Phase
- `active`
- `incubation`
- `maintenance`
- `paused`
- `archived`

## 5) Review Cycle
- `daily`
- `weekly`
- `monthly`
- `on-demand`

## 6) Execution Snapshot Fields
- `workflow_stage`: 실행 흐름 단계명
- `sequence_order`: 순서도 상 단계 번호
- `kanban_lane`: Trello형 실행 레인 (`Backlog` | `This Week` | `In Progress` | `Blocked` | `Review` | `Done`)
- `plan_start`: 간트 시작일 (`YYYY-MM-DD`)
- `plan_end`: 간트 종료일 (`YYYY-MM-DD`)
- `progress_pct`: 진행률 (`0-100`)
- `status_now`: 현재 상태 1문장 요약
- `major_issues`: 현재 핵심 문제(최소 1개)
- `next_actions`: 다음 실행 항목(최소 1개)
- `risk_level`: `low` | `medium` | `high`

## 7) Relation Kind
- `experiment-branch`
- `upstream-source`
- `research-input`
- `decision-source`
- `ops-support`
- `ops-sync`
- `execution-tracking`
- `research-feedback`
- `prompt-source`
- `prompt-asset`
- `project-ops`
- `telemetry-source`
- `knowledge-sync`
- `build-support`

## 8) Relation Direction
- `in`
- `out`
- `bi`
