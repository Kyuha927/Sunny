---
type: chatgpt-export-conversation
topic: "Antigravity-CodeTracker"
title: "Game‑Dev AI & Automation Highlights"
conversation_id: "6992993e-3888-83a4-83d1-11ed032715f6"
imported_at_utc: "2026-03-03T05:32:12+00:00"
turn_count: 7
chars: 22924
topic_score: 8
---

# Game‑Dev AI & Automation Highlights

- topic: `Antigravity-CodeTracker`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/6992993e-3888-83a4-83d1-11ed032715f6_Game_Dev_AI_Automation_Highlights.txt`
- conversation_id: `6992993e-3888-83a4-83d1-11ed032715f6`
- matched_keywords: 실행, 로그, 코드, antigravity, log, telemetry
- card: [[workspace-links/_catalog/cards/Antigravity-CodeTracker|실행 로그·코드 추적 허브]]

## Summary
한글로

## Transcript

## 1. assistant

Here’s a **current, high‑level summary of the latest tools, frameworks, trends, and best practices** in automation, AI agents (including Claude Code), and game development workflows across planning, design, and development:

---

## 🎮 1) Industry Adoption & Broader Trends

**AI agents are now widespread in game development.**  
A recent survey found that **about 87–90% of game developers use AI agents** to automate tasks such as playtesting, localization, scripting, and code generation — freeing up time for creative work and reducing overall costs. citeturn0news20turn0news21

Key trends include:  
- Use of AI not just for code generation but also for creative tasks like **level design, dialogue writing, and asset generation**. citeturn0news20  
- Growing adoption in both AAA and indie studios, often as part of CI/CD pipelines or rapid prototyping workflows.

---

## 🤖 2) Claude Code — Agents & Automation

**Claude Code remains a major platform for agent‑driven automation**, especially for coding and orchestration:  

### 🧠 Multi‑Agent Orchestration  
- Claude Code’s **Task Tool** lets you spawn multiple specialized sub‑agents that can work autonomously on different parts of a complex workflow (e.g., generating assets, writing code, or validating results). citeturn0search9  
- Community collections (such as plugin sets with *112+ specialized agents* and orchestration tools) show how modular frameworks are being built for scalable automation workflows. citeturn0search1

### 🛠 Tool Discovery & Efficient Workflows  
- Claude now supports **on‑demand tool discovery and dynamic invocation** rather than preloading everything upfront — making large tool libraries manageable and efficient. citeturn0search3  
- There are community‑built skills (e.g., for **browser automation**) to help agents interact more reliably with the web as part of automation pipelines. citeturn0search13

### 🌐 Accessibility Improvements  
- Anthropic expanded Claude Code to a **web‑based interface** (beyond CLI), simplifying agent creation and management for all developers with a Pro/Max subscription. citeturn0news28

---

## 🛠 3) Game Dev Tools with Integrated AI Automation

### Unity & AI
- **Unity AI** is pushing deeper in‑editor automation: generating placeholders, assets, contextual assistance, bulk modifications, debug help, and even code generation directly within the editor. citeturn0search6

### AI Assistants & Plugins
- Tools like **Bezi** act as AI assistants for developers building in Unity — automating debugging, code generation tailored to your project, and repetitive task creation. citeturn0search14

### Asset & Content Automation
- External solutions such as **Tencent’s VISVISE** aim to automate art pipelines (e.g., skinning, animation) to cut generation time from weeks to minutes. citeturn0search19

### Emerging Frameworks in Research
- Academic frameworks show **multi‑agent AI systems** that interpret design docs and generate full game prototypes (e.g., UniGen and other LLM‑driven game generation systems). citeturn0academia24turn0academia26

---

## 📈 4) Best Practices & Workflow Automation

**Key industry practices emerging include:**

✅ **Parallel agent workflows:** Use multiple agents to handle different roles (planning, coding, debugging) in parallel rather than serial single‑agent interactions. citeturn0search9  
✅ **Incremental automation adoption:** Start with automating repetitive tasks (QA, testing, asset batching) and expand toward more complex workflows. citeturn0news20  
✅ **Tool orchestration platforms:** Platforms that help you *manage, monitor, and compare* agents (e.g., GitHub’s new “Agent HQ” which integrates multiple coding agents under one control plane) are emerging. citeturn0news17  
✅ **Human‑in‑the‑loop supervision:** While AI speeds creation, expert oversight still improves quality — especially for design decisions, narrative coherence, and player experience.

---

## 🧩 5) Broader Automation Ecosystems

Beyond game‑specific tooling:

- **Google Antigravity** is another AI agent ecosystem focused on IDE workflows, enabling agent‑side task management, both in editor and background orchestration. citeturn0search23  
- Agent‑oriented tools with no‑code interfaces (similar in spirit to Claude Code’s plugins) are growing, making automation accessible even to non‑developers.

---

## 📌 Summary — What Matters Today

**The direction of automation & game dev workflows is clear:**

- AI agents are becoming core parts of the development process — from planning to final testing. citeturn0news20  
- Modular, orchestrated agent frameworks (like Claude Code with task spawning and plugin ecosystems) make complex workflows manageable. citeturn0search1  
- In‑editor AI tools (Unity AI, Bezi, etc.) automate tasks in the context where developers are already working. citeturn0search6  
- Research and emerging tools are pushing toward **end‑to‑end game automation** (even prototype generation from design docs). citeturn0academia24

---

If you want an **actionable developer stack** (e.g., Claude Code workflows, Unity AI integrations, agent orchestration examples), I can structure a practical setup next — just let me know.

## 2. user

한글로

## 3. assistant

좋아요 👍 위에서 정리한 **자동화·에이전트·게임개발 트렌드** 내용을 한국어로 다시 정리해드릴게요.

---

# 🎮 1) 게임 업계의 AI 에이전트 활용 현황

현재 **대부분의 게임 개발자들이 AI 에이전트를 실제 업무에 사용**하고 있습니다.  
활용 영역은 다음과 같습니다:

- 자동 플레이테스트
- 스크립트/코드 생성
- 반복 작업 자동화
- 로컬라이징(번역)
- 레벨 디자인 보조
- 대사 작성 및 스토리 초안
- 에셋 생성

👉 단순 코드 보조 수준을 넘어 **기획–제작–QA 전 과정에 통합**되는 흐름입니다.

---

# 🤖 2) Claude Code 기반 에이전트 자동화

## 🧠 멀티 에이전트 오케스트레이션
- Task Tool을 통해 **여러 개의 전문 에이전트를 병렬 실행**
- 예:
  - 기획 분석 에이전트
  - 코드 생성 에이전트
  - 테스트 자동화 에이전트
  - 결과 검증 에이전트

복잡한 워크플로우를 **역할 분담 구조**로 설계하는 것이 최신 트렌드입니다.

---

## 🛠 도구 동적 호출
- 모든 툴을 미리 불러오는 방식이 아니라
- 필요한 순간에만 툴을 탐색하고 실행

→ 대규모 플러그인 환경에서도 효율적인 자동화 가능

---

## 🌐 접근성 확장
- CLI 중심에서 웹 인터페이스 확장
- 에이전트 설정 및 실행이 더 쉬워짐
- 비개발자도 워크플로우 설계 가능

---

# 🛠 3) 게임 엔진 + AI 자동화 통합

## 🎯 Unity AI
- 에디터 내부에서:
  - 코드 생성
  - 디버그 보조
  - 대량 수정 자동화
  - 임시 에셋 생성
  - 맥락 기반 도움

👉 개발자가 작업하는 “같은 공간” 안에서 AI가 동작하는 것이 핵심

---

## 🎨 아트 파이프라인 자동화
- 스킨/애니메이션 자동 생성
- 텍스처 변형
- 스타일 일괄 적용
- AI 기반 리타게팅

기존 수 주 걸리던 작업이 **수 분~수 시간 단위로 단축**

---

# 📈 4) 최신 베스트 프랙티스

### ✅ 병렬 에이전트 구조
단일 에이전트에 모든 걸 맡기지 말 것  
→ 역할별 분리 + 결과 통합

### ✅ 점진적 자동화 도입
처음부터 전체 자동화 ❌  
반복 작업부터 단계적 적용 ✔

### ✅ Human-in-the-loop
AI는 가속기, 최종 품질 책임은 인간  
특히:
- 밸런싱
- 내러티브 일관성
- 플레이 경험

---

# 🧩 5) 연구·차세대 방향

- 디자인 문서 → 자동 프로토타입 생성
- LLM 기반 게임 생성 프레임워크
- 에이전트 협업형 게임 제작
- IDE 내 상시 AI 코파일럿화

---

# 🔥 지금 가장 중요한 포인트

1. AI는 보조 도구가 아니라 **워크플로우 구성 요소**
2. 멀티 에이전트 설계 능력이 경쟁력
3. 자동화는 "속도"가 아니라 **실험 반복 횟수 증가**가 핵심 가치
4. 인간의 감각과 판단은 여전히 필수

---

김지훈님처럼 **픽셀아트 + 보스 캐릭터 설계 + 반복 생성 작업**을 많이 하시는 경우라면:

- 🎨 프롬프트 자동 변형 에이전트
- 🧠 스타일 일관성 체크 에이전트
- 📦 스프라이트 시트 정렬 자동화
- 🧪 애니메이션 루프 검증 에이전트

이런 구조로 가면 생산성이 크게 올라갑니다.

---

원하시면 다음 중 하나를 구체적으로 만들어드릴 수 있어요:

1️⃣ Claude Code 기반 게임 제작 자동화 구조 설계  
2️⃣ Unity + AI 에이전트 실전 세팅 가이드  
3️⃣ 픽셀아트 제작 자동화 파이프라인 설계  
4️⃣ 1인 개발자를 위한 AI 멀티에이전트 템플릿  

어느 쪽으로 깊게 들어가볼까요?

## 4. user

레벨디자인보조 및 각 파트 더 깊게

## 5. assistant

좋아요 👍  
**레벨 디자인 보조 AI + 각 파트 심화 구조**를 실전 개발 관점에서 깊게 정리해드릴게요.  
(특히 김지훈님처럼 2D 픽셀 액션/보스 중심 게임을 만드는 상황에 맞춰 설명합니다.)

---

# 🎮 1️⃣ 레벨 디자인 AI 보조 — 구조적으로 이해하기

레벨 디자인에서 AI는 크게 **4단계**로 나뉩니다:

1. 구조 설계
2. 플레이 리듬 설계
3. 배치 자동화
4. 플레이 테스트 및 수정 제안

---

## 🧠 A. 구조 설계 (Macro Layout Design)

### 🔹 역할
- 맵 전체 흐름 생성
- 시작–중반–클라이맥스–보스 구간 설계
- 난이도 곡선 생성

### 🔹 AI 활용 방식
- 텍스트 기반 구조 생성
- 그래프 기반 레벨 구조 생성
- 타일맵 블록 초안 자동 생성

### 🔹 예시 프롬프트 구조
```
2D 사이드스크롤 액션 게임
테마: 디젤펑크 산업 도시
플레이 시간: 8~10분
보스 전 진입 긴장감 상승
플레이어 능력: 점프, 대시, 근접 공격
```

→ AI 출력:
- 5구간 구조 제안
- 중간 미니보스 위치
- 적 밀도 변화
- 함정 배치 패턴

---

## 📈 B. 플레이 리듬 설계 (Flow & Pacing AI)

이 부분이 가장 중요합니다.

### 🔹 분석 대상
- 점프 간격
- 전투 밀도
- 회복 아이템 간격
- 안전 구간 길이

### 🔹 AI가 잘하는 것
- “지루한 구간” 탐지
- 과도한 적 밀집 경고
- 리듬 반복 감지

예:
- 40초 이상 긴장 없는 구간 → 긴장 이벤트 추가 제안
- 적 6연속 배치 → 피로도 경고

---

## 📦 C. 오브젝트 자동 배치

AI를 이용한:
- 적 스폰 위치 자동 추천
- 함정 간격 자동 최적화
- 시야 기반 배치 분석

### 🔹 고급 방식
- 플레이어 이동 속도 기반 간격 계산
- 반응 시간 기반 함정 거리 계산
- 시야에 동시에 보이는 위협 개수 제한

---

## 🧪 D. 플레이 테스트 AI (시뮬레이션 에이전트)

이게 진짜 강력합니다.

### 🔹 방식
- AI 봇이 레벨 반복 플레이
- 평균 클리어 시간 계산
- 사망 위치 히트맵 생성
- 점프 실패 구간 분석

→ 인간 QA 이전에 1차 자동 검증 가능

---

# 🤖 2️⃣ 멀티 에이전트 구조 (Claude Code 스타일)

레벨 디자인을 하나의 AI에게 맡기면 안 됩니다.

## 🧩 권장 구조

### 🎯 1. Macro Designer Agent
- 레벨 전체 구조 설계
- 테마 반영
- 난이도 곡선 설계

### ⚔ 2. Encounter Designer Agent
- 전투 이벤트 설계
- 적 조합 구성
- 패턴 다양성 확보

### 🧠 3. Flow Analyzer Agent
- 플레이 리듬 분석
- 반복성 감지
- 난이도 급상승 감지

### 🧪 4. Simulation Agent
- 자동 플레이
- 히트맵 생성
- 실패 지점 분석

### 🧹 5. Optimization Agent
- 오브젝트 밀도 조정
- CPU 부하 감소 제안
- 충돌 박스 최적화

---

# 🎨 3️⃣ 픽셀 2D 액션 특화 전략

김지훈님 스타일 (보스 중심 2D 액션)이라면:

## 🔥 보스 진입 전 설계 자동화

AI가 다음을 체크:

- 플레이어 체력 소모율
- 최근 2분간 긴장도
- 보스 직전 회복 아이템 위치
- 공간 크기 대비 회피 동선 확보

---

## ⚙ 플랫폼 간격 계산 자동화

AI가:
- 점프 최대 거리 계산
- 대시 포함 이동 거리 계산
- 평균 반응 속도 기반 안전 마진 계산

→ “불합리한 점프” 제거 가능

---

# 📊 4️⃣ 고급: 데이터 기반 학습

레벨 로그 데이터를 모으면:

- 사망 위치 클러스터 분석
- 특정 적 조합의 이탈률 분석
- 플레이어 평균 체력 곡선 생성

이걸 기반으로:

> “난이도는 높지만 공정한지” 판단 가능

---

# 🚀 5️⃣ 실제 적용 구조 예시

### 🔧 Unity 환경 기준

1. 레벨 JSON 추출
2. AI 에이전트 분석
3. 수정 제안 JSON 생성
4. 에디터 자동 적용

---

# 💡 6️⃣ 더 깊은 영역 (연구급)

- 플레이어 유형별 레벨 자동 변형
  - 공격적 플레이어
  - 탐험형 플레이어
- 실시간 적응형 레벨
- AI가 다음 구간을 즉석 생성

---

# 🔥 핵심 정리

레벨 디자인 AI는:

- “자동 생성”이 목적이 아니라
- “밸런스 감지 + 리듬 최적화”가 핵심

---

원하시면 다음 중 하나를 아주 구체적으로 설계해 드릴게요:

1️⃣ Unity용 레벨 분석 에이전트 구조 코드 설계  
2️⃣ 2D 보스 중심 액션용 레벨 리듬 공식 정리  
3️⃣ 멀티에이전트 실제 프롬프트 템플릿 제작  
4️⃣ 레벨 자동 QA 시스템 설계  

어느 단계까지 파볼까요?

## 6. user

1,2,3,4 모두

## 7. assistant

좋습니다. 아래는 **1) Unity용 레벨 분석 에이전트 구조(코드 포함)**, **2) 2D 보스 중심 액션 레벨 리듬 공식**, **3) 멀티에이전트 프롬프트 템플릿**, **4) 레벨 자동 QA 시스템 설계**를 한 번에 “바로 써먹을 수 있게” 묶은 실전 패키지입니다.

---

# 1) Unity용 레벨 분석 에이전트 구조 + 코드 설계

## 1-1. 데이터 흐름(가장 현실적인 형태)
Unity 에디터에서 **레벨을 JSON으로 추출 → AI(Claude Code/에이전트) 분석 → “패치 JSON”으로 수정안 생성 → Unity가 자동 적용**.

- `LevelExport.json` : 현재 레벨(타일/오브젝트/스폰/트리거) 스냅샷
- `LevelPatch.json` : AI가 제안한 변경사항(추가/삭제/이동/파라미터 수정)
- Unity Editor Tool : Export / Import / Patch Apply 버튼 제공

## 1-2. 최소 스키마(확장 가능한 형태)
### LevelExport.json 예시(핵심만)
```json
{
  "meta": { "levelId": "L01", "theme": "dieselpunk_factory", "units": "tiles" },
  "player": { "speed": 6.5, "jumpHeight": 3.2, "dashDistance": 4.0 },
  "segments": [
    { "id": "S1", "x0": 0, "x1": 180, "tag": "intro" },
    { "id": "S2", "x0": 180, "x1": 420, "tag": "combat" },
    { "id": "S3", "x0": 420, "x1": 640, "tag": "platform" },
    { "id": "S4", "x0": 640, "x1": 760, "tag": "preboss" },
    { "id": "S5", "x0": 760, "x1": 900, "tag": "boss" }
  ],
  "objects": [
    { "id": "E_01", "type": "enemy_grunt", "pos": [210, 3], "params": { "patrol": 6 } },
    { "id": "T_02", "type": "trap_spike", "pos": [505, 2], "params": { "damage": 1 } },
    { "id": "P_07", "type": "platform_moving", "pos": [560, 5], "params": { "range": 4, "speed": 1.2 } },
    { "id": "H_01", "type": "heal_pickup", "pos": [710, 3], "params": { "amount": 2 } }
  ],
  "nav": {
    "jumpLinks": [
      { "from": [520, 2], "to": [545, 5], "required": { "jump": 3.0 } }
    ]
  }
}
```

### LevelPatch.json 예시
```json
{
  "levelId": "L01",
  "actions": [
    { "op": "move", "id": "H_01", "pos": [735, 3] },
    { "op": "add", "newId": "C_01", "type": "checkpoint", "pos": [740, 3], "params": {} },
    { "op": "tune", "id": "P_07", "params": { "speed": 1.0 } },
    { "op": "add", "newId": "E_12", "type": "enemy_shooter", "pos": [612, 4], "params": { "fireRate": 0.8 } }
  ],
  "notes": [
    "보스 진입 직전 회복/체크포인트를 시야에 보이게 재배치",
    "플랫폼 속도를 낮춰 점프 실패율 감소"
  ]
}
```

## 1-3. Unity Editor 코드(Export/Import/Apply)
> 아래 코드는 **“오브젝트에 LevelEntity 컴포넌트가 붙어 있다”**는 전제의 가장 단순한 버전입니다. (실전에서는 Addressables/Tilemap도 확장 가능)

### (A) LevelEntity.cs
```csharp
using UnityEngine;

