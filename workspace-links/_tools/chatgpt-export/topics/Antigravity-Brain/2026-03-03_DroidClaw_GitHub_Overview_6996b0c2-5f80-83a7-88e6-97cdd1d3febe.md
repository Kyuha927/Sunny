---
type: chatgpt-export-conversation
topic: "Antigravity-Brain"
title: "DroidClaw GitHub Overview"
conversation_id: "6996b0c2-5f80-83a7-88e6-97cdd1d3febe"
imported_at_utc: "2026-03-03T05:32:13+00:00"
turn_count: 5
chars: 4535
topic_score: 3
---

# DroidClaw GitHub Overview

- topic: `Antigravity-Brain`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/6996b0c2-5f80-83a7-88e6-97cdd1d3febe_DroidClaw_GitHub_Overview.txt`
- conversation_id: `6996b0c2-5f80-83a7-88e6-97cdd1d3febe`
- matched_keywords: 에이전트, research
- card: [[workspace-links/_catalog/cards/Antigravity-Brain|에이전트 브레인 R&D 허브]]

## Summary
https://github.com/unitedbyai/droidclaw?fbclid=IwdGRzaAQDkAdjbGNrBAOP82V4dG4DYWVtAjExAHNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABHp5yb2ghkFNlm4p5UMDOerRHrEHjD5Irypis_yZLDyrpO4M6t9DlyILWpHzY_aem_LYmZEvpfSPhXRNUu53ttzQ&sfnsn=mo

## Transcript

## 1. user

https://github.com/unitedbyai/droidclaw?fbclid=IwdGRzaAQDkAdjbGNrBAOP82V4dG4DYWVtAjExAHNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABHp5yb2ghkFNlm4p5UMDOerRHrEHjD5Irypis_yZLDyrpO4M6t9DlyILWpHzY_aem_LYmZEvpfSPhXRNUu53ttzQ&sfnsn=mo

## 2. assistant

search("https://github.com/unitedbyai/droidclaw?fbclid=IwdGRzaAQDkAdjbGNrBAOP82V4dG4DYWVtAjExAHNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABHp5yb2ghkFNlm4p5UMDOerRHrEHjD5Irypis_yZLDyrpO4M6t9DlyILWpHzY_aem_LYmZEvpfSPhXRNUu53ttzQ&sfnsn=mo")

## 3. assistant

Here’s a summary of the GitHub project you linked:

### 📌 **link_titleunitedbyai/droidclaw on GitHubturn0search0**

**DroidClaw** is an open-source project that turns Android devices into *AI agents* you can control with natural language goals. You give it a goal in plain English, and the system:

- Reads the current screen state (via Android’s accessibility tree),
- Sends that plus the goal to a large language model,
- Decides what to *tap, type, swipe, or launch*,
- Executes those actions through ADB (Android Debug Bridge), and
- Repeats until the goal is achieved. citeturn0search0

Think of it as an AI “robot” that navigates your phone like a human would — without needing app-specific APIs. citeturn0search1

---

### 🤖 What It Does

- **AI-Powered Control:** An LLM interprets the UI and determines actions.
- **Three Modes:**
  - **Interactive** — type a goal and it figures out what to do.
  - **Workflows** — JSON scripts of multi-step goals across apps.
  - **Flows** — fixed, deterministic YAML macros (no AI). citeturn0search0

---

### 🛠 How It Works

1. **Perceive:** Dump and parse the accessibility tree of the screen. citeturn0search0  
2. **Reason:** Send the UI state + goal to an LLM, which returns a plan + action. citeturn0search0  
3. **Act:** Execute taps, typing, swipes, on the device via ADB. citeturn0search0  
4. **Adapt:** Loop until done, with stuck detection and recovery. citeturn0search0

The repo includes example workflows like sending WhatsApp messages, posting on social media, checking weather or flights, posting Slack standups, ordering food, etc. citeturn0search0

---

### 🧠 Notable Use Cases

- Automate messaging (WhatsApp, SMS, Telegram)  
- Research & data gathering (Google search, news roundup)  
- Productivity tasks (calendar events, notes)  
- Social actions (posting, liking, navigating apps)  
- Device control (toggle wifi/brightness) citeturn0search0

---

### 📦 Tech Stack

- Written primarily in **TypeScript** using **Bun**  
- Uses Android **ADB + accessibility** for control  
- Supports various LLM providers (Groq, OpenAI, Ollama, etc.) citeturn0view0

---

### ⚠️ Limitations

Works best with standard native apps. It can struggle with:

- WebViews, games, apps with poor accessibility support  
- Some complex UI interactions like drag-and-drop  
- Apps that block accessibility tools (e.g., banking apps) citeturn0search0

---

If you want, I can walk you through how to set it up, or help with writing a workflow for a specific task you want to automate on your device.

## 4. user

한글

## 5. assistant

링크에 있는 **DroidClaw** 프로젝트를 한글로 정리해줄게.

---

## 📌 DroidClaw이란?

**DroidClaw**는 안드로이드 스마트폰을 “AI 에이전트”처럼 제어할 수 있게 해주는 오픈소스 프로젝트야.

👉 사람이 직접 터치하는 대신  
👉 AI가 화면을 읽고  
👉 무엇을 눌러야 할지 판단하고  
👉 실제로 터치/입력/스와이프를 실행함

즉, **자연어 목표를 주면 AI가 휴대폰을 대신 조작하는 시스템**이야.

---

## 🤖 어떻게 동작하나?

기본 루프는 다음과 같아:

1. **Perceive (인식)**  
   - 현재 화면의 접근성 트리(accessibility tree)를 읽음
   - 버튼, 텍스트, 입력창 등의 UI 구조 파악

2. **Reason (판단)**  
   - 화면 정보 + 사용자가 준 목표를 LLM(대형언어모델)에 전달
   - 다음에 무엇을 눌러야 할지 결정

3. **Act (실행)**  
   - ADB(Android Debug Bridge)를 통해 실제 터치/입력 수행

4. **Loop (반복)**  
   - 목표가 달성될 때까지 반복

---

## 🧩 사용 모드

### 1️⃣ Interactive 모드
- "카톡에서 엄마한테 오늘 늦는다고 보내줘"
- 이런 식으로 자연어 목표를 입력
- AI가 알아서 앱 실행 → 채팅방 이동 → 메시지 입력 → 전송

### 2️⃣ Workflow 모드
- JSON 기반 멀티스텝 자동화
- 예: 뉴스 검색 → 요약 → 노트 앱에 저장

### 3️⃣ Flow 모드
- AI 없이 YAML 기반 고정 매크로 실행
- 전통적인 자동화 방식

---

## 🛠 기술 스택

- TypeScript 기반
- Bun 런타임 사용
- Android ADB + 접근성 API 활용
- OpenAI / Groq / Ollama 등 다양한 LLM 연결 가능

---

## 📱 가능한 활용 예시

- 메시지 자동 전송
- SNS 자동 포스팅
- 날씨/뉴스 확인 후 정리
- 캘린더 일정 등록
- 설정 토글 (와이파이, 밝기 등)

---

## ⚠️ 한계

잘 안 되는 경우도 있음:

- WebView 기반 앱
- 게임
- 접근성 차단 앱 (은행 앱 등)
- 드래그/복잡한 제스처

---

## 🔥 너한테 중요한 포인트

너가 예전에 말했던:

> “빅스비처럼 음성으로 부르면 AI가 대신 실행”

이 구조를 만들 때  
👉 DroidClaw 같은 방식이 **모바일 쪽 자동화 엔진**으로 쓸 수 있음

- 음성 인식 → 목표 생성
- 목표 → DroidClaw에 전달
- AI가 폰 제어
- 완료 후 종료

---

원하면:

1. 🔧 설치 방법 단계별로 정리해줄까?
2. 🧠 너 시스템(로컬 AI + PC 자동화)과 어떻게 결합할지 설계해줄까?
3. 📱 노트북/WSL 환경에서 돌리는 방법 정리해줄까?

어느 방향으로 파볼까?
