---
type: project-card
project_name: "OpenClaw"
display_name: "OpenClaw 운영 허브"
entry_link: "[[OpenClaw]]"
domain: agent-ops
artifact_type:
  - ops-logs
  - design-doc
  - research-notes
execution_mode: operate
phase: active
review_cycle: daily
priority: p1
risk_level: medium
workflow_stage: "Ops Control"
sequence_order: 60
kanban_lane: "Review"
plan_start: 2026-02-18
plan_end: 2026-03-14
progress_pct: 55
status_now: "운영 허브는 구축되어 있고 프로젝트 증가에 따른 관리 자동화가 필요함"
major_issues:
  - "프로젝트 수가 늘면 수동 정리 비용이 증가"
  - "브리프-실행 로그-리서치 연결이 일부 수작업 의존"
next_actions:
  - "프로젝트 브리프 갱신 규칙 자동 점검"
  - "코드 트래커/리서치 카드 링크 무결성 체크"
last_review: 2026-03-03
relationship_tags:
  - same-domain
  - cross-domain
relations:
  - target: "[[workspace-links/_catalog/cards/Antigravity-CodeTracker]]"
    kind: telemetry-source
    direction: in
    strength: high
    reason: "운영 텔레메트리 수신"
  - target: "[[workspace-links/_catalog/cards/Antigravity-Brain]]"
    kind: knowledge-sync
    direction: bi
    strength: medium
    reason: "리서치 산출물과 운영 태스크 동기화"
  - target: "[[workspace-links/_catalog/cards/MSW-VampireSurvivors]]"
    kind: project-ops
    direction: bi
    strength: medium
    reason: "실행 프로젝트 관제"
  - target: "[[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro]]"
    kind: project-ops
    direction: bi
    strength: low
    reason: "실험 프로젝트 관제"
  - target: "[[workspace-links/_catalog/cards/Copilot-Prompts]]"
    kind: ops-support
    direction: in
    strength: medium
    reason: "운영용 프롬프트 입력"
---

# OpenClaw

## 목적
- 프로젝트 운영/추적/의사결정을 한 지점에서 관리합니다.

## 분류 근거
- `domain`: agent-ops
- `artifact_type`: ops-logs + design-doc + research-notes
- `execution_mode`: operate

## 연관 프로젝트
- [[workspace-links/_catalog/cards/Antigravity-CodeTracker]] - telemetry-source
- [[workspace-links/_catalog/cards/Antigravity-Brain]] - knowledge-sync
- [[workspace-links/_catalog/cards/MSW-VampireSurvivors]] - project-ops
- [[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro]] - project-ops
- [[workspace-links/_catalog/cards/Copilot-Prompts]] - ops-support

## 현황
- 운영 허브 역할은 수행 중이며 자동화 규칙 강화가 필요합니다.

## 문제
- 연결된 프로젝트가 늘수록 수동 동기화 비용이 큽니다.

## 다음 할 일
- 링크 무결성과 브리프 갱신 상태를 자동 점검합니다.

<!-- AUTO_INTEL:START -->
## 자동 인텔리전스
- 마지막 업데이트: 2026-03-03 00:06 UTC
- 수집 범위: 최근 30일
- 수집 건수: 10건
- 리포트: [[workspace-links/_catalog/updates/OpenClaw/2026-03-03]]

### 핵심 시그널
- [Bosch Introduces “Manufacturing Co-Intelligence” at Hannover Messe 2026 Press Preview - 산업일보](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9uNE5uaE95N1JnNHFxX0V0cTd5bHloRDh3emo1YlowQXlUU1JJZVFPR3FDOVhLQ0I1Z25SMTJPNHAzTlZtYzlscg?oc=5) (GoogleNews: AI agent orchestration framework, 2026-03-01)
- [KT Showcases AI and K-Culture Innovations at MWC 2026 in Barcelona - Korea IT Times](https://news.google.com/rss/articles/CBMicEFVX3lxTE5NZlcwR1MwTW1pcEc0TTdBeXJFdW1HQXNHUUxYWEl1U2NRQWNEdEdYZUhUc29aOW1BaFoxRTdSdE02LXYxV1FyV2o2LUV3bmdWX0JTOWprNjBhMFRkX21USTJvV3M1LUQ5cE1HaUFhNmk?oc=5) (GoogleNews: AI agent orchestration framework, 2026-03-02)
- ["광화문이 바르셀로나로"…KT, K-컬처 입힌 AX 전략 공개 - 네이트](https://news.google.com/rss/articles/CBMieEFVX3lxTFBFSHhaTWtYeTBkdGlYbGVwQlN2ZTlHYnVIWU1oWkl1dHg3NXcyNzdTVWNQM0JrYlQySFUtRkFIOXlWYTluRFUyWFU4MGNCNHM3YXRQMUtBVzBjMndobW5rTEZYTzZ2WHd2bDhkT0k0MzF0cGtTTVJ2Vw?oc=5) (GoogleNews: AI agent orchestration framework, 2026-03-01)
<!-- AUTO_INTEL:END -->
