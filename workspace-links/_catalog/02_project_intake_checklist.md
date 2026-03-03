# 새 프로젝트 등록 체크리스트

## 1) Junction 연결
```powershell
& ".\workspace-links\_tools\add-workspace-link.ps1" `
  -TargetPath "C:\Projects\NewProject" `
  -Category "projects"
```

## 2) 카드 생성
1. `workspace-links/_catalog/cards/_template_project_card.md` 복제
2. 파일명을 프로젝트명으로 변경
3. 아래 필드 작성
- `domain`, `artifact_type`, `execution_mode`
- `phase`, `review_cycle`, `priority`, `risk_level`
- `workflow_stage`, `sequence_order`, `kanban_lane`, `plan_start`, `plan_end`, `progress_pct`
- `status_now`, `major_issues`, `next_actions`

## 3) 연관성 작성
1. `relations` 최소 2개 입력
2. `kind`, `direction`, `strength`, `reason` 채움
3. 최소 1개는 같은 `domain`, 최소 1개는 다른 `domain` 연결

## 4) 대시보드 등록
1. `workspace-links/_catalog/00_project_dashboard.md`에 카드가 보이는지 확인
2. `workspace-links/_catalog/04_execution_overview.md`에서 순서/현황 표시 확인
3. `workspace-links/_catalog/05_kanban_execution.md`에서 레인 배치 확인
4. `workspace-links/_catalog/03_relationship_dashboard.md`에서 관계 표시 확인

## 5) 유지보수
1. `review_cycle` 주기마다 `status_now`, `major_issues`, `next_actions` 갱신
2. 상태 변경 시 `last_review` 함께 수정
3. 일정 변경 시 `plan_start`/`plan_end`와 간트차트를 함께 갱신