public class LevelEntity : MonoBehaviour
{
    public string id;       // "E_01" 등 유니크
    public string type;     // "enemy_grunt" 등
    [TextArea] public string jsonParams; // 간단히 JSON string으로 보관(확장 여지)

    public Vector2 Pos2D => new Vector2(transform.position.x, transform.position.y);
}
```

### (B) LevelIOModels.cs
```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

[Serializable]
public class LevelExport
{
    public Meta meta;
    public PlayerSpec player;
    public List<Segment> segments = new();
    public List<Obj> objects = new();
}

[Serializable] public class Meta { public string levelId; public string theme; public string units; }
[Serializable] public class PlayerSpec { public float speed; public float jumpHeight; public float dashDistance; }
[Serializable] public class Segment { public string id; public float x0; public float x1; public string tag; }

[Serializable]
public class Obj
{
    public string id;
    public string type;
    public float[] pos;
    public string paramsJson;
}

[Serializable]
public class LevelPatch
{
    public string levelId;
    public List<PatchAction> actions = new();
    public List<string> notes = new();
}

[Serializable]
public class PatchAction
{
    public string op;      // add/move/remove/tune
    public string id;      // existing id
    public string newId;   // for add
    public string type;    // for add
    public float[] pos;    // for add/move
    public string paramsJson; // for tune/add
}
```

### (C) LevelExporterWindow.cs (Editor)
```csharp
#if UNITY_EDITOR
using UnityEditor;
using UnityEngine;
using System.IO;
using System.Linq;

