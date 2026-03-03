# PROJECT MAP (2026-02-28)

## North Star
- Moltbot를 "중단 후 즉시 재개 가능한 태스크형 에이전트 운영체계"로 고정.
- 로그/결정/아티팩트가 Daily Rollup + Context Pack으로 누적 합성되는 구조 유지.

## Core Systems
- 	ools/sync_master_chat.py : SSOT ↔ Obsidian 미러 동기화
- daily_intelligence.py --verify : 일일 브리프 생성/검증
- 운영 루틴: sync -> verify -> sync

## Routing Policy (현재 실전)
- 일반 코딩/빌드/테스트: WSL-Ubuntu 우선
- Heavy automation: Fold1 우선, 실패 시 WSL fallback
- Browser/Antigravity 성격 작업: 전용 경로 우선

## Active Focus (우선순위)
1. ntigravity_bridge_watcher.py 안정화
   - processed 캐시 상한
   - malformed 요청 격리
2. Fold1(8023/8022) 복구 루틴 상시 가동성 확보
3. ChatGPT export ingestion 파이프라인 스모크
4. 16GB 환경 병목 완화(IDE + Chrome 동시 사용)

## Top Risks
- 브리지/동기화 포인트 증가로 장애 원인 분리 난이도 상승
- 일부 문서 인코딩 깨짐으로 검색 품질 저하 가능
- 경로 다양화(Windows/WSL/Fold1)로 운영 복잡도 증가

## 7-Day Execution Plan
- D1-2: watcher 안정화 + 회귀 체크
- D3: Fold1 doctor/복구 자동화 점검
- D4: ChatGPT export ingest 스모크 + 실패 케이스 기록
- D5: sync/verify 장애 시나리오 테스트
- D6: 운영 KPI 보드(성공률/재작업/MTTR/컨텍스트 손실)
- D7: 주간 리트로 + 백로그 재정렬

## Success Criteria
- verify PASS 연속성 유지
- 동기화 실패 재발률 감소
- 복구 시간(MTTR) 단축
- "다음 액션" 기준 즉시 재개 가능 상태 유지
