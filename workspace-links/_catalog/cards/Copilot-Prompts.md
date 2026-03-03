---
type: project-card
project_name: "Copilot-Prompts"
display_name: "코파일럿 프롬프트 라이브러리"
entry_link: "[[copilot]]"
domain: prompt-ops
artifact_type:
  - prompt-library
  - research-notes
execution_mode: research
phase: active
review_cycle: weekly
priority: p2
risk_level: low
workflow_stage: "Prompt Asset"
sequence_order: 20
kanban_lane: "This Week"
plan_start: 2026-02-18
plan_end: 2026-02-28
progress_pct: 45
status_now: "프롬프트 세트는 확장 중이며, 버전별 성능 차이 기록이 필요함"
major_issues:
  - "좋은 프롬프트와 실패 프롬프트 비교 기록이 부족함"
  - "주제별 중복 프롬프트가 늘어남"
next_actions:
  - "프롬프트 카드에 실패 예시 1개 이상 의무화"
  - "MSW/OpenClaw 공용 프롬프트 번들 분리"
last_review: 2026-03-03
relationship_tags:
  - cross-domain
relations:
  - target: "[[workspace-links/_catalog/cards/Antigravity-Brain]]"
    kind: prompt-source
    direction: in
    strength: high
    reason: "리서치 문서를 프롬프트 자산으로 수신"
  - target: "[[workspace-links/_catalog/cards/MSW-VampireSurvivors]]"
    kind: build-support
    direction: out
    strength: medium
    reason: "개발 작업용 프롬프트 제공"
  - target: "[[workspace-links/_catalog/cards/OpenClaw]]"
    kind: ops-support
    direction: out
    strength: medium
    reason: "운영 자동화 프롬프트 제공"
---

# Copilot-Prompts

## 목적
- 리서치 결과를 재사용 가능한 프롬프트 자산으로 운영합니다.

## 분류 근거
- `domain`: prompt-ops
- `artifact_type`: prompt-library + research-notes
- `execution_mode`: research

## 연관 프로젝트
- [[workspace-links/_catalog/cards/Antigravity-Brain]] - prompt-source
- [[workspace-links/_catalog/cards/MSW-VampireSurvivors]] - build-support
- [[workspace-links/_catalog/cards/OpenClaw]] - ops-support

## 현황
- 프롬프트 저장량은 충분하나 품질 비교 체계가 보완 필요합니다.

## 문제
- 버전 비교 근거가 약해 회귀 탐지가 늦습니다.

## 다음 할 일
- 실패/개선 쌍을 기준으로 템플릿을 재정의합니다.

<!-- AUTO_INTEL:START -->
## 자동 인텔리전스
- 마지막 업데이트: 2026-03-03 00:06 UTC
- 수집 범위: 최근 30일
- 수집 건수: 10건
- 리포트: [[workspace-links/_catalog/updates/Copilot-Prompts/2026-03-03]]

### 핵심 시그널
- [Copilot usage metrics now includes enterprise-level GitHub Copilot CLI activity](https://github.blog/changelog/2026-02-27-copilot-usage-metrics-now-includes-enterprise-level-github-copilot-cli-activity) (RSS: https://github.blog/changelog/feed/, 2026-02-27)
- [From idea to pull request: A practical guide to building with GitHub Copilot CLI](https://github.blog/ai-and-ml/github-copilot/from-idea-to-pull-request-a-practical-guide-to-building-with-github-copilot-cli/) (RSS: https://github.blog/feed/, 2026-02-27)
- [What’s new with GitHub Copilot coding agent](https://github.blog/ai-and-ml/github-copilot/whats-new-with-github-copilot-coding-agent/) (RSS: https://github.blog/feed/, 2026-02-26)
<!-- AUTO_INTEL:END -->

<!-- CHATGPT_EXPORT_MERGE:fcf6183ee8ec -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Copilot-Prompts/2026-03-03_Auto-Claude_Overview_69a274dc-6e94-83aa-93f3-41925ecf3682|Auto-Claude Overview]]
- 토픽: `Copilot-Prompts`
- conversation_id: `69a274dc-6e94-83aa-93f3-41925ecf3682`
- 유사도: `0.279`

### 요약
https://github.com/AndyMik90/Auto-Claude

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:fcf6183ee8ec -->

<!-- CHATGPT_EXPORT_MERGE:2394a85770c0 -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Copilot-Prompts/2026-03-03_Pixel_Art_Robot_Sprite_69981390-6278-83a9-b411-fa908ea4d2f7|Pixel Art Robot Sprite]]
- 토픽: `Copilot-Prompts`
- conversation_id: `69981390-6278-83a9-b411-fa908ea4d2f7`
- 유사도: `0.243`

### 요약
Pixel art sprite sheet, 2 heads tall chibi robot running cycle, side view. Smooth metallic dome helmet, dark grey armor with glowing red lines, red chest core. Downsampled, very low resolution, chunky pixels, no anti-aliasing. Retro 2D side-scrolling game asset, flat colors, white background.