public class LevelExporterWindow : EditorWindow
{
    private string exportPath = "Assets/LevelExport.json";
    private string patchPath  = "Assets/LevelPatch.json";

    [MenuItem("Tools/Level/AI Export & Patch")]
    public static void Open() => GetWindow<LevelExporterWindow>("Level AI Tool");

    void OnGUI()
    {
        GUILayout.Label("Export / Patch", EditorStyles.boldLabel);
        exportPath = EditorGUILayout.TextField("Export JSON Path", exportPath);
        patchPath  = EditorGUILayout.TextField("Patch JSON Path", patchPath);

        if (GUILayout.Button("1) Export LevelExport.json")) Export();
        if (GUILayout.Button("2) Apply LevelPatch.json")) ApplyPatch();
    }

    void Export()
    {
        var entities = FindObjectsOfType<LevelEntity>();
        var exp = new LevelExport
        {
            meta = new Meta { levelId = "L01", theme = "dieselpunk_factory", units = "tiles" },
            player = new PlayerSpec { speed = 6.5f, jumpHeight = 3.2f, dashDistance = 4.0f }
        };

        foreach (var e in entities.OrderBy(x => x.id))
        {
            exp.objects.Add(new Obj
            {
                id = e.id,
                type = e.type,
                pos = new float[] { e.transform.position.x, e.transform.position.y },
                paramsJson = string.IsNullOrWhiteSpace(e.jsonParams) ? "{}" : e.jsonParams
            });
        }

        var json = JsonUtility.ToJson(exp, true);
        File.WriteAllText(exportPath, json);
        AssetDatabase.Refresh();
        Debug.Log($"Exported: {exportPath} (objects: {exp.objects.Count})");
    }

