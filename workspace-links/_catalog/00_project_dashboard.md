# 프로젝트 분류 대시보드

## 분류 매트릭스
| Project | Domain | Mode | Phase | Priority | Card |
|---|---|---|---|---|---|
| [[workspace-links/projects/MSW-VampireSurvivors|MSW 본편 개발]] | game-dev | build | active | p1 | [[workspace-links/_catalog/cards/MSW-VampireSurvivors]] |
| [[workspace-links/projects/MSW-VampireSurvivors-Pro|MSW 실험 트랙]] | game-dev | build | incubation | p2 | [[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro]] |
| [[workspace-links/projects/Gameplay-OCR-ComputerUse-QA|게임플레이 OCR 제어 QA]] | game-dev | build | incubation | p1 | [[workspace-links/_catalog/cards/Gameplay-OCR-ComputerUse-QA]] |
| [[workspace-links/antigravity/brain|에이전트 브레인 R&D 허브]] | knowledge-rnd | research | active | p1 | [[workspace-links/_catalog/cards/Antigravity-Brain]] |
| [[workspace-links/antigravity/code_tracker|실행 로그·코드 추적 허브]] | agent-ops | operate | active | p1 | [[workspace-links/_catalog/cards/Antigravity-CodeTracker]] |
| [[OpenClaw|OpenClaw 운영 허브]] | agent-ops | operate | active | p1 | [[workspace-links/_catalog/cards/OpenClaw]] |
| [[copilot|코파일럿 프롬프트 라이브러리]] | prompt-ops | research | active | p2 | [[workspace-links/_catalog/cards/Copilot-Prompts]] |

## 실행 보드
- [[workspace-links/_catalog/04_execution_overview]]
- [[workspace-links/_catalog/05_kanban_execution]]
- [[workspace-links/_catalog/03_relationship_dashboard]]

```dataview
TABLE
  sequence_order AS Seq,
  choice(display_name, display_name, file.link) AS Project,
  workflow_stage AS Stage,
  kanban_lane AS Lane,
  plan_start AS Start,
  plan_end AS End,
  progress_pct AS Progress,
  status_now AS CurrentStatus,
  major_issues AS TopIssues,
  next_actions AS NextActions,
  risk_level AS Risk
FROM "workspace-links/_catalog/cards"
WHERE type = "project-card"
SORT sequence_order ASC, priority ASC
```

## 운영 규칙
1. `status_now`, `major_issues`, `next_actions`는 매 리뷰 주기마다 갱신합니다.
2. `sequence_order`는 실행 흐름 기준으로만 관리합니다.
3. `relations`가 비어 있으면 분류 누락으로 간주합니다.

## 인텔리전스
- [[workspace-links/_catalog/06_intelligence_updates]]
- [[workspace-links/_catalog/automation/README]]

## 이름 규칙
- [[workspace-links/_catalog/07_naming_convention]]
- [[workspace-links/project-shortcuts/README]]