### 세부 메모
# Pixel Art Robot Sprite
- topic: `Copilot-Prompts`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/69981390-6278-83a9-b411-fa908ea4d2f7_Pixel_Art_Robot_Sprite.txt`
- conversation_id: `69981390-6278-83a9-b411-fa908ea4d2f7`
- matched_keywords: prompt
- card: [[workspace-links/_catalog/cards/Copilot-Prompts|코파일럿 프롬프트 라이브러리]]
## Summary
## Transcript
## 1. user
## 2. assistant
## 3. tool
## 4. user
## 5. assistant
## 6. tool
## 7. user
## 8. assistant
## 9. tool
## 10. user
- Frame 1 (Far Left): The red glow is very dim.
- Frame 2: The red glow is medium brightness.
- Frame 3: The red glow is very bright and intense.
- Frame 4 (Far Right): The red glow is medium brightness again.
## 11. assistant
## 12. tool
## 13. user
## 14. assistant
## 15. tool
Pixel art sprite sheet, 2 heads tall chibi robot running cycle, side view. Smooth metallic dome helmet, dark grey armor with glowing red lines, red chest core. Downsampled, very low resolution, chunky pixels, no anti-aliasing. Retro 2D side-scrolling game asset, flat colors, white background.
Pixel art sprite sheet, 2 heads tall chibi robot running cycle, side view. Smooth metallic dome helmet, dark grey armor with glowing red lines, red chest core. Downsampled, very low resolution, chunky pixels, no anti-aliasing. Retro 2D side-scrolling game asset, flat colors, white background.
{"prompt":null,"size":"1024x1024","n":1,"transparent_background":false}
{'asset_pointer': 'sediment://file_000000006820720797ab203bacdd8824', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1024, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': 1024, 'container_pixel_width': 1536, 'dalle': {'edit_op': None, 'gen_id': '023c31c8-ad76-43fe-afb5-7c74b652d84f', 'parent_gen_id': None, 'prompt': '', 'seed': None, 'serialization_title': 'DALL-E generation metadata'}, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': {'gen_id': '023c31c8-ad76-43fe-afb5-7c74b652d84f', 'gen_size': 'image',...

<!-- /CHATGPT_EXPORT_MERGE:2394a85770c0 -->

<!-- CHATGPT_EXPORT_MERGE:e753c6987d0c -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Copilot-Prompts/2026-03-03_에이전트모드_작업법_69909172-6520-83a2-a90b-bda2f8fa4be8|에이전트모드 작업법]]
- 토픽: `Copilot-Prompts`
- conversation_id: `69909172-6520-83a2-a90b-bda2f8fa4be8`
- 유사도: `0.138`

### 요약
에이전트모드와 작업 쓰는법

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:e753c6987d0c -->

<!-- CHATGPT_EXPORT_MERGE:e9e4726a4c19 -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Copilot-Prompts/2026-03-03_프롬프트_반복_효과_69a275d8-7448-83aa-af2c-5da45ef9b4ef|프롬프트 반복 효과]]
- 토픽: `Copilot-Prompts`
- conversation_id: `69a275d8-7448-83aa-af2c-5da45ef9b4ef`
- 유사도: `0.326`

### 요약
https://arxiv.org/abs/2512.14982

### 세부 메모
(no transcript)

<!-- /CHATGPT_EXPORT_MERGE:e9e4726a4c19 -->

<!-- CHATGPT_EXPORT_MERGE:9e98b9ce79a1 -->
## ChatGPT Export 통합 (2026-03-03)
- 원본: [[workspace-links/_tools/chatgpt-export/topics/Copilot-Prompts/2026-03-03_Cyborg_Running_Sprite_Sheet_6991ba97-7ac4-83a8-92f0-4cd1e662b874|Cyborg Running Sprite Sheet]]
- 토픽: `Copilot-Prompts`
- conversation_id: `6991ba97-7ac4-83a8-92f0-4cd1e662b874`
- 유사도: `0.139`

### 요약
"A pixel art sprite sheet showing a 4-frame running animation of a heavy cyborg mercenary. Side view. He has a bald head and a giant rusty robotic arm. He runs with a heavy, stomping gait, leaning forward. The coat trails behind to show speed. Isolated on a white background for game development."

### 세부 메모
# Cyborg Running Sprite Sheet
- topic: `Copilot-Prompts`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/6991ba97-7ac4-83a8-92f0-4cd1e662b874_Cyborg_Running_Sprite_Sheet.txt`
- conversation_id: `6991ba97-7ac4-83a8-92f0-4cd1e662b874`
- matched_keywords: prompt
- card: [[workspace-links/_catalog/cards/Copilot-Prompts|코파일럿 프롬프트 라이브러리]]
## Summary
## Transcript
## 1. user
## 2. assistant
## 3. tool
## 4. assistant
- 🔧 Tighten the animation loop (make frame 1 and 4 connect more seamlessly)
- 💥 Exaggerate the stomp impact (add dust puffs / stronger leg squash)
- 🎮 Convert to transparent background instead of white
- 📐 Reformat into a properly spaced sprite sheet grid (fixed frame width for engine import)
- 🎨 Reduce palette to strict 24–32 color retro limit
- 📦 Export as evenly sliced frames (e.g., 128x128 per frame)
"A pixel art sprite sheet showing a 4-frame running animation of a heavy cyborg mercenary. Side view. He has a bald head and a giant rusty robotic arm. He runs with a heavy, stomping gait, leaning forward. The coat trails behind to show speed. Isolated on a white background for game development."
"A pixel art sprite sheet showing a 4-frame running animation of a heavy cyborg mercenary. Side view. He has a bald head and a giant rusty robotic arm. He runs with a heavy, stomping gait, leaning forward. The coat trails behind to show speed. Isolated on a white background for game development."
{"prompt":null,"size":"1024x1024","n":1,"transparent_background":false}
{'asset_pointer': 'sediment://file_00000000c0b47208bb0b8af3f4be5b14', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1024, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': 1024, 'container_pixel_width': 1536, 'dalle': {'edit_op': None, 'gen_id': 'ac171e4b-5db8-4f93-8a19-efc4461c7dd2', 'parent_gen_id': None, 'prompt': '', 'seed': None, 'serialization_title': 'DALL-E generation metadata'}, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation'...

<!-- /CHATGPT_EXPORT_MERGE:9e98b9ce79a1 -->
