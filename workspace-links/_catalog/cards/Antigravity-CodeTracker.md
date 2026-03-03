---
type: project-card
project_name: "Antigravity-CodeTracker"
display_name: "실행 로그·코드 추적 허브"
entry_link: "[[workspace-links/antigravity/code_tracker]]"
domain: agent-ops
artifact_type:
  - ops-logs
  - automation
execution_mode: operate
phase: active
review_cycle: daily
priority: p1
risk_level: medium
workflow_stage: "Execution Tracking"
sequence_order: 50
kanban_lane: "In Progress"
plan_start: 2026-02-19
plan_end: 2026-03-07
progress_pct: 40
status_now: "추적 체계는 동작 중이며 로그 스키마 정합성 관리가 핵심"
major_issues:
  - "프로젝트별 로그 필드 불일치가 간헐적으로 발생"
  - "이벤트 누락 시 사후 복구 비용이 큼"
next_actions:
  - "공통 로그 스키마 v1 고정"
  - "누락 감지 규칙 추가"
last_review: 2026-03-03
relationship_tags:
  - same-domain
  - cross-domain
relations:
  - target: "[[workspace-links/_catalog/cards/MSW-VampireSurvivors]]"
    kind: execution-tracking
    direction: in
    strength: high
    reason: "개발 실행 로그 수신"
  - target: "[[workspace-links/_catalog/cards/OpenClaw]]"
    kind: telemetry-source
    direction: out
    strength: high
    reason: "운영 대시보드에 텔레메트리 제공"
  - target: "[[workspace-links/_catalog/cards/Antigravity-Brain]]"
    kind: research-feedback
    direction: out
    strength: medium
    reason: "리서치 개선용 피드백 전달"
---

# Antigravity-CodeTracker

## 목적
- 실행/변경 데이터를 안정적으로 추적해 운영 판단을 지원합니다.

## 분류 근거
- `domain`: agent-ops
- `artifact_type`: ops-logs + automation
- `execution_mode`: operate

## 연관 프로젝트
- [[workspace-links/_catalog/cards/MSW-VampireSurvivors]] - execution-tracking
- [[workspace-links/_catalog/cards/OpenClaw]] - telemetry-source
- [[workspace-links/_catalog/cards/Antigravity-Brain]] - research-feedback

## 현황
- 추적 파이프라인은 운영 중이며 정합성 강화를 진행 중입니다.

## 문제
- 로그 스키마가 흔들리면 분석 연속성이 깨집니다.

## 다음 할 일
- 누락 감지와 스키마 고정을 우선 적용합니다.

<!-- AUTO_INTEL:START -->
## 자동 인텔리전스
- 마지막 업데이트: 2026-03-03 00:06 UTC
- 수집 범위: 최근 30일
- 수집 건수: 10건
- 리포트: [[workspace-links/_catalog/updates/Antigravity-CodeTracker/2026-03-03]]

### 핵심 시그널
- [v1.53.0/v0.147.0](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.147.0) (GitHubFeed: https://github.com/open-telemetry/opentelemetry-collector/releases.atom, 2026-03-02)
- [service/v0.147.0](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/service%2Fv0.147.0) (GitHubFeed: https://github.com/open-telemetry/opentelemetry-collector/releases.atom, 2026-03-02)
- [service/telemetry/telemetrytest/v0.147.0](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/service%2Ftelemetry%2Ftelemetrytest%2Fv0.147.0) (GitHubFeed: https://github.com/open-telemetry/opentelemetry-collector/releases.atom, 2026-03-02)
<!-- AUTO_INTEL:END -->

<!-- CHATGPT_EXPORT_MERGE:d255689f61d1 -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Antigravity-CodeTracker/2026-03-03_FreeFlow_GitHub_Overview_69a277a3-18a4-83a8-8334-3d057c51c507|FreeFlow GitHub Overview]]
- 토픽: `Antigravity-CodeTracker`
- conversation_id: `69a277a3-18a4-83a8-8334-3d057c51c507`
- 유사도: `0.251`

### 요약
https://github.com/zachlatta/freeflow

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:d255689f61d1 -->

<!-- CHATGPT_EXPORT_MERGE:a10c7581083a -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Antigravity-CodeTracker/2026-03-03_Google_Grounding_Snippets_Extraction_69a276ae-e1d0-83a2-a35a-1eb9bcebea3c|Google Grounding Snippets Extraction]]
- 토픽: `Antigravity-CodeTracker`
- conversation_id: `69a276ae-e1d0-83a2-a35a-1eb9bcebea3c`
- 유사도: `0.228`

### 요약
https://dejan.ai/blog/what-extraction-method-is-google-using-to-build-grounding-snippets/

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:a10c7581083a -->

<!-- CHATGPT_EXPORT_MERGE:4a2db1863dba -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Antigravity-CodeTracker/2026-03-03_Link_sharing_6993a734-5540-83a5-858c-dbcf09104569|Link sharing]]
- 토픽: `Antigravity-CodeTracker`
- conversation_id: `6993a734-5540-83a5-858c-dbcf09104569`
- 유사도: `0.157`

### 요약
https://lilys.ai/digest/8177565/9127895?s=1&noteVersionId=5583039&fbclid=IwdGRzaAQAhlNjbGNrBACGQmV4dG4DYWVtAjExAHNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABHm5i_ZUMIeHAkvFFI3IbE9olHW7dQ5tgGcEHDSfQLaxBi_X1tATT4JmDzO7b_aem_CwN09lAAtWtiz2mS078a6Q&sfnsn=mo

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:4a2db1863dba -->

<!-- CHATGPT_EXPORT_MERGE:7503dd970cab -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Antigravity-CodeTracker/2026-03-03_원리를_생각하는_프롬프팅_69973cc3-1f68-83a9-a5f4-d1517de576d3|원리를 생각하는 프롬프팅]]
- 토픽: `Antigravity-CodeTracker`
- conversation_id: `69973cc3-1f68-83a9-a5f4-d1517de576d3`
- 유사도: `0.162`

### 요약
(summary missing)

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:7503dd970cab -->

<!-- CHATGPT_EXPORT_MERGE:524781403b33 -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Antigravity-CodeTracker/2026-03-03_코덱스_사용법_안내_699efa87-9f30-83a7-bec3-bd1de5cc78ed|코덱스 사용법 안내]]
- 토픽: `Antigravity-CodeTracker`
- conversation_id: `699efa87-9f30-83a7-bec3-bd1de5cc78ed`
- 유사도: `0.131`

### 요약
코덱스 잘쓰는법

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:524781403b33 -->
