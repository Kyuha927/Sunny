---
type: project-card
project_name: "Gameplay-OCR-ComputerUse-QA"
display_name: "게임플레이 OCR 제어 QA"
entry_link: "[[workspace-links/projects/Gameplay-OCR-ComputerUse-QA]]"
domain: game-dev
artifact_type:
  - codebase
  - automation
  - design-doc
execution_mode: build
phase: incubation
review_cycle: daily
priority: p1
risk_level: high
workflow_stage: "Gameplay QA Automation"
sequence_order: 35
kanban_lane: "This Week"
plan_start: 2026-02-18
plan_end: 2026-03-10
progress_pct: 8
status_now: "OCR+입력 제어 기반 테스트 툴 기획 완료, MVP 구현 시작 단계"
major_issues:
  - "OCR 오탐/미탐으로 시나리오 판정이 불안정할 수 있음"
  - "해상도/UI 스킨 변화에 따라 좌표/ROI 유지보수 비용이 큼"
next_actions:
  - "MVP 시나리오 1개(메인->인게임->결과) 실행기 구현"
  - "Lead GPT와 교환 패킷 규격으로 첫 스프린트 핸드오프"
last_review: 2026-03-03
relationship_tags:
  - same-domain
  - cross-domain
relations:
  - target: "[[workspace-links/_catalog/cards/MSW-VampireSurvivors]]"
    kind: build-support
    direction: out
    strength: high
    reason: "본편 플레이 회귀 시나리오 자동 점검 지원"
  - target: "[[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro]]"
    kind: research-input
    direction: in
    strength: medium
    reason: "실험 트랙 시나리오를 테스트 케이스로 수신"
  - target: "[[workspace-links/_catalog/cards/Antigravity-Brain]]"
    kind: decision-source
    direction: in
    strength: medium
    reason: "OCR/제어 전략 및 우선순위 근거 수신"
  - target: "[[workspace-links/_catalog/cards/Antigravity-CodeTracker]]"
    kind: execution-tracking
    direction: out
    strength: medium
    reason: "실행 결과/실패 로그 전달"
  - target: "[[workspace-links/_catalog/cards/OpenClaw]]"
    kind: project-ops
    direction: bi
    strength: medium
    reason: "운영 룰/핸드오프 동기화"
---

# Gameplay-OCR-ComputerUse-QA

## 목적
- OCR + 마우스/키보드 제어를 통해 게임 플레이 회귀 점검을 자동화합니다.

## 분류 근거
- `domain`: game-dev
- `artifact_type`: codebase + automation + design-doc
- `execution_mode`: build

## 연관 프로젝트
- [[workspace-links/_catalog/cards/MSW-VampireSurvivors]] - build-support
- [[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro]] - research-input
- [[workspace-links/_catalog/cards/Antigravity-Brain]] - decision-source
- [[workspace-links/_catalog/cards/Antigravity-CodeTracker]] - execution-tracking
- [[workspace-links/_catalog/cards/OpenClaw]] - project-ops

## 현황
- 문서/협업 규약은 준비되었고, 코드 MVP 시작 전 단계입니다.

## 문제
- OCR 정확도와 UI 변화 대응 비용이 핵심 리스크입니다.

## 다음 할 일
- 시나리오 실행기 MVP 구현 후 첫 자동 리포트를 산출합니다.

<!-- AUTO_INTEL:START -->
## 자동 인텔리전스
- 마지막 업데이트: 2026-03-03 00:06 UTC
- 수집 범위: 최근 30일
- 수집 건수: 10건
- 리포트: [[workspace-links/_catalog/updates/Gameplay-OCR-ComputerUse-QA/2026-03-03]]

