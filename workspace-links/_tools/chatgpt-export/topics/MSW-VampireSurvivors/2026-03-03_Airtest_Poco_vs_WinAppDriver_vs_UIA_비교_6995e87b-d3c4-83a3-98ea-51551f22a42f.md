---
type: chatgpt-export-conversation
topic: "MSW-VampireSurvivors"
title: "Airtest/Poco vs WinAppDriver vs UIA 비교"
conversation_id: "6995e87b-d3c4-83a3-98ea-51551f22a42f"
imported_at_utc: "2026-03-03T05:32:13+00:00"
turn_count: 1
chars: 3077
topic_score: 3
---

# Airtest/Poco vs WinAppDriver vs UIA 비교

- topic: `MSW-VampireSurvivors`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/6995e87b-d3c4-83a3-98ea-51551f22a42f_Airtest_Poco_vs_WinAppDriver_vs_UIA.txt`
- conversation_id: `6995e87b-d3c4-83a3-98ea-51551f22a42f`
- matched_keywords: 개발, unity
- card: [[workspace-links/_catalog/cards/MSW-VampireSurvivors|MSW 본편 개발]]

## Summary
## 1. assistant 게임/윈도우 앱 UI 자동화를 처음부터 빠르게 이해하고, 언제 어떤 도구를 쓰면 좋은지 한눈에 정리해드릴게요. --- # 어떤 접근이 가장 안정적일까? - **계층(트리) 기반 탐색 → 가장 견고** 앱이 **UI 계층/접근성 속성**을 노출하면 요소를 ID·이름으로 정확히 찾을 수 있어요. 스크린리더가 쓰는 **Windows UI Automation(UIA)**가 여기에 해당합니다. 자동화 스크립트가 버튼/리스트 같은 “컨트롤 패턴·속성”으로 상호작용할 수 있어 **시각(OCR) 인식보다 훨씬 덜 흔들립니다**. citeturn0search3turn0search11 - **이미지 매칭/OCR →...

## Transcript

## 1. assistant

게임/윈도우 앱 UI 자동화를 처음부터 빠르게 이해하고, 언제 어떤 도구를 쓰면 좋은지 한눈에 정리해드릴게요.  

---

# 어떤 접근이 가장 안정적일까?

- **계층(트리) 기반 탐색 → 가장 견고**  
  앱이 **UI 계층/접근성 속성**을 노출하면 요소를 ID·이름으로 정확히 찾을 수 있어요. 스크린리더가 쓰는 **Windows UI Automation(UIA)**가 여기에 해당합니다. 자동화 스크립트가 버튼/리스트 같은 “컨트롤 패턴·속성”으로 상호작용할 수 있어 **시각(OCR) 인식보다 훨씬 덜 흔들립니다**. citeturn0search3turn0search11

- **이미지 매칭/OCR → 보조(폴백)**  
  화면 픽셀을 템플릿으로 찾는 방식은 UIA/계층이 없을 때 유용하지만, 테마/해상도 변화에 민감합니다.  
  → **권장:** “계층/접근성”을 1순위, 불가 시 “이미지 템플릿”을 **폴백**으로.

---

# 도구 선택 가이드

### 1) 게임/엔진(특히 Unity) 자동화: **Airtest + Poco**
- **Poco SDK**를 게임에 주입하면 런타임의 **UI 계층**을 바로 읽고 element 쿼리가 초고속·안정적으로 됩니다. 필요 시 Airtest의 **이미지 템플릿**을 폴백으로 혼용. citeturn0search13turn0search1turn0search17
- 모두 **오픈소스(Apache-2.0 계열)**라 비용 부담이 적고, Airtest IDE로 녹화/리포트도 지원합니다. citeturn0search0turn0search4

**1줄 PoC 예시 (Unity 게임, 계층+이미지 폴백 혼합):**
```python
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

# 윈도우 타겟 연결(예: 특정 윈도우 핸들/타이틀)
init_device("Windows")  # 필요 시 uuid=<window_handle>

poco = UnityPoco()                  # ← 계층 기반
poco("btn_start").click()           # 1차 시도: 계층 셀렉터
touch(Template("btn_start.png"))    # 폴백: 이미지 템플릿
```
(계층이 잡히면 `poco('btn_start')`, 안 잡히면 `Template('...png')`가 백업.)  
Airtest/Poco 개요 및 Unity 드라이버는 공식 GitHub를 참고하세요. citeturn0search0turn0search13turn0search17

---

### 2) Windows 네이티브 앱(UWP/WPF/WinForms/Win32): **WinAppDriver / Appium Windows Driver**
- **WinAppDriver**는 마이크로소프트가 만든 Windows용 **Selenium/Appium 스타일** 드라이버. UWP·WPF·WinForms·Win32를 지원하고, 내부적으로 **UIA 접근성 트리**를 사용해서 **결정론적**입니다. citeturn0search2
- Appium 환경이라면 **appium-windows-driver**로 WinAppDriver를 프록시처럼 붙여 동일한 테스트 생태계를 재사용할 수 있어요. citeturn0search6

---

# 비용·안정성 스냅샷

- **비용:** 위 도구들은 GitHub 오픈소스(WinAppDriver = MIT)라 **금전 비용은 거의 0**. 다만  
  - 게임 쪽은 **Poco SDK 주입**  
  - Windows 앱은 **자동화 속성(AutomationId 등)** 노출/정비  
  - 이미지 템플릿은 **유지보수(해상도·테마별)**  
  같은 **통합/세팅 시간이 실질 비용**입니다. citeturn0search2turn0search13
- **안정성:** **계층/접근성 기반 > 이미지/OCR 기반**. UIA는 컨트롤 패턴·속성·이벤트로 스크립트 상호작용을 보장(테마/언어 변화에 강함). citeturn0search3turn0search11

---

# 언제 무엇을 쓰나 (결정 트리)

1) **내가 앱을 빌드/수정할 수 있다(게임/Unity 등)**  
→ **Poco SDK 주입 + Airtest** (필요 시 템플릿 폴백) 추천. citeturn0search13

2) **Windows 데스크톱 앱 자동화가 목적**  
→ **WinAppDriver(Appium)**로 **AutomationId/Name 기반** 셀렉터 설계. citeturn0search2turn0search6

3) **둘 다 불가(검은박스·접근성 미노출)**  
→ **Airtest의 이미지 템플릿** 중심으로 시작하되, 가능하면 최소한의 **접근성 속성 노출**을 개발팀에 요청(안정성↑). citeturn0search0

---

# 바로 써먹는 체크리스트

- [ ] **요소 식별자**를 우선: `AutomationId`(Windows) / `name/path`(Poco) 확보. citeturn0search3  
- [ ] 이미지 템플릿은 **DPI/테마/언어**별로 최소 세트 준비(폴백용). citeturn0search0  
- [ ] **레코더/IDE**로 스파이크: Airtest IDE로 첫 스크립트 녹화·리포트 생성. citeturn0search4  
- [ ] CI에서 **WinAppDriver/Appium 세션** 부팅 후 테스트 병렬화. citeturn0search2turn0search6  
- [ ] 실패 케이스 캡처: 스냅샷/DOM 덤프(UIA 트리, Poco 계층) 자동 저장. citeturn0search3turn0search13

---

필요하시면, **당신 프로젝트 화면** 기준으로  
- Poco 주입 지점,  
- WinAppDriver 셀렉터 설계(AutomationId 네이밍 규칙),  
- Airtest 템플릿 폴백 구조(“계층→이미지” 2단계),  
를 **실전 스캐폴딩**까지 한 번에 만들어드릴게요.