    void ApplyPatch()
    {
        if (!File.Exists(patchPath))
        {
            Debug.LogError($"Patch not found: {patchPath}");
            return;
        }

        var json = File.ReadAllText(patchPath);
        var patch = JsonUtility.FromJson<LevelPatch>(json);
        var entities = FindObjectsOfType<LevelEntity>().ToDictionary(x => x.id, x => x);

        foreach (var a in patch.actions)
        {
            if (a.op == "move" && entities.TryGetValue(a.id, out var ent))
            {
                Undo.RecordObject(ent.transform, "Move Entity");
                ent.transform.position = new Vector3(a.pos[0], a.pos[1], ent.transform.position.z);
            }
            else if (a.op == "tune" && entities.TryGetValue(a.id, out var ent2))
            {
                Undo.RecordObject(ent2, "Tune Entity");
                ent2.jsonParams = string.IsNullOrWhiteSpace(a.paramsJson) ? ent2.jsonParams : a.paramsJson;
                EditorUtility.SetDirty(ent2);
            }
            else if (a.op == "add")
            {
                var go = new GameObject(a.newId);
                Undo.RegisterCreatedObjectUndo(go, "Add Entity");
                go.transform.position = new Vector3(a.pos[0], a.pos[1], 0);
                var le = go.AddComponent<LevelEntity>();
                le.id = a.newId;
                le.type = a.type;
                le.jsonParams = string.IsNullOrWhiteSpace(a.paramsJson) ? "{}" : a.paramsJson;
            }
            else if (a.op == "remove" && entities.TryGetValue(a.id, out var ent3))
            {
                Undo.DestroyObjectImmediate(ent3.gameObject);
            }
        }

        Debug.Log($"Applied Patch: {patchPath}\n- Notes: {string.Join(" | ", patch.notes)}");
    }
}
#endif
```

✅ 여기까지 하면 “AI가 제안한 변경사항을 Unity가 자동 반영”까지 됩니다.  
다음 단계(4번 QA)에서 **로그 기반 히트맵/사망지점**까지 붙이면 완전체입니다.

---

# 2) 2D 보스 중심 액션용 레벨 리듬 공식(실전 지표)

레벨 리듬은 감각처럼 보이지만, 실제로는 **지표화**하면 자동화가 됩니다.

## 2-1. 핵심 5지표(보스 전개용)
### (1) 긴장도 밀도 Tension Density (TD)
- 단위 시간(예: 10초) 내 위협 이벤트 수
- 위협 이벤트 = 적 조우/탄막/함정/낙사 위험/시간 압박/시야 제한

**권장 패턴(보스 레벨):**
- Intro TD 낮음 → Mid TD 중간 → Preboss TD 최고 → Boss는 패턴으로 변조

### (2) 회복 간격 Recovery Gap (RG)
- “플레이어가 숨 돌리는 안전 구간” 사이의 평균 시간
- 액션 게임에서 RG가 너무 길면 피로, 너무 짧으면 긴장 저하

**보스 직전 권장:**
- 보스 30~60초 전: **RG 짧게**(안도감) + “보스 문 연출”로 다시 긴장 전환

### (3) 실패 비용 Fail Cost (FC)
- 사망 후 되돌아가야 하는 거리/시간/재수행 전투량

**권장:**
- 보스 직전 FC는 낮게(체크포인트/짧은 복귀)
- “연습 반복”이 핵심이므로 보스 문 앞 FC를 줄여야 재도전이 즐겁습니다.

### (4) 학습-검증 루프 Learn/Verify Loop (LV)
- 새로운 기믹이 나오면:
  - **학습(Learn)**: 안전하게 한 번 보여줌
  - **검증(Verify)**: 변형해서 시험함
  - **혼합(Mix)**: 이전 요소와 섞음

**룰:**
- 새 기믹을 처음부터 “즉사급”으로 주면 불공정함으로 인식

### (5) 시야 위협 동시성 On-Screen Threat Concurrency (OTC)
- 화면에 동시에 존재하는 “의미 있는 위협” 개수
- 2D 픽셀 액션에서 가독성 핵심

**권장:**
- 일반 구간 OTC 1~3
- 클라이맥스(프리보스) OTC 3~5 (짧게)
- 보스는 패턴 단계별로 OTC를 변조(페이즈 전환 시 리셋)

---

## 2-2. 플랫폼/점프 공정성 공식(실무용)
플레이어 스펙이 있을 때 “불합리 점프”를 자동 탐지하는 기준입니다.

### 안전 점프 거리(가로) SafetyJumpX
- 대략: `SafetyJumpX = MaxJumpX * 0.85`
- 대시 점프가 있으면 별도:
  - `SafetyDashJumpX = (MaxJumpX + DashDistance) * 0.85`

### 반응 시간 기반 함정 간격 TrapSpacing
- 플레이어 속도 `v`(타일/초), 평균 반응 `r`(초, 0.25~0.35 추천)
- `minSpacing = v * r + margin`
- margin은 1~2 타일(픽셀게임은 가독성 때문에 더 줌)

### “보스 직전 공정성” 룰
- 보스 문 20초 전에는 **즉사 함정/낙사/랜덤 요소를 줄이고**
- 대신 **전투 압박(하지만 공정한)** 으로 긴장도를 만들면 플레이어가 납득합니다.

---

# 3) 멀티 에이전트 프롬프트 템플릿(Claude Code 스타일)

아래 템플릿은 “한 에이전트가 다 하는” 게 아니라, **역할 분업 + 합의** 구조입니다.

## 3-1. 공통 시스템 프롬프트(모든 에이전트에 동일하게)
- 출력은 반드시 `LevelPatch.json` 형식(또는 별도 리포트)
- “근거 지표”를 notes에 넣기
- 변경은 “최소 수정” 우선(레벨 정체성 유지)

---

## 3-2. Macro Designer Agent (구조/곡선 담당)
**입력:** LevelExport.json  
**출력:** 구조 제안 리포트 + 큰 변경 1~3개만

**프롬프트**
- 목표: 8~10분 레벨, 테마 유지, 구간 태깅(인트로/전투/플랫폼/프리보스/보스)
- 산출: 세그먼트 조정, 체크포인트 위치 추천, 연출 트리거 추천

**출력 포맷(요약 + Patch 초안)**
- 변경 이유(난이도 곡선/리듬)
- Patch actions(큰 수정만)

---

## 3-3. Encounter Designer Agent (전투 설계)
**프롬프트 핵심 룰**
- 같은 적 조합 2회 이상 반복 금지(변형 필수)
- 화면 위협 동시성(OTC) 목표값 준수
- 회복 아이템 직후에는 “가벼운” 전투로 워밍업

**산출물**
- 적 배치 추가/삭제/조정 Patch
- notes에 “OTC 추정치 / 전투 강도” 기록

---

## 3-4. Flow Analyzer Agent (리듬/가독성)
**목표**
- TD, RG, FC, LV, OTC를 계산(정확 수치가 아니어도 상대 비교)
- 지루 구간/피로 구간/불공정 구간 탐지

**산출물**
- “문제 구간 Top 5”
- 각 문제 구간별 최소 수정안(오브젝트 1~3개 조정 수준)

---

## 3-5. Simulation Agent (자동 플레이/로그 분석과 결합)
**입력**
- 플레이 로그 요약(사망 좌표, 클리어 시간, 피해량 등)
- LevelExport.json

**산출**
- 사망 히트맵 클러스터별 원인 가설
- 해당 클러스터 주변 수정 Patch

---

## 3-6. Integrator Agent (최종 합의/충돌 해결)
**역할**
- 여러 에이전트 Patch가 충돌하면:
  - “보스 직전 공정성” 우선
  - “최소 수정” 우선
  - 성능/가독성 우선

**최종 출력**
- 단일 `LevelPatch.json`
- notes에 “어떤 제안을 왜 버렸는지” 짧게 기록

---

# 4) 레벨 자동 QA 시스템 설계(실전 구현 플로우)

## 4-1. 자동 QA가 뽑아야 하는 로그(최소)
플레이 테스트(사람/봇)에서 다음을 남기면 AI 분석이 훨씬 정확해집니다.

- `timeToClear`(초)
- `deaths[]`: (x,y, time, cause)
- `damageTaken[]`: (x,y, amount, source)
- `checkpointTimes[]`
- `jumpFails[]`: (from,to, time)  ← 플랫폼 공정성에 직결
- `inputIntensity`(대시/점프/공격 빈도)  ← 피로도 근사치

## 4-2. Unity에 로그 쌓기(간단 구현)
### (A) GameplayTelemetry.cs (런타임)
```csharp
using System;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

