# Anthropic Skilljar 정리 및 적용안 (2026-03-03)

- source entry: https://anthropic.skilljar.com/
- status: 자동 fetch는 403으로 차단됨. 아래 내용은 공개 검색 인덱스에 노출된 코스 설명/커리큘럼 기반 요약.
- confidence: medium (상세 영상 내용은 미수집)

## 확인된 코스 축

1. Claude Code in Action
- 핵심: 컨텍스트 제어, 커스텀 커맨드, MCP 서버 연동, GitHub 통합, Hooks/SDK
- 우리 적용 포인트: Codex/브리지 작업에 훅 기반 품질 게이트와 표준 커맨드 세트 추가

2. Introduction to Model Context Protocol
- 핵심: MCP 3요소(tools/resources/prompts), 서버/클라이언트 구현 흐름
- 우리 적용 포인트: 현재 멀티 에이전트 도구 체계를 MCP 명세 기반으로 정리해 재사용성 강화

3. Building with the Claude API / Vertex / Bedrock
- 핵심: 멀티턴 메시지 처리, 프롬프트 평가, tool use, RAG, 운영 패턴
- 우리 적용 포인트: 라우팅/자동화 결과를 평가 가능한 지표(정확도, 실패율, 재시도율)로 관리

4. Driving enterprise adoption / Train the Trainer
- 핵심: 단계별 도입 프레임워크, 체크리스트, 챔피언 프로그램, 확산 운영
- 우리 적용 포인트: 개인 운영에서 팀 운영으로 확장 가능한 온보딩 패키지 마련

5. AI Fluency (Framework & Foundations 등)
- 핵심: Delegation/Description/Discernment/Diligence의 4D 루프
- 우리 적용 포인트: 작업 요청 템플릿에 4D를 붙여 품질 편차 축소

## 우리 프로젝트(Moltbot/Obsidian/Notion)에 바로 적용할 것

### A. Codex 실행 표준화 (이번 주)
- `tools/handoff/`에 작업 타입별 표준 커맨드 프리셋 추가
- 목적: 프롬프트 의존을 줄이고 재현 가능한 실행 경로 확보

### B. Hook 기반 검증 파이프라인 (이번 주)
- 자동 실행 종료 시 최소 검증: `py_compile` + 관련 스모크 + 산출물 존재 확인
- 목적: “완료 보고 전에 실패 발견” 비율을 높여 재작업 감소

### C. MCP 스타일 도구 카탈로그 (다음 주)
- 도구를 `tool`, `resource`, `prompt` 단위로 인벤토리
- 목적: 신규 자동화 추가 시 통합 비용 절감

### D. Obsidian 지식 병합 품질 규칙 (다음 주)
- 유사도 임계치 + 토픽별 우선 타깃 노트 화이트리스트
- 목적: 잘못된 노트 병합(노이즈) 감소

### E. Notion 동기화 운영 규칙 (다음 주)
- “주제 digest -> 승인 -> notion import” 3단계 고정
- 목적: 정제 전 대량 반영 방지, 문서 품질 유지

## 실행 백로그 (체크리스트)

- [ ] `merge_chatgpt_topics_into_obsidian_notes.py`에 토픽별 타깃 화이트리스트 옵션 추가
- [ ] `organize_chatgpt_export_to_obsidian.py`에 코스/출처 태그 체계 추가
- [ ] ChatGPT/Anthropic 외부 학습 소스 ingest 공통 리포트 포맷(JSON+MD) 통일
- [ ] 주간 1회: 업데이트 노트에서 Notion 반영 대상 승인 리스트 생성

## 참고 링크(검색 인덱스 기반)

- Claude Code in Action: https://anthropic.skilljar.com/claude-code-in-action/303233
- Introduction to Model Context Protocol: https://anthropic.skilljar.com/introduction-to-model-context-protocol
- Building with the Claude API: https://anthropic.skilljar.com/claude-with-the-anthropic-api/287735
- Claude with Google Vertex AI: https://anthropic.skilljar.com/claude-with-google-vertex
- Claude with Amazon Bedrock: https://anthropic.skilljar.com/claude-in-amazon-bedrock
- Driving enterprise adoption of Claude: https://anthropic.skilljar.com/driving-enterprise-adoption-of-claude
- AI Fluency: Framework & Foundations: https://anthropic.skilljar.com/ai-fluency-framework-foundations/291863
