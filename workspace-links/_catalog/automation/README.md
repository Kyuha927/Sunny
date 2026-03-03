# Project Intel Automation

프로젝트 카드(`workspace-links/_catalog/cards/*.md`)를 최신 외부 정보 기반으로 주기 업데이트합니다.

## 포함 파일

- `project_intel_sources.json`: 프로젝트별 수집 소스/쿼리 설정
- `update_project_intel.py`: 수집 + 노트/카드 업데이트 엔진
- `run_project_intel_update.ps1`: 수동/스케줄 실행용 런처
- `install_project_intel_task.ps1`: Windows 작업 스케줄러 등록
- `uninstall_project_intel_task.ps1`: 작업 스케줄러 제거

## 1회 수동 실행

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\jhk92\OneDrive\문서\Obsidian Vault\workspace-links\_catalog\automation\run_project_intel_update.ps1"
```

## 스케줄러 설치 (기본: 매일 08:30)

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\jhk92\OneDrive\문서\Obsidian Vault\workspace-links\_catalog\automation\install_project_intel_task.ps1"
```

시간 변경 예시:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\jhk92\OneDrive\문서\Obsidian Vault\workspace-links\_catalog\automation\install_project_intel_task.ps1" -DailyAt "07:10"
```

## 산출물

- 프로젝트별 리포트: `workspace-links/_catalog/updates/{ProjectId}/{YYYY-MM-DD}.md`
- 실행 로그: `workspace-links/_catalog/updates/_logs/project_intel_update_*.log`
- 프로젝트 카드에 자동 블록 삽입:
  - `<!-- AUTO_INTEL:START -->`
  - `<!-- AUTO_INTEL:END -->`

## 설정 팁

- `project_intel_sources.json`에서 프로젝트별 `google_news_queries`, `rss_feeds`, `github_release_feeds`, `arxiv_queries`를 조정하면 정확도가 올라갑니다.
- 오래된 소스/노이즈 소스는 제거하고, 공식 문서/릴리즈 피드 중심으로 유지하세요.
