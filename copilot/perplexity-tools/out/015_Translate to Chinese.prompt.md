---
type: concept
tags:
  - copilot
created: 2026-03-25
summary: ""
---
# File
copilot/copilot-custom-prompts/Translate to Chinese.md

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
copilot-command-context-menu-order: 1010
copilot-command-model-key: ""
copilot-command-last-used: 0
---
Translate {} into Chinese:
    1. Preserve the meaning and tone
    2. Maintain appropriate cultural context
    3. Keep formatting and structure
    Return only the translated text.

## 중국어 번역 프롬프트 보강 (2026-02-15)
### 문서별 관찰
- 중국어 일관성을 위해서는 명확한 스크립트 선택이 필요합니다(zh-Hans 대 zh-Hant).
- 기술 번역에서는 이름/코드/URL을 엄격하게 보존해야 합니다.
### 권장 작업
1. 기본 대상을 zh-Hans로 설정하세요.
2. 보호 약관을 변경하지 않고 유지하세요.
3. 모호한 표현에는 괄호 설명을 허용하세요.
### 참고 링크
- https://www.w3.org/International/articles/language-tags/
- https://ai.google.dev/guide/prompt_best_practices

```
