# 프로젝트 인텔리전스 허브

자동 수집된 최신 외부 정보를 프로젝트 카드와 연결해 모니터링하는 페이지입니다.

## 최신 리포트 (프로젝트별 1개)
```dataviewjs
const updates = dv.pages('"workspace-links/_catalog/updates"')
  .where(p => p.type === "project-intel-update")
  .sort(p => p.generated_at, 'desc');

const latestMap = new Map();
for (const u of updates) {
  if (!latestMap.has(u.project_id)) {
    latestMap.set(u.project_id, u);
  }
}

const rows = Array.from(latestMap.values()).map(u => [
  u.project_id ?? "",
  u.generated_at ?? "",
  u.item_count ?? 0,
  u.file.link
]);

dv.table(["Project", "GeneratedAt", "Signals", "Report"], rows);
```

## 전체 히스토리
```dataview
TABLE
  project_id AS Project,
  generated_at AS GeneratedAt,
  item_count AS Signals,
  file.link AS Report
FROM "workspace-links/_catalog/updates"
WHERE type = "project-intel-update"
SORT generated_at DESC
```

## 점검 규칙
1. 매일 `item_count`가 0인 프로젝트는 소스/쿼리를 재조정합니다.
2. 핵심 시그널은 프로젝트 카드의 `next_actions`와 주 1회 동기화합니다.
3. 신뢰 가능한 공식 소스 비율을 유지하고, 노이즈 소스는 제거합니다.
