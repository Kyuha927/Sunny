# 프로젝트/폴더 네이밍 규칙

“이름만 보고도 역할을 알 수 있게” 하기 위한 기준입니다.

## 1) 프로젝트 ID (시스템용)

- 형식: `Domain-Product-Scope`
- 예시:
  - `Agent-Brain-RnD`
  - `Agent-Execution-Tracker`
  - `Game-MSW-Core`
  - `Game-MSW-Experiment`

## 2) 표시 이름 (사람용)

- 카드에는 `display_name`을 사용합니다.
- 짧고 역할 중심으로 씁니다.
- 예시:
  - `에이전트 브레인 R&D 허브`
  - `실행 로그·코드 추적 허브`
  - `MSW 본편 개발`

## 3) 폴더명

- 형식: `{영역번호}_{도메인}_{핵심목적}`
- 숫자로 정렬 우선순위를 고정합니다.
- 예시:
  - `01_game_msw_core`
  - `11_agent_brain_rnd`
  - `21_prompt_copilot_library`

## 4) 금지 패턴

- 의미 없는 이름: `new`, `tmp`, `test2`, `final-final`
- UUID 폴더를 사람이 직접 탐색 경로로 사용
- 한글/영문 혼합 시 규칙 없는 임의 표기

## 5) 운영 규칙

1. 원본 경로를 바꾸기 어려우면 `project-shortcuts`에 의미형 별칭을 만듭니다.
2. 대시보드/칸반은 파일명 대신 `display_name`을 우선 표기합니다.
3. 신규 프로젝트 생성 시 카드(frontmatter)와 바로가기를 동시에 만듭니다.
