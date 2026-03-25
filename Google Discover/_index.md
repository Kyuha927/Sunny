---
type: moc
tags:
  - google-discover
  - archive
  - moc
created: 2026-03-25
summary: "Google 알림 추천 기사 아카이브 인덱스"
---
# Google Discover 아카이브

Tasker + AutoNotification으로 자동 수집한 Google 추천 기사 모음.

## 최근 아카이브

- [[Google Discover/2026-03-25|2026-03-25]]
- [[Google Discover/2026-03-24|2026-03-24]]

## 사용법

1. 폰에서 Tasker가 Google 알림을 인터셉트
2. `/sdcard/Tasker/google_discover.jsonl`에 자동 저장
3. Syncthing 또는 ADB로 PC에 동기화
4. `python scripts/discover_to_obsidian.py` 실행 → 일별 노트 자동 생성

## 관련 노트

- [[0_Inbox]]
