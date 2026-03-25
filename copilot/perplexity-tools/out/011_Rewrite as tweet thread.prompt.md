---
type: concept
tags:
  - copilot
created: 2026-03-25
summary: ""
---
# File
copilot/copilot-custom-prompts/Rewrite as tweet thread.md

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
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: false
copilot-command-context-menu-order: 1120
copilot-command-model-key: ""
copilot-command-last-used: 0
---
Convert {} into a Twitter thread following these rules:
    1. Each tweet must be under 240 characters
    2. Start with "THREAD START" on its own line
    3. Separate tweets with "

---

"
    4. End with "THREAD END" on its own line
    5. Make content engaging and clear
    Return only the formatted thread.

## 트윗 스레드 변환 프롬프트 보강 (2026-02-15)
### 문서별 관찰
- 글자 수를 보수적으로 잡으면 스레드 안정성이 좋아집니다.
- Hook-first와 CTA-last 구조를 쓰면 가독성이 좋아집니다.
### 권장 작업
1. '1/N' 번호 매기기를 추가해 두세요.
2. URL이 포함된 게시물에는 더 엄격한 길이 제한을 적용하세요.
3. 명확한 다음 작업으로 마무리하세요.
### 참고 링크
- https://help.x.com/en/using-x/types-of-posts
- https://help.x.com/en/using-twitter/twitter-blue-how-to

```
