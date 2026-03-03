---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: false
copilot-command-context-menu-order: 1100
copilot-command-model-key: ""
copilot-command-last-used: 0
---
Remove all URLs from {}. Preserve all other content and formatting. URLs may be in various formats (http, https, www). Return only the text with URLs removed.

## URL 제거 프롬프트 보강 (2026-02-15)
### 문서별 관찰
- URL 패턴은 RFC 3986 기준으로 형태가 다양하므로 신중하게 처리해야 합니다.
- 마크다운 링크는 URL이 제거될 때 앵커 텍스트를 유지해야 합니다.
### 권장 작업
1. `[text](url)` 형식은 `text`만 남기도록 변환하세요.
2. 이메일 주소와 파일 경로 패턴은 제외하세요.
3. 구두점과 공백은 마지막에 한 번 정리하세요.
### 참고 링크
- https://www.rfc-editor.org/rfc/rfc3986
- https://spec.commonmark.org/
