# Project — Codex-Chat-GUI-NextGen-clean

## DoD
- [ ] Ubuntu ext4 기준 작업 경로를 완전히 표준화
- [ ] 로컬 전용 파일 9개의 보존/커밋 여부를 결정
- [ ] `.venv`, `node_modules`, 외부 시크릿 복구 절차를 다시 검증

## Current Status
- 표준 작업 경로는 fresh clone 기반 `feature/copilot-agents-auto-handoff` 브랜치로 교체됨.
- 원격 `origin/feature/copilot-agents-auto-handoff`와 commit 기준 `0 / 0`으로 동기화됨.
- 기존 dirty 작업본은 별도 백업 경로로 보존했고, Ubuntu 이전용 문서와 스크립트만 선별 유지함.
- `/mnt/c` 직접 대량 복사보다 ext4에서 아카이브를 만든 뒤 필요한 결과만 옮기는 방식이 훨씬 빠르다는 점을 확인함.

## Key Links
- [[workspace-links/_catalog/cards/Codex-Chat-GUI-NextGen-clean|Codex-Chat-GUI-NextGen-clean 프로젝트 카드]]
- [[workspace-links/_catalog/updates/Codex-Chat-GUI-NextGen-clean/2026-03-18|2026-03-18 업데이트]]
- [[workspace-links/_catalog/cards/Antigravity-Brain|Antigravity-Brain]]
- [[workspace-links/_catalog/cards/Copilot-Prompts|Copilot-Prompts]]

## Next Actions
- `.env`, migration handoff 문서, migration 스크립트 4종을 Git에 올릴지 로컬 전용으로 유지할지 결정.
- Ubuntu 복원 후 `.venv` 재생성, smoke/route 검증 재실행.
- Vault 기준 링크와 프로젝트 카드가 실제 작업 흐름과 맞는지 점검.
