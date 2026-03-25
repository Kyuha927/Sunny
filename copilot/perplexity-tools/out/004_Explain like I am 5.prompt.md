---
type: concept
tags:
  - copilot
created: 2026-03-25
summary: ""
---
# File
copilot/copilot-custom-prompts/Explain like I am 5.md

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
copilot-command-context-menu-order: 1040
copilot-command-model-key: ""
copilot-command-last-used: 0
---
Explain {} in simple terms that a 5-year-old would understand:
    1. Use basic vocabulary
    2. Include simple analogies
    3. Break down complex concepts
    Return only the simplified explanation.

## 아동 눈높이 설명 프롬프트 보강 (2026-02-15)
### 문서별 관찰
- 쉬운 언어 규칙을 적용하면 낮은 읽기 수준에서도 이해도가 올라갑니다.
- 기술 용어를 쓸 때는 바로 뒤에 짧고 쉬운 정의를 붙여야 합니다.
### 권장 작업
1. 한 문장에는 핵심 개념 하나만 담으세요.
2. 일상 비유는 필요한 만큼만 제한적으로 쓰세요.
3. 마지막은 한 문장 요약으로 마무리하세요.
### 참고 링크
- https://www.plainlanguage.gov/guidelines/
- https://www.cdc.gov/ccindex/

```