### 핵심 시그널
- [앤트로픽, 실행형 AI의 정점 ‘클로드 소네트 4.6’ 전격 공개… "코딩·컴퓨터 조작·비즈니스 추론까지 압도적 진화" - 인공지능신문](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5xdnFVU3Q2OGU0eHh0a0RHZ3dtWTB5UERJVldKSHFFVHhlUUhxWlN6S0d2cklyYTRkU0ZLdFItSi1oelBDc2h3ZFpRbC1ST0RlSU15ZG5qVmdaOG9MUnRieGROQVNoMFU?oc=5) (GoogleNews: computer use ai automation, 2026-02-18)
- [[AW 2026 프리뷰] 젝스컴퍼니, 'AI 추론·영상 분석 최적화' 고성능 팬리스 엣지 PC 선보인다 - 헬로티](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAyYVZZSDRqcWRYbWwxeW5wdlFPU3UySmhaeF9Sd2ZhUV9udUt5bE9EazUtWnVOSjJLWXlhaG1LcmNBbFZ4OGJzSy1TUUFoSTdCUnpZVV9aOGxCR291aUFr?oc=5) (GoogleNews: computer use ai automation, 2026-02-11)
- ['제2의 자비스' 물거품…네카당이 금지한 오픈클로, 어떻길래 - 지디넷코리아](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5QeWR4eV9jM2tIN2x6YWY3OEVMc3F0RU1HNm5MLUczcWRjRHFPVjZreE5RVXJHLThOMU91dGw0Mk05RERNelFrWWF4U3RIYWZ1RlZTUWlB?oc=5) (GoogleNews: computer use ai automation, 2026-02-09)
<!-- AUTO_INTEL:END -->

<!-- CHATGPT_EXPORT_MERGE:b11c82486db7 -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Antigravity-CodeTracker/2026-03-03_NexPhone_3-in-1_스마트폰_69a296e2-6c24-83ab-ad8f-e541171563cf|NexPhone 3-in-1 스마트폰]]
- 토픽: `Antigravity-CodeTracker`
- conversation_id: `69a296e2-6c24-83ab-ad8f-e541171563cf`
- 유사도: `0.135`

### 요약
리눅스·윈도11 실행하는 안드로이드폰 나온다 - 지디넷코리아 https://share.google/H3x4ebbYnAJHGDYFz

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:b11c82486db7 -->

<!-- CHATGPT_EXPORT_MERGE:9b9b0d14acd2 -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Copilot-Prompts/2026-03-03_마이크로GPT_핵심_구현_69954bc4-64f8-83a8-8907-35d2b24c555c|마이크로GPT 핵심 구현]]
- 토픽: `Copilot-Prompts`
- conversation_id: `69954bc4-64f8-83a8-8907-35d2b24c555c`
- 유사도: `0.244`

### 요약
카르파시,파이썬 200줄로 GPT 핵심 구현한 ‘마이크로GPT’ 공개 < 산업일반 < AI산업 < 기사본문 - AI타임스 https://share.google/0TXaBEILWNjBFVq0S

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:9b9b0d14acd2 -->

<!-- CHATGPT_EXPORT_MERGE:4a8f6ac22f4d -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Gameplay-OCR-ComputerUse-QA/2026-03-03_Tesseract_EasyOCR_OpenCV_기반_한국어_OCR_파이프라인_6995e870-eafc-83a6-ab22-d89ad9e2b447|Tesseract + EasyOCR + OpenCV 기반 한국어 OCR 파이프라인]]
- 토픽: `Gameplay-OCR-ComputerUse-QA`
- conversation_id: `6995e870-eafc-83a6-ab22-d89ad9e2b447`
- 유사도: `0.280`

### 요약
(summary missing)

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:4a8f6ac22f4d -->

<!-- CHATGPT_EXPORT_MERGE:a200431a8750 -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Gameplay-OCR-ComputerUse-QA/2026-03-03_라즈베리파이_활용법_69a09505-1cc4-83a9-8bfa-4ea309d9500a|라즈베리파이 활용법]]
- 토픽: `Gameplay-OCR-ComputerUse-QA`
- conversation_id: `69a09505-1cc4-83a9-8bfa-4ea309d9500a`
- 유사도: `0.214`

### 요약
라즈베리파이

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:a200431a8750 -->
