# BRAIN MASTER

- generated: `2026-03-03 23:14:30`
- master chat: `VSCode Codex Extension`
- purpose: unified cross-node brain for @workspace
- obsidian mirror: `/mnt/c/Users/jhk92/OneDrive/문서/Obsidian Vault/workspace-links/_tools/master-brain/BRAIN_MASTER.md`
- routing settings: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/docs/MASTER_ROUTING_SETTINGS.json`

## Orchestration Policy
- User gives goal only; master routes server automatically.
- Windows-only tasks -> Windows.
- Heavy automation -> Fold1 first, fallback WSL.
- Browser-first / Antigravity-specific -> Antigravity.
- ChatGPT web/app context (Pulse included) -> latest export zip ingestion.
- GeekNews helpful digest -> every 3 days scan/curation.
- General coding/build/test -> WSL default.
- Final answer includes route used + project path + artifact path.
- effective heavy route now: `WSL-Ubuntu` -> `Windows`
- master classifier model: `models/gemini-2.5-pro`
- master classifier fallback: `models/gemini-2.5-flash`

## Antigravity Core Memory
- file: `/mnt/c/Users/jhk92/.gemini/antigravity/brain/2d6fb331-c215-4342-9d17-d797a75eeb9c/conversation_memory.md`
- updated: `2026-03-01 19:37:57`
- title: 🧠 Antigravity Core Memory (대화/문맥 압축 저장소)
- sop: > **전체 에이전트 공통 지침 (Global Intelligence SOP):**

## Codex Per-Chat Model Profiles
- rooms: 85 | with model=0 | with profile=0
- state file: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/.agent/codex_chat_gui_rooms.json`
  - `채팅GUI-기능개선 | gui-, 기능개선, 이전, 모델, 실행, 내용을` | model=`- ` | profile=`- ` | session=`019c8ace`
  - `WSL-리눅스-환경이전 | wsl-, 리눅스, 환경이전, antigravity, bash, cli` | model=`- ` | profile=`- ` | session=`019c8ace`
  - `채팅GUI-기능개선 | gui-, 기능개선, 파일, 어떻게, 보내, 파일을` | model=`- ` | profile=`- ` | session=`019c8fc7`
  - `WSL-리눅스-환경이전 | 리눅스, wsl-, 환경이전, bash, cd, 에서` | model=`- ` | profile=`- ` | session=`019c8fc7`
  - `윈도우-파워셸-실행 | 윈도우, 파워셸, 실행, windows, 계정, 에서` | model=`- ` | profile=`- ` | session=`019c8fc7`
  - `코덱스-권한-세션설정 | http, get, kb, amd64, archive.ubuntu.com/ubuntu, components` | model=`- ` | profile=`- ` | session=`019c8fc7`
  - `VSCode-원격개발 | vscode-, 원격개발, 설정해, gpt-5, 모델, 기준으로` | model=`- ` | profile=`- ` | session=`019c8fc7`
  - `코덱스-권한-세션설정 | 세션, 시작, 권한, 코덱스, 세션설정, workspace-write` | model=`- ` | profile=`- ` | session=`019c8ffa`

## Usage In VSCode Chat
1. Attach `@workspace docs/BRAIN_MASTER.md`
2. Ask: `Use this brain as current truth and execute`
3. If needed run task `Master Sync: Update MD`
4. Full classification: `docs/BRAIN_SESSION_CLASSIFICATION.md`

