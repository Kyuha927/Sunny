---
type: concept
tags:
  - copilot
created: 2026-03-25
summary: ""
---
# File
copilot/copilot-custom-prompts/Simplify.md

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
copilot-command-context-menu-order: 1030
copilot-command-model-key: ""
copilot-command-last-used: 0
---
Simplify {} to a 6th-grade reading level (ages 11-12). Use simple sentences, common words, and clear explanations. Maintain the original key concepts. Return only the simplified text.

## 문장 단순화 프롬프트 보강 (2026-02-15)
### 문서별 관찰
- 짧은 문장과 능동태를 쓰면 가독성이 좋아집니다.
- 기술 문서를 단순화할 때는 인라인 용어 설명이 사실상 필수입니다.
### 권장 작업
1. 문장 길이를 짧게 제한하세요.
2. 수동태보다 능동태를 우선 사용하세요.
3. 단락당 한 줄 요약을 강제하세요.
### 참고 링크
- https://www.plainlanguage.gov/guidelines/
- https://www.cdc.gov/ccindex/

```
