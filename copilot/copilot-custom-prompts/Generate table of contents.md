---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: false
copilot-command-context-menu-order: 1080
copilot-command-model-key: ""
copilot-command-last-used: 0
---
Generate a hierarchical table of contents for {}. Use appropriate heading levels (H1, H2, H3, etc.). Include page numbers if present. Return only the table of contents.

## 목차 생성 프롬프트 보강 (2026-02-15)
### 문서별 관찰
- 제목을 파싱할 때는 오탐을 막기 위해 코드/인용 블록을 제외해야 합니다.
- 탐색성을 높이려면 섹션 링크 동작을 고려해야 합니다.
### 권장 작업
1. 기본 범위는 H1-H3로 두세요.
2. 제목 레벨이 갑자기 뛰면 경고를 띄우세요.
3. 출력 모드 토글을 추가해 두세요.
### 참고 링크
- https://spec.commonmark.org/
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/basic-writing-and-formatting-syntax#section-links
