# File
copilot/copilot-custom-prompts/Fix grammar and spelling.md

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
copilot-command-context-menu-order: 1000
copilot-command-model-key: ""
copilot-command-last-used: 0
---
Fix the grammar and spelling of {}. Preserve all formatting, line breaks, and special characters. Do not add or remove any content. Return only the corrected text.

## 문법·맞춤법 교정 프롬프트 보강 (2026-02-15)
### 문서별 관찰
- 마크다운/YAML/코드는 토큰 보존 규칙 없이 문법 수정 중에 쉽게 깨질 수 있습니다.
- 사소한 구문 편집으로 의미가 바뀔 수 있습니다.
### 권장 작업
1. 분리 코드 블록과 인라인 코드는 수정 대상에서 제외하세요.
2. YAML 순서와 들여쓰기를 유지하세요.
3. 숫자, 단위, 고유명사는 바꾸지 마세요.
### 참고 링크
- https://spec.commonmark.org/
- https://yaml.org/spec/1.2.2/

```
