---
type: project-card
project_name: "Antigravity-Brain"
display_name: "에이전트 브레인 R&D 허브"
entry_link: "[[workspace-links/antigravity/brain]]"
domain: knowledge-rnd
artifact_type:
  - research-notes
  - design-doc
execution_mode: research
phase: active
review_cycle: daily
priority: p1
risk_level: medium
workflow_stage: "Research & Decision"
sequence_order: 10
kanban_lane: "In Progress"
plan_start: 2026-02-12
plan_end: 2026-02-23
progress_pct: 65
status_now: "문서 보강은 진행 중이며, 실행 프로젝트로 연결되는 의사결정 정리가 필요함"
major_issues:
  - "리서치 내용은 많지만 실행 우선순위 매핑이 약함"
  - "검증 백로그 갱신 주기가 일정하지 않음"
next_actions:
  - "핵심 3개 주제에 대해 의사결정 템플릿 적용"
  - "MSW/OpenClaw 연계 액션 항목을 카드별로 분리"
last_review: 2026-03-03
relationship_tags:
  - cross-domain
relations:
  - target: "[[workspace-links/_catalog/cards/Copilot-Prompts]]"
    kind: prompt-source
    direction: out
    strength: high
    reason: "리서치 결과를 프롬프트 자산으로 변환"
  - target: "[[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro]]"
    kind: research-input
    direction: out
    strength: medium
    reason: "실험 가설/우선순위 입력"
  - target: "[[workspace-links/_catalog/cards/MSW-VampireSurvivors]]"
    kind: decision-source
    direction: out
    strength: high
    reason: "본편 구현 우선순위 근거 제공"
  - target: "[[workspace-links/_catalog/cards/OpenClaw]]"
    kind: knowledge-sync
    direction: bi
    strength: medium
    reason: "운영 리듬과 리서치 출력 동기화"
---

# Antigravity-Brain

## 목적
- 리서치 자산을 실행 가능한 의사결정으로 변환합니다.

## 분류 근거
- `domain`: knowledge-rnd
- `artifact_type`: research-notes + design-doc
- `execution_mode`: research

## 연관 프로젝트
- [[workspace-links/_catalog/cards/Copilot-Prompts]] - prompt-source
- [[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro]] - research-input
- [[workspace-links/_catalog/cards/MSW-VampireSurvivors]] - decision-source
- [[workspace-links/_catalog/cards/OpenClaw]] - knowledge-sync

## 현황
- 문서 기반 인사이트는 충분하며, 실행 연결을 강화하는 단계입니다.

## 문제
- 실행 우선순위로 압축되지 않은 항목이 누적되고 있습니다.

## 다음 할 일
- 카드별 의사결정 체크리스트를 만들어 프로젝트별로 바로 전달합니다.

<!-- AUTO_INTEL:START -->
## 자동 인텔리전스
- 마지막 업데이트: 2026-03-03 00:06 UTC
- 수집 범위: 최근 30일
- 수집 건수: 10건
- 리포트: [[workspace-links/_catalog/updates/Antigravity-Brain/2026-03-03]]

