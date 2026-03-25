---
type: concept
tags:
  - copilot
created: 2026-03-25
summary: ""
---
# File
copilot/copilot-custom-prompts/Emojify.md

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
copilot-command-context-menu-order: 1050
copilot-command-model-key: ""
copilot-command-last-used: 0
---
Add relevant emojis to enhance {}. Follow these rules:
    1. Insert emojis at natural breaks in the text
    2. Never place two emojis next to each other
    3. Keep all original text unchanged
    4. Choose emojis that match the context and tone
    Return only the emojified text.

## 이모지 변환 프롬프트 운영 지침 보강 (2026-02-15)
### 문서별 관찰
- 이모티콘 렌더링은 플랫폼마다 달라서, 사용량을 낮게 유지하는 편이 안전합니다.
- 복잡한 ZWJ 이모티콘은 일부 클라이언트에서 깨질 수 있습니다.
### 권장 작업
1. 문장당 이모티콘은 최대 1개로 제한하세요.
2. 제목에 이모티콘을 사용하지 마세요.
3. 모호하거나 냉소적으로 읽힐 수 있는 이모티콘은 기본 차단으로 두세요.
### 참고 링크
- https://unicode.org/reports/tr51/
- https://unicode.org/emoji/charts/full-emoji-list.html

```
