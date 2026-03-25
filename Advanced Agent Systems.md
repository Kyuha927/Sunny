---
tags: [AI, Agent, Research, Architecture]
aliases: [Advanced Agent Systems, 에이전트 아키텍처]
date: 2026-03-22
---

# 🤖 Advanced Agent Systems (차세대 에이전트 시스템 로드맵)

더 나은 에이전트 시스템을 구축하고 발전시키는 것은 현재 개발 중인 모든 자동화 프로젝트(미연시 생성, 픽셀 에이전트 등)를 관통하는 **가장 중요한 핵심 과제**이다. 이 문서는 최신 프레임워크 리서치, 아키텍처 패턴, 그리고 실제 구현 결과를 추적하는 척도(SSOT)로 활용한다.

## 🎯 핵심 발전 방향 (Core Directives)
1. **Contamination-Free Handoff (무오염 인계)**: 에이전트가 단일 세션에서 긴 문맥을 유지하며 삽질하는 것을 막고, 가장 작은 다음 단계(Smallest Next Step)를 도출한 뒤 깨끗한 환경(Fresh Session)으로 작업을 이관하는 시스템 확립 (Codex 모델 참고).
2. **Hybrid Automation (하이브리드 자동화)**: LLM의 추론 병목을 순수 코드로 대체. `browser-use` 기반의 빠른 DOM 액션과 `PydanticAI/TheAgenticBrowser` 기반의 에러 검수(Critique) 파트를 결합하여 속도와 안정성의 시너지를 창출.
3. **Multi-Agent Orchestration**: 역할을 쪼갠 다중 에이전트(`docs_researcher`, `worker`, `critique` 등)가 백그라운드에서 병렬 동작할 수 있도록 권한과 통신 프로토콜 정립.

## 📚 최근 리서치 & 프레임워크 스택 (Tech Stack tracker)

### 웹 자동화 (Web Automation)
- **browser-use (Python)**: 현재 가장 실용적인 시각+DOM 기반 웹 오토메이션. 캡챠 우회 및 동적 페이지 조작에 특화.
- **TheAgenticBrowser**: `Planner -> Executor -> Critique`의 3-에이전트 자가 피드백 루프 아키텍처. 이 중 `Critique(검수)` 패턴을 하이브리드 루프에 주입하는 연구 진행 중.
- **Alibaba OpenClaw / Qwen-Agent**: 데스크탑(로컬)과 웹 환경을 동시에 묶는 중앙 통제자 모델.

### 멀티에이전트 오케스트레이션 프레임워크 (Multi-Agent Orchestration)

| 프레임워크 | 추출한 핵심 장점 | 우리에게 쓸모 |
|---|---|---|
| **CrewAI** | 역할(Role) 기반 자율 위임 + `Memory` 시스템(세션 간 기억 유지) + LangChain 제거로 독립 경량화 + **배포 속도 LangGraph 대비 40% 빠름** | 미연시 자동화에서 `프롬프트 작성자 → 영상 생성자 → 검수자` 역할 분리에 적합 |
| **LangGraph** | 그래프 기반 **상태 머신**(State Machine): 자동 체크포인트 + 크래시 후 자동 복구(Resume) + Human-in-the-Loop 일시정지/승인 루프 내장 | Kling 파이프라인의 `대기 → 완료 → 다운로드` 상태 흐름 관리에 최적. v2.0 (2026 Q2) 예정 |
| **AutoGen (MS)** | `Writer ↔ Critic` 자기 반성(Self-Reflection) 루프: 에이전트가 자기 산출물을 자체 검증 후 수정하는 반복 + 비동기 이벤트 드리븐 아키텍처 | 영상 프롬프트 품질을 올리는 자동 정제(Refinement) 파이프라인에 결합 가능 |
| **MetaGPT** | 소프트웨어 회사 시뮬레이션(PM → 아키텍트 → 엔지니어) + **SOP(표준운영절차)를 프롬프트로 인코딩** → 에이전트 간 구조화된 소통 + 한 줄 요구사항으로 전체 프로젝트 산출 | 픽셀 에이전트 같은 대규모 코드베이스 리팩토링을 자동 기획/분배하는 데 참고할 아키텍처 |

### 인프라 & CLI
- **Codex CLI**: 터미널 기반 다이렉트 에이전트, 백그라운드 병렬 파일 서치 및 시스템 Handoff 구조의 롤모델.
- **Claude Code CLI**: 고도화된 컨텍스트 조망 능력과 대규모 코드베이스 리팩토링 특화. Codex CLI와 상호 보완적인 강력한 3각 편대(GUI-Codex-Claude Code) 구성의 핵심 아키텍트.

## 📅 Action Logs & 디벨롭 노트 (Changelog)
- **2026-03-23**: Claude Code CLI를 공식 스택에 편입하여 `STUDIO.md` 단일화 구조를 보완하는 `/claude-delegation` 기반 3각 워크플로우 제정 완료.
- **2026-03-22**: Antigravity 내에 수동 Handoff 시스템을 글로벌 룰로 구축 완료. 
- **2026-03-22**: 미연시 컷신 무인 자동화를 위한 Hybrid Factory (browser-use 액션 + 순수 파이썬 모니터 대기 + AI 기반 검수) 설계도 초안 완성.
- **2026-03-22 (Troubleshooting)**: Antigravity "무한 Running" 상태 돌파 및 자가 치유(Self-Healing)를 위한 3중 복구 체계(JS/Extension/Manual) 문서화 완료.

---

### 🛡️ [부록] Antigravity 무한 로딩(Running) 방지 3중 복구 체계

에이전트가 30초 이상 명령을 반환하지 않고 멈췄을 때의 실용적 탈출 가이드.

1. **Auto Retry/Sync 익스텐션 (Open VSX `mrd9999.antigravity-sync`)**
   - CDP 통신을 통해 모니터링하다가 멈춤 감지 시 재시작 취소 신호를 날려주는 공식 워크어라운드.

2. **DIY 브라우저 콘솔 자가 치유 스크립트 (가장 확실함)**
   - 브라우저 기반 GUI 개발자도구 (F12 > Console) 에 붙여넣어 상시 구동하는 봇:
   ```javascript
   setInterval(() => {
     const run = document.querySelector('.agent-status.running');
     const noProg = !document.querySelector('.agent-progress, .terminal-output'); 
     if (run && noProg) {
       document.querySelector('[data-action="cancel"], .stop-btn')?.click();
       setTimeout(() => document.execCommand('RestartAgentService'), 2000);
     }
   }, 5000);
   ```

3. **수동 루틴 (최종 보험)**
   - Cancel 버튼 클릭 -> "현재 디렉토리 파일 목록?" 등으로 핑(Ping)을 날려 응답성(블록 해제) 여부 파악하기.
