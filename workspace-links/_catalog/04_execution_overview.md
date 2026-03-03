# 실행 현황 한눈 보드

- 칸반 보드: [[workspace-links/_catalog/05_kanban_execution]]

## 프로젝트 순서도
```mermaid
flowchart LR
  A[Antigravity-Brain<br/>Research & Decision]
  B[Copilot-Prompts<br/>Prompt Asset]
  C[MSW-VampireSurvivors-Pro<br/>Experiment]
  G[Gameplay-OCR-ComputerUse-QA<br/>Gameplay QA Automation]
  D[MSW-VampireSurvivors<br/>Core Build]
  E[Antigravity-CodeTracker<br/>Execution Tracking]
  F[OpenClaw<br/>Ops Control]

  A --> B --> C --> G --> D --> E --> F
  F --> A
  C --> D
  C --> G
  G --> D
  B --> D
```

## 로드맵 간트차트
```mermaid
gantt
  title 프로젝트 실행 로드맵 (2026-02-18 기준)
  dateFormat YYYY-MM-DD
  axisFormat %m/%d

  section Research
  Antigravity-Brain        :brain, 2026-02-12, 2026-02-23
  Copilot-Prompts          :copilot, 2026-02-18, 2026-02-28

  section Build
  MSW-VampireSurvivors-Pro :mpro, 2026-02-20, 2026-03-03
  Gameplay-OCR-ComputerUse-QA :gqa, 2026-02-18, 2026-03-10
  MSW-VampireSurvivors     :crit, mcore, 2026-02-17, 2026-03-12

  section Ops
  Antigravity-CodeTracker  :track, 2026-02-19, 2026-03-07
  OpenClaw                 :ops, 2026-02-18, 2026-03-14
```

## 전체 현황
```dataview
TABLE
  sequence_order AS Seq,
  choice(display_name, display_name, file.link) AS Project,
  workflow_stage AS Stage,
  plan_start AS Start,
  plan_end AS End,
  progress_pct AS Progress,
  domain AS Domain,
  phase AS Phase,
  priority AS Priority,
  risk_level AS Risk,
  status_now AS CurrentStatus
FROM "workspace-links/_catalog/cards"
WHERE type = "project-card"
SORT sequence_order ASC
```

## 진행률 한눈 보기
```dataviewjs
const cards = dv.pages('"workspace-links/_catalog/cards"')
  .where(p => p.type === "project-card")
  .sort(p => p.sequence_order, 'asc');

const bar = (p) => {
  const pct = Number(p.progress_pct ?? 0);
  const clamped = Math.max(0, Math.min(100, pct));
  const filled = Math.round(clamped / 10);
  return "█".repeat(filled) + "░".repeat(10 - filled) + ` ${clamped}%`;
};

const rows = cards.map(p => [
  p.sequence_order,
  p.display_name ?? p.file.link,
  p.plan_start ?? "",
  p.plan_end ?? "",
  bar(p),
  p.risk_level ?? ""
]);

dv.table(["Seq", "Project", "Start", "End", "ProgressBar", "Risk"], rows);
```

## 문제 / 다음 할 일
```dataview
TABLE
  choice(display_name, display_name, file.link) AS Project,
  major_issues AS TopIssues,
  next_actions AS NextActions,
  last_review AS LastReview
FROM "workspace-links/_catalog/cards"
WHERE type = "project-card"
SORT sequence_order ASC
```

## 즉시 체크 (오늘)
```dataviewjs
const cards = dv.pages('"workspace-links/_catalog/cards"')
  .where(p => p.type === "project-card")
  .sort(p => p.sequence_order, 'asc');

const rows = cards.map(p => {
  const issue = (p.major_issues ?? [])[0] ?? "";
  const next = (p.next_actions ?? [])[0] ?? "";
  return [p.sequence_order, (p.display_name ?? p.file.link), issue, next, p.risk_level ?? ""];
});

dv.table(["Seq", "Project", "Today Issue", "Today Next", "Risk"], rows);
```
