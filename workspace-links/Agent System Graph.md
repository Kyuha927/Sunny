---
type: concept
tags:
  - concept
  - workspace-links
created: 2026-03-25
summary: "Agent System Graph"
tags::
  - workspace-links
---
# Agent System Graph

이 노트는 에이전트 시스템의 관계를 한 번에 보는 지도다.

```mermaid
flowchart LR
  subgraph Vault["Obsidian Vault"]
    W["workspace-links/Agent System Quick Guide"]
    G["workspace-links/Agent System Graph"]
    MOC["workspace-links/Agent MOC"]
    P["workspace-links/Projects"]
    Rf["workspace-links/References"]
    N["workspace-links/Agent Notes"]
    L["workspace-links/Daily Logs Index"]
    Wk["workspace-links/Weekly Review Index"]
    Ps["workspace-links/Project Status Index"]
    AIdx["workspace-links/Archive Index"]
    Pn["workspace-links/Obsidian Plugins"]
    A["workspace-links/Archive"]
  end

  subgraph Docs["SSOT and Index"]
    R["msw2/Docs/Rules.md"]
    I["msw2/Docs/Interfaces.md"]
    M["msw2/Docs/MCP_ToolMap.md"]
    S["msw2/Docs/AgentSharedReference.md"]
    C["msw2/Docs/AgentContextIndex.json"]
    Q["msw2/Docs/OpenQuestions.md"]
  end

  subgraph Runtime["Execution Layer"]
    B["antigravity_bridge/bin/ag-session"]
    X["antigravity_bridge/sessions/*"]
  end

  subgraph Memory["Memory Layer"]
    AB["antigravity_brains/*"]
    T["Agent-Stall-Recovery"]
    D["Discord-Bot-Fold1"]
  end

  W --> MOC
  W --> S
  W --> R
  W --> I
  W --> M
  W --> C
  W --> Q
  MOC --> P
  MOC --> Rf
  MOC --> N
  MOC --> L
  MOC --> Wk
  MOC --> Ps
  MOC --> AIdx
  MOC --> Pn
  MOC --> A
  P --> MOC
  Rf --> MOC
  N --> L
  N --> Wk
  N --> Ps
  N --> AIdx
  N --> Pn
  AIdx --> A

  S --> R
  S --> I
  S --> M

  B --> X
  X --> AB
  AB --> T
  AB --> D

  R --> B
  I --> B
  M --> B
  Q --> M
```

## 해석

- `Docs/`는 행동 기준이다.
- `antigravity_bridge`는 단발 실행을 고정한다.
- `antigravity_brains`는 누적된 기억과 복구력을 만든다.
- `workspace-links`는 이 모든 것을 Obsidian에서 빠르게 재진입하기 위한 진입점이다.
- 템플릿은 반복 작업의 형식을 고정한다.
- 주간 회고와 프로젝트 상태는 현재를 유지하는 운영 노트다.

## 실전 메모

- 새 작업을 시작하면 Quick Guide부터 연다.
- 길게 남길 내용은 Graph 노트에 따라 어디에 저장할지 결정한다.
- 일회성 결과는 브리지 세션에, 장기 판단은 브레인에 남긴다.
- 오늘 기록은 `Daily Logs/2026/2026-03-20.md`에 남겼다.