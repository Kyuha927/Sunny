---
type: concept
tags:
  - copilot
created: 2026-03-25
summary: ""
---
# File
copilot/copilot-custom-prompts/Make shorter.md

# Prompt
Role: Technical documentation enhancement editor.
Goal: Improve the markdown document using current, evidence-backed research.
Rules:
- Add source URLs for factual claims.
- Use absolute dates (YYYY-MM-DD) for recent facts.
- Remove duplication and improve structure.
Output:
1) Top 10 improvement points
2) Research summary with sources
3) Final integrated markdown ready to paste

Document source:
```markdown
---
copilot-command-context-menu-enabled: true
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 1060
copilot-command-model-key: ""
copilot-command-last-used: 0
---
Reduce {} to half its length while preserving these elements:
    1. Main ideas and key points
    2. Essential details
    3. Original tone and style
    Return only the shortened text.

## 본문 축약 프롬프트 보강 (2026-02-15)
### 문서별 관찰
- 압축은 필수 항목을 먼저 추출할 때 가장 잘 작동합니다.
- 2단계 요약은 논리 손실을 줄여 줍니다.
### 권장 작업
1. 결론/숫자/조건/예외를 유지하세요.
2. 누락되지 않은 키포인트 자체 검사를 추가해 두세요.
3. 테이블/목록 구조를 그대로 유지하세요.
### 참고 링크
- https://docs.anthropic.com/en/docs/prompt-engineering
- https://ai.google.dev/guide/prompt_best_practices

```
