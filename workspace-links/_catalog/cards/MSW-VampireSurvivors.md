---
type: project-card
project_name: "MSW-VampireSurvivors"
display_name: "MSW 본편 개발"
entry_link: "[[workspace-links/projects/MSW-VampireSurvivors]]"
domain: game-dev
artifact_type:
  - codebase
  - automation
execution_mode: build
phase: active
review_cycle: daily
priority: p1
risk_level: high
workflow_stage: "Core Build"
sequence_order: 40
kanban_lane: "In Progress"
plan_start: 2026-02-17
plan_end: 2026-03-12
progress_pct: 50
status_now: "핵심 게임 로직과 자동화 스크립트는 동작하지만 안정화가 최우선"
major_issues:
  - "Maker UI 변화에 자동화 내구성이 약함"
  - "컴포넌트/로직 변경 시 회귀 점검 루틴이 부족함"
next_actions:
  - "핵심 시나리오 회귀 체크리스트 고정"
  - "실험 트랙 반영 후보를 주간 1회만 병합"
last_review: 2026-03-03
relationship_tags:
  - same-domain
  - cross-domain
relations:
  - target: "[[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro]]"
    kind: experiment-branch
    direction: bi
    strength: high
    reason: "본편-실험 상호 보완"
  - target: "[[workspace-links/_catalog/cards/Antigravity-Brain]]"
    kind: decision-source
    direction: in
    strength: high
    reason: "우선순위/설계 근거 수신"
  - target: "[[workspace-links/_catalog/cards/Copilot-Prompts]]"
    kind: build-support
    direction: in
    strength: medium
    reason: "개발 작업 프롬프트 수신"
  - target: "[[workspace-links/_catalog/cards/Antigravity-CodeTracker]]"
    kind: execution-tracking
    direction: out
    strength: high
    reason: "실행 로그와 변경 이력 전달"
  - target: "[[workspace-links/_catalog/cards/OpenClaw]]"
    kind: project-ops
    direction: bi
    strength: medium
    reason: "운영 계획과 실행 동기화"
---

# MSW-VampireSurvivors

## 목적
- 플레이 가능한 본편 게임 빌드를 안정적으로 고도화합니다.

## 분류 근거
- `domain`: game-dev
- `artifact_type`: codebase + automation
- `execution_mode`: build

## 연관 프로젝트
- [[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro]] - experiment-branch
- [[workspace-links/_catalog/cards/Antigravity-Brain]] - decision-source
- [[workspace-links/_catalog/cards/Copilot-Prompts]] - build-support
- [[workspace-links/_catalog/cards/Antigravity-CodeTracker]] - execution-tracking
- [[workspace-links/_catalog/cards/OpenClaw]] - project-ops

## 현황
- 실행은 가능하며, 안정성/회귀 관리 개선이 필요합니다.

## 문제
- 자동화 내구성과 회귀 점검 체계가 병목입니다.

## 다음 할 일
- 회귀 루틴을 명문화해 일일 점검 항목으로 고정합니다.

<!-- AUTO_INTEL:START -->
## 자동 인텔리전스
- 마지막 업데이트: 2026-03-03 00:06 UTC
- 수집 범위: 최근 30일
- 수집 건수: 7건
- 리포트: [[workspace-links/_catalog/updates/MSW-VampireSurvivors/2026-03-03]]

### 핵심 시그널
- [MapleStory N, 5월 15일 Avalanche L1에서 서비스 시작 - games.gg](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNX2tkNlk2MFc3UXktWVdvM2xfTWdDZS1USUpLc2VlUkRnYkhXS1hIX1V6MV9JOUdFV0p2TUI2bzRTTjA4WW9jbHp4YzA5U0hTSVFIVm5JcjhjeEtaa0poUFlkVkhueHBtWWpDWmVFak00eXRGbDFNWDFYaWVqN0YxNVk2RzdjSGRZU2s0M3VDMDFaZm5aSzVCaVFLbEludTlSUHQ3VnpmV0xQOWtTVkxQN0RjYkFBcURYWnJOTUg2bFMwenBkYmVlZ085Q0NqbmJhV2wzMjRR?oc=5) (GoogleNews: MapleStory Worlds update, 2026-02-13)
- [MapleStory N, 오리지널과 차별화된 독점 콘텐츠 제공 - games.gg](https://news.google.com/rss/articles/CBMipAJBVV95cUxPYy1laGtLMmkzbHF4TkE5b09SYl9vMVE3eEJFbUZIVEx4R19LUTRUUTFzaEpzWUMtc1U5VFd6N3h2V3NadXpoT1RGcUx0SUVZTjdSbnNRMktZVHp4S1VBemJJNkY1YlNWd3NSUlFUWElqeVhnT2cyVDRKRE43Q2swcko5dkdNMlNiMDFWUmttUTFtVEc3Z2NjVlN4RDNVSlVRcGp6bUJvUVRCalBCaFhSMXdrOExPZkRxZ3drbEt3RVA0Vi1ZZDMxRDQ3ZXRKMVVqRnNBTWN4R2JUeG42TTNqUlBmazQxQklpV1BLMmlSTkFuWjdrWnVDaVA4TUduRk9pTHcxdThtMFJPZ2tCWFFyZUExRnlrTEMyNWxqd19QNjZOeU8z?oc=5) (GoogleNews: MapleStory Worlds update, 2026-02-05)
- [넥슨, MapleStory Universe Web3 IP에 1억 달러 투자 - games.gg](https://news.google.com/rss/articles/CBMiygFBVV95cUxON2xWeU1EeG4zUE5SbFpHaVlaR2twR2VlX1FVOGxwd0F3VkVsYWdrRHdOVjc2a1ZKVGNlS0s0YmV2OFF1bnVjbmp3OWgxeUpNVVB2WURHSFVHUnZQaDVOMzg0cXFOZVlwd3FJUVI0VFNhcXpuWUFFb2pXWnk5UHB5NUR4YUNFYVFSSzZHVWN4LWNieUQzOXNieFVoRDk4VEd0LUZzaF9aM0F5WlExRTh6VzBIazJkMm50cjd1bFd4X3FjVE1Sb2FIVFBR?oc=5) (GoogleNews: MapleStory Worlds update, 2026-02-05)
<!-- AUTO_INTEL:END -->

<!-- CHATGPT_EXPORT_MERGE:cb7586bc52ab -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/MSW-VampireSurvivors/2026-03-03_Clawdbot_Name_Controversy_69a2765d-10f4-83ab-a6f2-461240415c55|Clawdbot Name Controversy]]
- 토픽: `MSW-VampireSurvivors`
- conversation_id: `69a2765d-10f4-83ab-a6f2-461240415c55`
- 유사도: `0.258`

### 요약
https://trond.ai/p/clawdbot-was-rad-until-google-killed

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:cb7586bc52ab -->

<!-- CHATGPT_EXPORT_MERGE:29ab4cff1633 -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/MSW-VampireSurvivors/2026-03-03_Z390_M.2_SATA_지원_69a11328-3064-83a4-a29b-e9862034f052|Z390 M.2 SATA 지원]]
- 토픽: `MSW-VampireSurvivors`
- conversation_id: `69a11328-3064-83a4-a29b-e9862034f052`
- 유사도: `0.134`

### 요약
z390은 m2만 돼?

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:29ab4cff1633 -->