[Serializable]
public class TelemetryRun
{
    public string levelId;
    public float timeToClear;
    public List<DeathEvent> deaths = new();
    public List<DamageEvent> damages = new();
    public List<JumpFailEvent> jumpFails = new();
}

[Serializable] public class DeathEvent { public float t; public float x; public float y; public string cause; }
[Serializable] public class DamageEvent { public float t; public float x; public float y; public int amount; public string source; }
[Serializable] public class JumpFailEvent { public float t; public float fx; public float fy; public float tx; public float ty; }

public class GameplayTelemetry : MonoBehaviour
{
    public static GameplayTelemetry I;
    public string levelId = "L01";
    private TelemetryRun run;
    private float startTime;

    void Awake()
    {
        I = this;
        run = new TelemetryRun { levelId = levelId };
        startTime = Time.time;
    }

    public void LogDeath(Vector2 pos, string cause)
    {
        run.deaths.Add(new DeathEvent { t = Time.time - startTime, x = pos.x, y = pos.y, cause = cause });
    }

    public void LogDamage(Vector2 pos, int amount, string source)
    {
        run.damages.Add(new DamageEvent { t = Time.time - startTime, x = pos.x, y = pos.y, amount = amount, source = source });
    }

    public void LogJumpFail(Vector2 from, Vector2 to)
    {
        run.jumpFails.Add(new JumpFailEvent { t = Time.time - startTime, fx = from.x, fy = from.y, tx = to.x, ty = to.y });
    }

