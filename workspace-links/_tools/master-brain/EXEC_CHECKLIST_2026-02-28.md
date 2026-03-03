# EXEC CHECKLIST (2026-02-28)

## A. 필수 루틴 (매 작업 시작/종료)
- [ ] 시작 전 sync_master_chat 실행
- [ ] 핵심 작업 후 daily_intelligence.py --verify 실행
- [ ] 종료 전 최종 sync_master_chat 재실행
- [ ] 결과 아티팩트 경로 기록

## B. 오늘 우선 작업
- [ ] watcher: processed 캐시 상한 적용
- [ ] watcher: malformed 요청 격리 로직 검증
- [ ] Fold1 8023/8022 복구 루틴 점검
- [ ] ChatGPT export zip 인입 스모크

## C. 장애 대응 체크
- [ ] timeout/인증/라우팅/포맷/리소스 중 실패 분류 태깅
- [ ] 재현 명령 1개 이상 기록
- [ ] 임시 우회책 + 근본 수정 분리 기록
- [ ] 동일 장애 재발 여부 체크

## D. 성능/안정성 체크
- [ ] 16GB 환경에서 IDE+Chrome 동시 사용 시 체감 지표 기록
- [ ] 스왑/메모리 압박 시 대체 루트(WSL/Fold1) 전환 기준 확인
- [ ] 장시간 작업 세션에서 verify PASS 유지 확인

## E. 주간 KPI
- [ ] 자동화 성공률
- [ ] 재작업 횟수
- [ ] MTTR(복구 시간)
- [ ] 컨텍스트 손실 건수

## F. Done 정의
- [ ] 오늘 핵심 루틴(sync/verify/sync) 완료
- [ ] 실패 케이스 분류/기록 완료
- [ ] 다음 액션 3개 이하로 압축
- [ ] 내일 시작 시 바로 재개 가능한 상태
