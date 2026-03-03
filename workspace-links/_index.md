# Workspace Links

Obsidian vault entry points to external work folders via junction.

## Project Classification
- [[workspace-links/_catalog/00_project_dashboard]]
- [[workspace-links/_catalog/01_classification_taxonomy]]
- [[workspace-links/_catalog/02_project_intake_checklist]]
- [[workspace-links/_catalog/03_relationship_dashboard]]
- [[workspace-links/_catalog/04_execution_overview]]
- [[workspace-links/_catalog/05_kanban_execution]]
- [[workspace-links/_catalog/07_naming_convention]]

## antigravity
- [[workspace-links/antigravity/brain]] -> `C:\Users\jhk92\.gemini\antigravity\brain`
- [[workspace-links/antigravity/code_tracker]] -> `C:\Users\jhk92\.gemini\antigravity\code_tracker`

## projects
- [[workspace-links/projects/MSW-VampireSurvivors]] -> `C:\Projects\MSW-VampireSurvivors`
- [[workspace-links/projects/MSW-VampireSurvivors-Pro]] -> `C:\Projects\MSW-VampireSurvivors-Pro`
- [[workspace-links/projects/Gameplay-OCR-ComputerUse-QA]] -> `C:\Projects\Gameplay-OCR-ComputerUse-QA`

## human-friendly shortcuts
- [[workspace-links/project-shortcuts/01_game_msw_core]] -> MSW 본편 개발
- [[workspace-links/project-shortcuts/02_game_msw_experiment]] -> MSW 실험 트랙
- [[workspace-links/project-shortcuts/03_gameplay_ocr_control_qa]] -> 게임플레이 OCR 제어 QA
- [[workspace-links/project-shortcuts/11_agent_brain_rnd]] -> 에이전트 브레인 R&D 허브
- [[workspace-links/project-shortcuts/12_agent_execution_tracker]] -> 실행 로그·코드 추적 허브
- [[workspace-links/project-shortcuts/13_agent_openclaw_ops]] -> OpenClaw 운영 허브
- [[workspace-links/project-shortcuts/21_prompt_copilot_library]] -> 코파일럿 프롬프트 라이브러리

## Usage
- Add link: `.\workspace-links\_tools\add-workspace-link.ps1 -TargetPath "C:\Projects\MyProject" -Category "projects"`
- Rename link target folder? Recreate the matching junction.
- 사람이 보는 이름 기준 진입은 `workspace-links/project-shortcuts`를 우선 사용.