    public void LogClear()
    {
        run.timeToClear = Time.time - startTime;
        Save();
    }

    void Save()
    {
        var json = JsonUtility.ToJson(run, true);
        var path = Path.Combine(Application.persistentDataPath, $"telemetry_{levelId}_{DateTime.Now:yyyyMMdd_HHmmss}.json");
        File.WriteAllText(path, json);
        Debug.Log($"Telemetry saved: {path}");
    }
}
```

## 4-3. 자동 QA 분석 파이프라인(운영 방식)
1) 하루/빌드마다 텔레메트리 JSON 모음  
2) 간단한 전처리(클러스터링: “사망이 몰린 좌표들”)  
3) AI에게 “클러스터 + 주변 오브젝트 목록”을 함께 전달  
4) AI가 원인 가설 + Patch 생성  
5) Unity가 자동 적용  
6) 다음 빌드에서 지표 개선 확인 (사망률/클리어타임/피해량)

## 4-4. 판정 룰(자동 Fail/Pass)
- 보스 직전 구간(Preboss)에서:
  - 사망이 전체의 40% 이상이면 **FAIL**
  - 체크포인트 복귀 시간이 15초 넘으면 **FAIL**
- 점프 실패 특정 링크가 전체 점프 실패의 25% 이상이면 **FAIL**
- 클리어 시간 분산이 지나치게 크면(숙련도 양극화) 해당 구간 리듬 재검토

---

# 바로 적용 “최소 셋업” 체크리스트
- [ ] LevelEntity를 모든 배치 오브젝트에 붙임(id/type/jsonParams)
- [ ] EditorWindow로 Export/Patch Apply 동작 확인
- [ ] GameplayTelemetry로 death/damage/jumpfail 로그 저장
- [ ] AI 멀티에이전트 템플릿대로 Patch 생성/통합
- [ ] Patch 적용 후 플레이 테스트 → 지표 개선 확인

---

## 다음 액션(질문 없이 바로 제안)
김지훈님 작업 흐름에 맞춰 제일 효율적인 진행은 이겁니다:

1) 지금 쓰는 레벨(샘플 1개)을 `LevelExport.json`으로 뽑기  
2) 텔레메트리 10회치만 모으기(사람 플레이 5 + 간단 봇 5도 OK)  
3) 내가 위 템플릿으로 **Patch 1차**를 만들어주는 구조로 돌리기

원하시면, 다음 메시지에 **현재 레벨의 LevelExport.json(또는 스크린샷/오브젝트 리스트)** 를 붙여주시면  
제가 “Macro/Encounter/Flow/Sim/Integrator” 관점으로 **실제 LevelPatch.json** 형태로 바로 만들어드릴게요.
