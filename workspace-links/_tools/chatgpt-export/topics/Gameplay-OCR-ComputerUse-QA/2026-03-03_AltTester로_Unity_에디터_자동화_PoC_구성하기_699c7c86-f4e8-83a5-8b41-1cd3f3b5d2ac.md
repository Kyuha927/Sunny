---
type: chatgpt-export-conversation
topic: "Gameplay-OCR-ComputerUse-QA"
title: "AltTester로 Unity 에디터 자동화 PoC 구성하기"
conversation_id: "699c7c86-f4e8-83a5-8b41-1cd3f3b5d2ac"
imported_at_utc: "2026-03-03T05:32:14+00:00"
turn_count: 2
chars: 1362
topic_score: 2
---

# AltTester로 Unity 에디터 자동화 PoC 구성하기

- topic: `Gameplay-OCR-ComputerUse-QA`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/699c7c86-f4e8-83a5-8b41-1cd3f3b5d2ac_AltTester_Unity_PoC.txt`
- conversation_id: `699c7c86-f4e8-83a5-8b41-1cd3f3b5d2ac`
- matched_keywords: 제어, use
- card: [[workspace-links/_catalog/cards/Gameplay-OCR-ComputerUse-QA|게임플레이 OCR 제어 QA]]

## Summary
## 1. assistant AltTester Unity SDK 2.3.0 Unity Editor automation deterministic test runner TCP port 13000 WSS support NUnit harness PoC example ## 2. assistant 최근 Unity 프로젝트 자동화를 고민하고 있다면, 공식 **AltTester Unity SDK**를 이용해 **Play in Editor** 상태에서도 안정적으로 UI 테스트를 실행하는 PoC(Proof‑of‑Concept)를 빠르게 구성할 수 있습니다. 이 방법은 Unity 에디터와 NUnit 기반 테스트를 결합해 반복 가능하고 결정적인 패스/폴...

## Transcript

## 1. assistant

AltTester Unity SDK 2.3.0 Unity Editor automation deterministic test runner TCP port 13000 WSS support NUnit harness PoC example

## 2. assistant

최근 Unity 프로젝트 자동화를 고민하고 있다면, 공식 **AltTester Unity SDK**를 이용해 **Play in Editor** 상태에서도 안정적으로 UI 테스트를 실행하는 PoC(Proof‑of‑Concept)를 빠르게 구성할 수 있습니다. 이 방법은 Unity 에디터와 NUnit 기반 테스트를 결합해 반복 가능하고 결정적인 패스/폴 테스트를 자동으로 돌려볼 수 있도록 해줍니다. citeturn0search1

image_group{"layout":"carousel","aspect_ratio":"16:9","query":["AltTester Unity SDK UI test automation","Unity Editor PlayMode AltTester","AltTester Editor window Unity tests","AltTester AltDriver connecting to Unity"],"num_per_query":1}

또한 **AltTester Unity SDK** 자체는 오픈소스 UI 테스트 자동화 도구로, Unity Hierarchy 안의 오브젝트를 찾아 속성 확인 및 상호작용을 수행하도록 설계되어 있습니다. 기본적으로 **TCP 포트 13000**으로 서버가 실행되며, **AltDriver** 클래스를 통해 테스트 스크립트에서 이 서버에 연결하여 앱 오브젝트를 제어할 수 있습니다. citeturn0search1turn0search2

핵심 사항:
- AltTester는 Unity 프로젝트에 패키지로 설치해 UI 요소에 접근하고 자동으로 테스트 명령을 보낼 수 있도록 합니다. citeturn0search18  
- CLI 옵션으로 **Unity Editor를 -executeMethod** 플래그와 함께 실행해 특정 정적 메서드를 트리거하고 Play Mode에 들어가도록 할 수 있습니다. citeturn0search1  
- AltDriver 인스턴스는 기본적으로 **127.0.0.1:13000** 포트로 연결하며, WSS(보안 WebSocket) 옵션도 지원합니다. citeturn0search2

이 프레임워크는 C#, Python, Java, Robot Framework 등 다양한 언어 테스트를 지원하고, 실제 디바이스나 Unity Editor 내에서도 테스트를 실행할 수 있어 CI 환경에도 잘 맞습니다. citeturn0search1