### 핵심 시그널
- [코딩 에이전트 실패 이유로 지나치게 상세한 ‘AGENTS.md’ 파일 지목 - AI타임스](https://news.google.com/rss/articles/CBMiakFVX3lxTE9nX3VCLVF6ODE1S05zSldwaE4yRVMycy1BR0ktZGJROXE4bUFoUjVCUGxwQTJIOEE4eExVYmdCM1kxcU5iS3ZrZzdiME1RNDFUUWpRQmJmZks4aEg4Q2RrQ1ZvTzdHMF9kN3c?oc=5) (GoogleNews: AI coding agent benchmark, 2026-02-27)
- [BTC 뉴스: AI 에이전트 OpenClaw의 디스코드에서 '비트코인' 언급 시 BAN 처리 - CoinDesk](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNMmZTc1B6WHA2ZXBESmhsWW9FdDVncUlPNlBVa29NYzNHbWRmX3oxRlprTlhCaUlrUktLU1p1X0kwSWpyMjhVWG9sT0QwVEZpNVltaVBnNTBsa2JBMjFHSFNYRmk4aWRDeTQ2ajZnSXIwQ3dtckUxQ29QVm52YlNrLTA2YkUxWjRLMHlpN2VDT1FQTGp2dXdUY3A2WGNVMVhCc3A2TDFJUHJSSEctTExRb21mVmYybHl4RTVlSGRMaU8?oc=5) (GoogleNews: AI coding agent benchmark, 2026-02-21)
- [구글의 시간 돌아왔다… 압도적 성능 ‘제미나이 3.1 프로’ 에이전트 혁명 - 더밀크](https://news.google.com/rss/articles/CBMiUEFVX3lxTE5sVlJnMGd2MEJlMXJHb2pXUVpiV3ptNmhJZy0zWVlBVlJSSmJMV2EyaUViQWJMcUtIc1hEZHlGZmxsS3lsOFNubXBwV2ljTk9u?oc=5) (GoogleNews: AI coding agent benchmark, 2026-02-19)
<!-- AUTO_INTEL:END -->

<!-- CHATGPT_EXPORT_MERGE:205b9a1918ee -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Antigravity-Brain/2026-03-03_Accomplish_AI_Overview_69973373-6ef4-83a3-8b1d-e4d71cd84b7e|Accomplish AI Overview]]
- 토픽: `Antigravity-Brain`
- conversation_id: `69973373-6ef4-83a3-8b1d-e4d71cd84b7e`
- 유사도: `0.230`

### 요약
https://accomplish.ai/?fbclid=IwdGRzaAQEErhjbGNrBAQSpWV4dG4DYWVtAjExAHNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABHqtfhxpZLTVBopDqeD5w4wMmrNcFWismBTR_QN1nLdesBTAEBKMb2asJ1paH_aem_xN5-Al8Y5-AMHgDlAWs8vg&sfnsn=mo

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:205b9a1918ee -->

<!-- CHATGPT_EXPORT_MERGE:58996739f8ba -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Antigravity-Brain/2026-03-03_DroidClaw_GitHub_Overview_6996b0c2-5f80-83a7-88e6-97cdd1d3febe|DroidClaw GitHub Overview]]
- 토픽: `Antigravity-Brain`
- conversation_id: `6996b0c2-5f80-83a7-88e6-97cdd1d3febe`
- 유사도: `0.185`

### 요약
https://github.com/unitedbyai/droidclaw?fbclid=IwdGRzaAQDkAdjbGNrBAOP82V4dG4DYWVtAjExAHNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABHp5yb2ghkFNlm4p5UMDOerRHrEHjD5Irypis_yZLDyrpO4M6t9DlyILWpHzY_aem_LYmZEvpfSPhXRNUu53ttzQ&sfnsn=mo

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:58996739f8ba -->

<!-- CHATGPT_EXPORT_MERGE:aabe3521af4b -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Antigravity-Brain/2026-03-03_zclaw_AI_Assistant_69a2772a-6cbc-83ab-a616-51645d1b8fee|zclaw AI Assistant]]
- 토픽: `Antigravity-Brain`
- conversation_id: `69a2772a-6cbc-83ab-a616-51645d1b8fee`
- 유사도: `0.349`

### 요약
https://github.com/tnm/zclaw

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:aabe3521af4b -->

<!-- CHATGPT_EXPORT_MERGE:e366807b2eb2 -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Antigravity-Brain/2026-03-03_지피티_프로_띵낑_차이_6992b1f4-7f6c-83a3-9ec9-6678f2b92b08|지피티 프로 띵낑 차이]]
- 토픽: `Antigravity-Brain`
- conversation_id: `6992b1f4-7f6c-83a3-9ec9-6678f2b92b08`
- 유사도: `0.192`

### 요약
지피티 프로와 띵낑의 차이

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:e366807b2eb2 -->
