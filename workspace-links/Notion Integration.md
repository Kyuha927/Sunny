---
type: concept
tags:
  - concept
  - workspace-links
created: 2026-03-25
summary: "Notion Integration"
tags::
  - workspace-links
---
# Notion 연동 정보

> 이 파일은 에이전트가 Notion 관련 작업 시 반드시 참조할 것

## API Token
- 파일: `~/projects/Sunny/workspace-links/Notion API Credentials.md`
- 환경변수: `NOTION_TOKEN`

## Page/DB ID
- 원페이지 기획서: `fd80956f-4986-83e5-a819-814c0ac7b1b0`
- Daily Report DB: `~/.notion_daily_db_id`
- 공개 URL: `https://mountainous-niece-acc.notion.site/1-87d0956f4986823cbcff016984c3e91a`

## 양식 원본
- `~/다운로드/Windows_Projects/antigravity_brains/a3bc3949-7bc2-4426-8719-e51869b6426c/ONE-PAGE-SPEC-TEMPLATE.md`
- `~/다운로드/Windows_Projects/antigravity_brains/a3bc3949-7bc2-4426-8719-e51869b6426c/DAILY-REPORT-TEMPLATE.md`

## 상세 가이드
- `~/다운로드/.agent/know-how/NOTION_INTEGRATION.md`

## 스크립트
- `~/.local/bin/notion_sync.py` — Notion API 동기화
- `~/.local/bin/daily_report.sh` — 매일 자동 실행 (cron 23시)