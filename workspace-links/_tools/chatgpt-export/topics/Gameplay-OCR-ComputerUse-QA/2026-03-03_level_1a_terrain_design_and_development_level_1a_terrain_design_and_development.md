---
type: chatgpt-export-conversation
topic: "Gameplay-OCR-ComputerUse-QA"
title: "level_1a_terrain_design_and_development"
conversation_id: "level_1a_terrain_design_and_development"
imported_at_utc: "2026-03-03T05:29:26+00:00"
turn_count: 0
chars: 2315
topic_score: 2
---

# level_1a_terrain_design_and_development

- topic: `Gameplay-OCR-ComputerUse-QA`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::file-RJMhcHYP8ZGgCZNikcPS8D-LevelEditorTool.zip::level_1a_terrain_design_and_development.md`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/level_1a_terrain_design_and_development.txt`
- conversation_id: `level_1a_terrain_design_and_development`
- matched_keywords: 제어, use
- card: [[workspace-links/_catalog/cards/Gameplay-OCR-ComputerUse-QA|게임플레이 OCR 제어 QA]]

## Summary
# Stage 1-A 지형 설계 및 개발 기록 작성일: 2026-02-25 ## 1. 목적 - 스테이지 1-A를 빠르게 반복 제작/수정할 수 있게 화이트박스 지형 생성 자동화. - 디자이너가 인스펙터 수치만 조절해 난이도(경사, 간격, 낙차, 비거리)를 즉시 튜닝. - 씬 뷰 클릭 기반 배치(Shift+클릭)로 레벨 조립 속도 향상. ## 2. 설계 의도 Stage 1-A는 학습형 곡선으로 설계됨. - A-1: 기본 경사 적응 구간 - 20도 내리막(기본값)으로 관성/속도 체감. - A-2: 점프대 + 착지 구간 - 경사 끝에서 램프 진입, 갭을 넘어 착지. - 램프 각도/길이, 갭, 착지 높이 차를 독립 파라미터로 분리. - A-...

## Transcript

# Stage 1-A 지형 설계 및 개발 기록
작성일: 2026-02-25

## 1. 목적
- 스테이지 1-A를 빠르게 반복 제작/수정할 수 있게 화이트박스 지형 생성 자동화.
- 디자이너가 인스펙터 수치만 조절해 난이도(경사, 간격, 낙차, 비거리)를 즉시 튜닝.
- 씬 뷰 클릭 기반 배치(Shift+클릭)로 레벨 조립 속도 향상.

## 2. 설계 의도
Stage 1-A는 학습형 곡선으로 설계됨.
- A-1: 기본 경사 적응 구간
  - 20도 내리막(기본값)으로 관성/속도 체감.
- A-2: 점프대 + 착지 구간
  - 경사 끝에서 램프 진입, 갭을 넘어 착지.
  - 램프 각도/길이, 갭, 착지 높이 차를 독립 파라미터로 분리.
- A-3: S자 + 대도약 구간
  - 연속 기울기 전환(S자)으로 속도 제어를 요구.
  - 마지막에 큰 갭과 최종 착지로 난이도 피크를 구성.

핵심 원칙:
- 모든 구간은 "앞 구간의 끝점"을 다음 구간 시작점으로 연결.
- 구간별 수치를 Inspector 노출해서 코드 수정 없이 플레이테스트 가능.

## 3. 구현 구조
## 3.1 LevelGenerator (구간형 생성기)
파일: `Assets/Scripts/LevelGenerator.cs`

주요 역할:
- `GenerateStage1A()`에서 A-1/A-2/A-3를 순차 생성.
- `CreateConnectedSegment()`로 세그먼트를 끝점 기준 체인 연결.
- `CreateSegmentFromStart()` + 각도/길이 계산으로 중심점 배치 자동화.
- 생성물에 Collider/Physics Material/Ground 레이어 자동 적용.
- `groundTexture`를 타일드 스프라이트로 적용해 시각 일관성 유지.

확장 포인트:
- `useSectionAPrefab` 활성화 시 낱개 생성 대신 세트 프리팹 인스턴스 소환.
- `GenerateStage1ASet(worldPosition)`으로 그룹 단위 복수 배치 지원.

## 3.2 LevelEditorTool (에디터 배치 도구)
파일: `Assets/Editor/LevelEditorTool.cs`

주요 역할:
- Scene 뷰에서 Shift+좌클릭 시 `LevelGenerator.GenerateStage1ASet()` 호출.
- 클릭 월드 좌표에 Stage 1-A 세트를 그룹으로 배치.
- Undo/Scene Dirty 처리로 에디터 워크플로우와 호환.

의도:
- "인스펙터 버튼 생성 -> 위치 조정" 반복 대신
  "원하는 위치 Shift+클릭" 방식으로 레벨 작업 시간 단축.

## 3.3 SplineTerrainSet (노드형 생성기)
파일: `Assets/Scripts/SplineTerrainSet.cs`

주요 역할:
- 노드 간 직선 세그먼트를 자동 재생성(`RebuildSegments`).
- 노드 이동 즉시 지형 반영 가능한 보조 시스템.
- Stage 1-A 같은 고정 패턴 외 자유형 지형 제작 용도.

## 4. 개발 과정 (실제 작업 흐름)
1. 화이트박스 목표 정의
- 플레이 흐름을 A-1/A-2/A-3로 분리.
- 각 구간 난이도를 수치로 튜닝 가능하도록 파라미터화.

2. 핵심 생성기 구현
- LevelGenerator에서 구간별 길이/각도/갭/낙차 변수를 공개 필드로 작성.
- 연결 로직을 공통 함수화(`CreateConnectedSegment`)하여 유지보수성 확보.

3. 물리/시각 자동 부착
- 생성 직후 Collider, 마찰 Material, Ground 레이어를 자동 적용.
- 스프라이트 DrawMode=Tiled로 통일해 길이 스케일 변화에 대응.

4. 에디터 생산성 기능 추가
- LevelEditorTool로 Shift+클릭 배치 지원.
- 그룹 이름 자동 증가(`Stage1A_Group_01`...)로 다중 세트 관리.

5. 프리팹 기반 운영 모드 추가
- 구간형 생성 결과가 안정화되면 세트를 프리팹화.
- 이후 `useSectionAPrefab`로 맵 구조 변경 비용 최소화.

6. 보조 생성기 병행
- 자유형 구간은 SplineTerrainSet(노드형)으로 작성해 빠른 프로토타이핑 수행.

## 5. 현재 상태 요약
- Stage 1-A 자동 생성: 구현 완료.
- Shift+클릭 에디터 배치: 구현 완료.
- 노드 기반 지형 생성: 구현 완료.
- 구간 수치 튜닝: 인스펙터에서 즉시 가능.

## 6. 다음 개선 권장
- A-1/A-2/A-3 파라미터 프리셋(쉬움/보통/어려움) ScriptableObject화.
- 생성 검증(겹침, 극단 각도, 불가능 점프) 에디터 검증기 추가.
- Stage 1-B 이상을 동일한 체인 생성 규칙으로 확장.