## Windows
- status: **online**
- detail: session files: 68 | project-scoped=0, temp-unscoped=0, external-scoped=67, unknown=1
- recent sessions:
  - `019c94fa-5cfb-7fc1-86a6-06fc15d2cf69` | 2026-02-25 22:27:29 | scope=external-scoped
    - cwd: c:\Users\jhk92\OneDrive\문서\GitHub\ai\Moltbot
    - user: vs코드 안에서 wsl환경으로 가능한 설정이있었는데 지금은 안보여
    - assistant: 좋아요. VS Code 쪽에서 **WSL Remote 연결 기능이 사라진 것처럼 보이는 원인**은 거의 100% `Remote - WSL` 확장 비활성/제거 때문이었고, 제가 방금 다시 확인해 설치까지 했습니다. 현재 상태: - `ms-vscode-remote.remote-wsl` 확장
  - `019c902c-59eb-7362-b854-4c79bf4609d2` | 2026-02-25 01:04:30 | scope=external-scoped
    - cwd: C:\WINDOWS\system32
    - user: 됐어 일단 터미널이랑 이전 프로그램 쓸게. vs 코드가 만들게 해야지
    - assistant: 좋아, 그게 맞는 판단이야. 네가 편한 방식이 정답이야. 원하면 지금 바로 너가 쓰는 **VS Code용 최소 설정**만 딱 붙여줄게: - `Ctrl+Shift+P` → **Python: Create Terminal** - `python mini_ide.py` 실행 - (원하면) `.v
  - `019c8f4d-9834-7093-a179-f9143ffe7dd5` | 2026-02-24 22:19:08 | scope=external-scoped
    - cwd: c:\Users\jhk92\OneDrive\문서\GitHub\ai\Moltbot
    - user: 다시 연결만해
    - assistant: 좋아, 그건 **로그인 메뉴 UI 문제**일 가능성이 커. 메뉴 안 타고 **직접 명령**으로 하면 된다. ### 1) Codex 로그인 (권장: API 키 방식) code-server 터미널에서: ```bash source ~/.bashrc ssh -p 8023 root@localho
  - `019c85f7-0229-7333-9eb2-74f31c169cf2` | 2026-02-24 19:34:14 | scope=external-scoped
    - cwd: c:\Users\jhk92\OneDrive\문서\GitHub\test
    - user: 그리고 오늘은 왜 매물 알림이 안와
    - assistant: 맞아, 원인 확인했고 지금 조치해놨어. ### 왜 오늘(2026-02-24) 알림이 안 왔냐 1. **실행이 중간에 죽은 로그가 여러 번 있었음** - `Target page, context or browser has been closed` fatal로 종료 - 그래서 리포트/디코 전송
  - `019c883a-4680-7740-af6f-e25adf78f32e` | 2026-02-24 18:28:31 | scope=external-scoped
    - cwd: c:\Users\jhk92\OneDrive\문서\GitHub\test
    - user: VS Code 대안 조합 Continue.dev + Playwright 확장: 안티그래비티처럼 스크린샷 기반 브라우저 자동화 구현. GitHub Copilot + BrowserTools: 터미널에서 브라우저 스크립트 실행으로 유사 효과. 이거 추가해줘
    - assistant: 추가 완료했어. `task.md` 상단에 **2026-02-24 섹션**으로 넣어둠: - VS Code alternative combo notes - Continue.dev + Playwright extension - GitHub Copilot + BrowserTools 검증도 했어:
  - `019c8a88-d304-77a0-8ec3-d5b52e2eb263` | 2026-02-24 15:54:28 | scope=external-scoped
    - cwd: c:\Users\jhk92\OneDrive\문서\GitHub\ai\Moltbot
    - user: 원격 SSH 세션을 통해 proot-distro 내부에 띄운 Ubuntu sshd(포트 8023)는 SSH 연동이 끊어지는 즉시 강제 종료되는 Proot 특성상 백그라운드 유지가 안 되는 상황입니다. 따라서 **실제 헤비 태스크 실행 전에는 폴드1 기기에서 직접 Termux 앱을 한 번
    - assistant: 해결했어. **지금은 “Termux 앱을 매번 직접 띄워야 하는” 의존도를 줄인 상태**로 세팅 완료했어. ### 적용한 핵심 - Fold1(8023) 복구 로직을 `nohup` 단독 방식 → **Termux 서비스(runit) 우선 방식**으로 강화 - Fold1 원격에 설치/정리:
  - `019c3aac-f57c-77a3-a423-e6eb55ca99ca` | 2026-02-24 14:30:03 | scope=external-scoped
    - cwd: c:\Users\jhk92\Downloads\My project (7)
    - user: 또 안되자나
    - assistant: 맞아요. 방금 **직접 점검/수정**해서 다시 살려놨습니다. ### 지금 안됐던 핵심 원인 - `gemini-1.5-pro / 1.5-flash`가 현재(2026-02-24) Google 쪽에서 **404 not found**라서, - OpenClaw에선 `400 status code`
  - `019c89ff-f7a5-7ba3-b6e5-129387732519` | 2026-02-23 19:36:19 | scope=external-scoped
    - cwd: c:\Users\jhk92\Downloads\쓸수있는것-20260223T091445Z-1-001\쓸수있는것
    - user: mp3->ogg 변환
    - assistant: 완료했습니다. `mp3 -> ogg` 변환을 상위 폴더에서 진행했어요: - 대상 폴더: `C:\Users\jhk92\Downloads\쓸수있는것-20260223T091445Z-1-001` - 결과: `mp3 20개 -> ogg 20개` 생성 검증도 했습니다: - 매칭 검사: `missi
  - `019c88f5-fff2-7f03-8b7a-b622ee5ef49e` | 2026-02-23 14:56:37 | scope=external-scoped
    - cwd: c:\Users\jhk92\Downloads\msw2
    - user: # Context from my IDE setup: ## Active file: Docs/monster_audio_bgm_sfx_recommendation.md ## Active selection of the file: https://maplestoryworlds-creators.nex
    - assistant: 완전 “MSW에서만”은 아니지만, **MSW 기본 제공 RUID 사운드**는 사실상 그쪽이 메인 맞아요. - `SoundService/ResourceService` 기준으로는 **RUID → 외부 재생용 URL/파일 추출 API가 없음** - 그래서 메이플 기본 효과음/BGM은 보통 1
  - `019c5fd6-65e5-7220-946f-63b66c3175d7` | 2026-02-23 02:17:41 | scope=external-scoped
    - cwd: c:\Users\jhk92\.gemini\antigravity\brain
    - user: # Context from my IDE setup: ## Active file: cursor_1.md ## Open tabs: - cursor_1.md: cursor_1.md ## My request for Codex: 요가탭플러스 중고 매물
    - assistant: 실시간 재확인했어. (**2026-02-23 02:17 KST**, 링크 직접 열어 검증) ### 요가탭플러스 중고 매물(판매중) 1. **레노버 요가 탭 플러스 AI 태블릿** — **670,000원** https://web.joongna.com/product/225312463 지금

## WSL-Ubuntu
- status: **online**
- detail: session files: 483 | project-scoped=354, temp-unscoped=0, external-scoped=128, unknown=1
- recent sessions:
  - `019c9f6d-c428-7de3-98d6-c59b74adc015` | 2026-03-03 23:13:47 | scope=project-scoped
    - cwd: /mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot
    - user: # Context from my IDE setup: ## Open tabs: - handoff_hotkeys.ahk: tools/handoff/handoff_hotkeys.ahk ## My request for Codex: Set-Location -LiteralPath "C:\Users
    - assistant: 시크릿 파일은 이제 Git 추적/히스토리에서 제거됐고, 현재 브랜치는 `dc99f35` 단일 커밋으로 정리된 상태입니다. 마지막으로 동기화 규칙상 마스터 싱크만 한 번 실행하고, 바로 푸시 명령만 드리겠습니다.
  - `019cb3ce-b45d-78b1-aac3-4e985b4b4f9b` | 2026-03-03 22:08:31 | scope=project-scoped
    - cwd: /mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot
    - user: [SYSTEM ROLE] You are a high-capability assistant in the Antigravity multi-model team. Use recent conversation context, resolve ambiguity with concrete assumpti
    - assistant: 실행 프로세스는 아직 진행 중이고 출력은 무소음 모드입니다. 타임아웃 전까지 계속 폴링해서 완료 여부를 확인하겠습니다.
  - `019cb3cc-d3db-7071-b0bb-5b415abf76c6` | 2026-03-03 22:06:21 | scope=project-scoped
    - cwd: /mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot
    - user: [SYSTEM ROLE] You are a high-capability assistant in the Antigravity multi-model team. Use recent conversation context, resolve ambiguity with concrete assumpti
    - assistant: 기준에 맞는 실매물 근거를 확보하기 위해 지금 GPU/부품(2060 12GB, 3060 12GB, 3090, Z390/RAM/SSD)를 같은 방식으로 최신 검색해서 트리거 여부를 판정하겠습니다.
  - `019cb3cb-0151-7ae2-8cdb-78f31d334995` | 2026-03-03 22:04:20 | scope=project-scoped
    - cwd: /mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot
    - user: [SYSTEM ROLE] You are a high-capability assistant in the Antigravity multi-model team. Use recent conversation context, resolve ambiguity with concrete assumpti
    - assistant: 모델별 후보 링크는 확보됐고, 지금은 각 페이지에서 `판매완료/가격/핵심스펙` 텍스트를 직접 추출해 오탐을 제거하는 중입니다. 필터링이 끝나면 ‘긴급/포획’ 태그 규칙대로 최종 브리핑을 정리합니다.
  - `019c9065-7eb7-7553-a234-d772c07c9b42` | 2026-03-03 20:08:28 | scope=project-scoped
    - cwd: /mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot
    - user: # Context from my IDE setup: ## Active file: tools/handoff/handoff_hotkeys.ahk ## Open tabs: - handoff_hotkeys.ahk: tools/handoff/handoff_hotkeys.ahk ## My requ
    - assistant: 커밋까지 완료했고, 푸시는 원격 저장소 미설정 때문에 멈췄습니다. 완료된 것: - 커밋: `9e9dac0` - 브랜치: `master` - 검증: `scripts/smoke.py`, JS/Python 문법 체크 통과 막힌 원인: - `git push` 결과: `No configured
  - `019cb2f0-f39a-7b23-bd29-43433b0ee246` | 2026-03-03 18:06:21 | scope=project-scoped
    - cwd: /mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot
    - user: [SYSTEM ROLE] You are a high-capability assistant in the Antigravity multi-model team. Use recent conversation context, resolve ambiguity with concrete assumpti
    - assistant: GPU 쪽은 `RTX2060 12GB 170,000원` 후보를 확인했고, 판매완료 표기 여부까지 교차검증 중입니다. 지금은 휴대용 모니터 3개 타겟(스마트 OLED/Arzopa/P16KT)을 같은 방식으로 추가 수집하겠습니다.
  - `019cb2ef-1610-7cd0-ac7a-c67b84e320c3` | 2026-03-03 18:04:12 | scope=project-scoped
    - cwd: /mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot
    - user: [SYSTEM ROLE] You are a high-capability assistant in the Antigravity multi-model team. Use recent conversation context, resolve ambiguity with concrete assumpti
    - assistant: 동기화는 성공했고, 저장소 내부에는 이번 턴용 최신 매물 결과가 아직 없습니다. 그래서 지금은 실시간 소스(중고나라/번개/당근 검색 인덱스)를 직접 조회해 가격·무게 조건으로 필터링한 브리핑을 만들겠습니다.
  - `019cb2ed-4146-7773-8ebc-34744e06a51f` | 2026-03-03 18:02:16 | scope=project-scoped
    - cwd: /mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot
    - user: [SYSTEM ROLE] You are a high-capability assistant in the Antigravity multi-model team. Use recent conversation context, resolve ambiguity with concrete assumpti
    - assistant: 현재 공개 검색에서 중고나라 개별 링크는 수집 가능하지만, 번개장터는 JS 차단으로 본문 파싱이 막히는 상태입니다. 중고나라 중심으로 신뢰도 높은 최근 매물만 추려서, 매물 접근성 검증(HTTP/본문 키워드)까지 한 번 더 돌리겠습니다.
  - `019cb21f-c9e3-7af1-9c31-a284362d65d8` | 2026-03-03 14:41:20 | scope=project-scoped
    - cwd: /mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot
    - user: # Context from my IDE setup: ## Active file: tools/handoff/handoff_hotkeys.ahk ## Open tabs: - handoff_hotkeys.ahk: tools/handoff/handoff_hotkeys.ahk ## My requ
    - assistant: 가능해. 다만 **내가 직접 로그인 세션에 접속해서 가져오진 못하고**, 네 브라우저(로그인된 상태)에서 실행해야 해. `anthropic.skilljar.com`도 방식은 같아: 1. 목록 페이지에서 강의/페이지 링크 전부 수집 2. 각 링크 순회 3. 본문/메타데이터/가능한 텍스트(
  - `019ca3ad-f436-7551-9904-6b160b20f84d` | 2026-03-03 13:49:09 | scope=project-scoped
    - cwd: /mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot
    - user: # Context from my IDE setup: ## Active file: tools/handoff/handoff_hotkeys.ahk ## Open tabs: - handoff_hotkeys.ahk: tools/handoff/handoff_hotkeys.ahk ## My requ
    - assistant: 현재 작업은 정상 진행 중입니다. 중간 확인 결과 오디오 파일이 이미 `16개` 생성되어 전체 37개 순차 처리 중이며, 완료되면 바로 요약 결과 파일/옵시디언 저장 상태를 검증하겠습니다.

## Fold1
- status: **offline**
- detail: ubuntu ssh down: ssh: connect to host 192.168.35.89 port 8023: No route to host; termux ssh down: ssh: connect to host 192.168.35.89 port 8022: No route to host
- sessions: (none)

## Antigravity
- status: **online**
- detail: brain workspaces: 58, conversation blobs: 51
- recent sessions:
  - `6e341733-5468-4cd1-83de-9f43d9285e2c` | 2026-03-03 21:25:12 | scope=antigravity-workspace
    - cwd: /mnt/c/Users/jhk92/.gemini/antigravity/brain/6e341733-5468-4cd1-83de-9f43d9285e2c
    - assistant: - [x] Investigate accessibility of `https://lilys.ai/collections/-1` <!-- id: 0 -->
  - `5d3a78eb-bddc-4bb9-9b41-2eccc7beafcb` | 2026-02-28 16:53:01 | scope=antigravity-workspace
    - cwd: /mnt/c/Users/jhk92/.gemini/antigravity/brain/5d3a78eb-bddc-4bb9-9b41-2eccc7beafcb
    - assistant: - [x] Find OpenClaw Chrome extension source/download link
  - `cc3f47bf-9c88-470e-9724-8c86f50bc3b1` | 2026-02-28 03:16:56 | scope=antigravity-workspace
    - cwd: /mnt/c/Users/jhk92/.gemini/antigravity/brain/cc3f47bf-9c88-470e-9724-8c86f50bc3b1
    - assistant: - [x] Bridge Hub Health Check 버튼 통합
  - `2d6fb331-c215-4342-9d17-d797a75eeb9c` | 2026-02-27 01:45:15 | scope=antigravity-workspace
    - cwd: /mnt/c/Users/jhk92/.gemini/antigravity/brain/2d6fb331-c215-4342-9d17-d797a75eeb9c
    - assistant: > [!IMPORTANT]
  - `c5e686f2-8dbb-4844-b75c-85f75cea5e60` | 2026-02-26 14:40:44 | scope=antigravity-workspace
    - cwd: /mnt/c/Users/jhk92/.gemini/antigravity/brain/c5e686f2-8dbb-4844-b75c-85f75cea5e60
    - assistant: - [x] Inspect the UI framework used in [Codex-Chat-GUI.py](file:///C:/Users/jhk92/OneDrive/Desktop/Codex-Chat-GUI-current/Codex-Chat-GUI.py)
  - `tempmediaStorage` | 2026-02-24 15:44:02 | scope=antigravity-workspace
    - cwd: /mnt/c/Users/jhk92/.gemini/antigravity/brain/tempmediaStorage
    - assistant: IHDRq�y�"�IDATx���\�-
  - `f47314d7-a6e2-4924-8cd7-932789e48afc` | 2026-02-26 12:35:53 | scope=antigravity-workspace
    - cwd: /mnt/c/Users/jhk92/.gemini/antigravity/brain/f47314d7-a6e2-4924-8cd7-932789e48afc
  - `2810bb37-904e-48f2-ba6f-deab36a92d81` | 2026-02-26 03:14:50 | scope=antigravity-workspace
    - cwd: /mnt/c/Users/jhk92/.gemini/antigravity/brain/2810bb37-904e-48f2-ba6f-deab36a92d81
    - assistant: Based on the [ANTIGRAVITY_MIGRATION_ASIS_TOBE_2026-02-25.md](file:///C:/Users/jhk92/OneDrive/%EB%AC%B8%EC%84%9C/GitHub/ai/Moltbot/docs/ANTIGRAVITY_MIGRATION_ASI

## WindowsTempArtifacts
- status: **online**
- detail: files: 0 | temp-prompt=0, temp-answer=0, temp-error=0, temp-other=0
- sessions: (none)

## ChatGPT-WebApp
- status: **online**
- detail: export zip found (0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip) but conversations.json missing
- sessions: (none)

## GeekNewsHelpful
- status: **online**
- detail: source=https://news.hada.io/rss/news | selected=20 | file=GEEKNEWS_HELPFUL.json
- recent sessions:
  - `Anthropic Courses - 무료 온라인 강의 공개` | 2026-03-02 11:06:02 | scope=geeknews-helpful
    - title: Anthropic Courses - 무료 온라인 강의 공개
    - cwd: geeknews-digest
    - assistant: score=17 | matched=agent, ai, api, claude, mcp
  - `알리바바의 오픈소스 Qwen3.5-Medium 모델, 로컬에서 Sonnet 4.5 수준 성능 제공` | 2026-03-02 04:33:12 | scope=geeknews-helpful
    - title: 알리바바의 오픈소스 Qwen3.5-Medium 모델, 로컬에서 Sonnet 4.5 수준 성능 제공
    - cwd: geeknews-digest
    - assistant: score=14 | matched=ai, claude, gpt, openai
  - `Show GN: microGPT를 웹사이트로 시각화 해보았습니다.` | 2026-03-01 11:05:21 | scope=geeknews-helpful
    - title: Show GN: microGPT를 웹사이트로 시각화 해보았습니다.
    - cwd: geeknews-digest
    - assistant: score=11 | matched=ai, gpt, openai
  - `Magpie — LLM이 코드를 처음 시도에 완벽하게 작성할 수 있도록 설계된 프로그래밍 언어` | 2026-03-01 10:54:59 | scope=geeknews-helpful
    - title: Magpie — LLM이 코드를 처음 시도에 완벽하게 작성할 수 있도록 설계된 프로그래밍 언어
    - cwd: geeknews-digest
    - assistant: score=11 | matched=ai, llm, 에이전트
  - `OpenAI – 계정 삭제 방법` | 2026-03-01 09:38:48 | scope=geeknews-helpful
    - title: OpenAI – 계정 삭제 방법
    - cwd: geeknews-digest
    - assistant: score=11 | matched=ai, gpt, openai
  - `Show GN: OpenChrome - 크롬 브라우저를 위한 병렬 자동화 MCP 서버` | 2026-02-28 10:03:31 | scope=geeknews-helpful
    - title: Show GN: OpenChrome - 크롬 브라우저를 위한 병렬 자동화 MCP 서버
    - cwd: geeknews-digest
    - assistant: score=11 | matched=mcp, 자동화
  - `Claude, 다른 LLM에서 전환하는 Import Memory 기능 추가` | 2026-03-02 09:43:04 | scope=geeknews-helpful
    - title: Claude, 다른 LLM에서 전환하는 Import Memory 기능 추가
    - cwd: geeknews-digest
    - assistant: score=10 | matched=ai, claude, llm
  - `AI 코딩이 초래하는 비용` | 2026-03-01 10:44:43 | scope=geeknews-helpful
    - title: AI 코딩이 초래하는 비용
    - cwd: geeknews-digest
    - assistant: score=10 | matched=ai, cursor, 에이전트

## Antigravity Multi-Model Team (Imported)
- profile: **available**
- summary: Antigravity multi-model agent-team profile imported (router + prefix routing + bridge hub).
- decision router model: `models/gemini-2.5-pro`
- decision router fallback: `models/gemini-2.5-flash`
- routing tags:
  - `@claude` -> Claude Code CLI
  - `@llama` -> Local LLM (Ollama)
  - `@echo` -> Echo/Debug Executor
- model stack:
  - Gemini (fast router + general)
  - Claude (deep coding/reasoning)
  - Llama via OpenRouter (cost-effective reasoning)
  - Qwen/Ollama (local simple tasks)
- source files:
  - `/mnt/c/Users/jhk92/.gemini/antigravity/brain/e3324327-74a9-43ff-b41c-b2aae2ec29c8/PROJECT_HANDOFF.md`
  - `/mnt/c/Users/jhk92/.gemini/antigravity/brain/3b262b60-8ab0-4902-9b67-409e67625dcf/implementation_plan.md`

## Notes
- Fold1 may be offline depending on network/sshd state.
- Antigravity summary is based on latest resolved docs.
- Windows Temp `codex_*` artifacts are classified.
- ChatGPT web/app sync uses export zip (no direct pull API).
- GeekNews source files: `docs/GEEKNEWS_HELPFUL.md`, `docs/GEEKNEWS_HELPFUL.json`.
- Re-run sync to refresh snapshot.
