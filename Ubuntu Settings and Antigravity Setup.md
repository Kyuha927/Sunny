---
tags: [Ubuntu, Setup, Server, Antigravity, System]
aliases: [우분투 초기 설정, 안티그래비티 셋업]
date: 2026-03-22
---

# 🐧 Ubuntu Settings & Antigravity Setup

우분투 환경에서 Antigravity(AI 에이전트)를 멈춤이나 충돌 없이 안정적으로 구동하기 위한 시스템 레벨 설정과 패치 내역을 기록한다.

## 1. 터미널 및 시스템 의존성 패치 (Infinite Hang 방지)
Antigravity 에이전트가 `Running` 상태나 `Loading`에서 무한루프(Hang)에 걸리는 문제의 70%는 기반 OS 라이브러리와 버전 충돌에서 기인한다. (2026-03-22 패치 적용)

### glibc 수동 업그레이드
```bash
sudo apt update && sudo apt install libc6=2.38-1ubuntu6 -y
```

### Antigravity 안정화 버전 (v1.16.5) 고정
가장 크래시가 덜 나는 구버전(1.16.5)으로 롤백 및 고정:
```bash
cd /tmp
wget https://github.com/google/antigravity/releases/download/v1.16.5/antigravity-1.16.5-linux_amd64.deb
sudo dpkg -i antigravity-1.16.5-linux_amd64.deb
```

## 2. 셸 오버라이드 환경 변수 (`~/.bashrc`)
Wayland 디스플레이 서버를 쓰는 시스템 구동이나 내부 타임아웃 방지를 위해 다음 내용을 `.bashrc` 최하단에 등록한다.
```bash
export ELECTRON_OZONE_PLATFORM_HINT=auto
export ANTIGRAVITY_SHELL_TIMEOUT=30
```

## 3. 데일리 캐시 클리너 (Cron)
시스템에 누적된 더미 쓰레기 로그/세션 찌꺼기가 쌓이면 에이전트가 오작동하므로, 매일 새벽에 안전 캐시 영역을 지워주도록 크론잡(Crontab)을 등록한다.
*(주의: `~/.gemini`를 삭제하면 활성화된 Antigravity 브레인이 초기화되므로 채팅 중 셧다운(Shutdown) 이후에 되도록 예약할 것)*
```bash
0 4 * * * rm -rf ~/.antigravity ~/.gemini
```
