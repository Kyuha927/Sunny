---
type: chatgpt-export-conversation
topic: "Antigravity-CodeTracker"
title: "Aseprite→TexturePacker→Unity 자동화 파이프라인"
conversation_id: "6994c572-f318-83aa-8e6b-e58a3b8896f2"
imported_at_utc: "2026-03-03T05:32:12+00:00"
turn_count: 1
chars: 4315
topic_score: 3
---

# Aseprite→TexturePacker→Unity 자동화 파이프라인

- topic: `Antigravity-CodeTracker`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/6994c572-f318-83aa-8e6b-e58a3b8896f2_Aseprite_TexturePacker_Unity.txt`
- conversation_id: `6994c572-f318-83aa-8e6b-e58a3b8896f2`
- matched_keywords: 실행, 코드, log
- card: [[workspace-links/_catalog/cards/Antigravity-CodeTracker|실행 로그·코드 추적 허브]]

## Summary
## 1. assistant 아트 생성물→스프라이트시트→유니티 SpriteAtlas까지 “완전 자동화” 파이프라인을 한 번에 깔 수 있는 실전 가이드예요. (Aseprite → TexturePacker → Unity CLI) --- # 왜 필요한가 - **생성형 도구/픽셀에디터 결과**를 사람이 일일이 자르고 붙이면 느리고 불안정합니다. - **CI에서 재현 가능**해야 빌드마다 동일한 결과(Deterministic)가 나옵니다. # 폴더 레이아웃(리포/CI 러너에 그대로 넣기) ``` ci-pipeline/ art/ raw/ # 생성 PNG들 (comfy-gen-0001.png …) tools/ aseprite_export.sh...

## Transcript

## 1. assistant

아트 생성물→스프라이트시트→유니티 SpriteAtlas까지 “완전 자동화” 파이프라인을 한 번에 깔 수 있는 실전 가이드예요. (Aseprite → TexturePacker → Unity CLI)

---

# 왜 필요한가
- **생성형 도구/픽셀에디터 결과**를 사람이 일일이 자르고 붙이면 느리고 불안정합니다.  
- **CI에서 재현 가능**해야 빌드마다 동일한 결과(Deterministic)가 나옵니다.

# 폴더 레이아웃(리포/CI 러너에 그대로 넣기)
```
ci-pipeline/
  art/
    raw/                 # 생성 PNG들 (comfy-gen-0001.png …)
  tools/
    aseprite_export.sh
    pack_with_texturepacker.sh
    unity_create_atlas.cs
  out/
    sheets/              # TexturePacker 결과 PNG
    data/                # TexturePacker .json/.tpsheet
    unity-ready/         # Unity 프로젝트에 투입할 파일
```

# 1) Aseprite로 시트/태그별 내보내기
> Aseprite는 `.aseprite`의 레이어·태그·슬라이스 정보를 CLI로 뽑아줄 수 있어요.

기본(단일 시트):
```bash
aseprite -b assets/character.aseprite \
  --sheet out/sheets/character_sheet.png \
  --data  out/data/character_sheet.json \
  --sheet-pack
```

태그별 시트(공격/달리기 등):
```bash
aseprite -b --list-tags assets/character.aseprite
aseprite -b assets/character.aseprite \
  --sheet out/sheets/character_{tag}.png \
  --data  out/data/character_{tag}.json \
  --sheet-pack --sheet-type packed
```

옵션 팁
- `--split-layers`, `--slice`로 레이어/슬라이스 단위 분리 가능
- `--data` JSON은 프레임/태그 메타를 담아 후처리에 활용

# 2) TexturePacker로 유니티 포맷 패킹
> 선택 프레임만 따로 모아 유니티가 좋아하는 레이아웃으로 압축합니다.

예시:
```bash
TexturePacker \
  --format unity-texture2d \
  --data out/data/hero.tpsheet \
  --sheet out/sheets/hero.png \
  --multipack --max-size 4096 \
  --trim-mode None \
  out/selected/*
```

멀티팩(여러 페이지 강제):
```bash
TexturePacker \
  --format unity-texture2d \
  --data out/data/hero-{n}.tpsheet \
  --sheet out/sheets/hero-{n}.png \
  --multipack --max-size 4096 --trim-mode None \
  out/selected/*
```

# 3) Unity 에셋 임포트 + SpriteAtlas 자동 생성(에디터 스크립트)
아웃풋을 유니티 프로젝트로 복사:
```bash
mkdir -p UnityProject/Assets/Art/Atlases
cp out/sheets/*.png   UnityProject/Assets/Art/Atlases/
cp out/data/*.tpsheet UnityProject/Assets/Art/Atlases/
```

`Assets/Editor/AutoCreateAtlases.cs`:
```csharp
using UnityEditor; using UnityEditor.U2D; using UnityEngine.U2D; using UnityEngine;
public static class AutoCreateAtlases {
  public static void CreateAtlases() {
    var dest = "Assets/Art/Atlases";
    var sheets = System.IO.Directory.GetFiles(dest, "*.png");
    foreach (var s in sheets) {
      var name = System.IO.Path.GetFileNameWithoutExtension(s) + "_atlas";
      var atlasPath = $"Assets/Art/Atlases/{name}.spriteatlas";
      var atlas = new SpriteAtlas();
      SpriteAtlasExtensions.Add(atlas, new Object[] { AssetDatabase.LoadAssetAtPath<Texture2D>(s) });
      AssetDatabase.CreateAsset(atlas, atlasPath);
    }
    AssetDatabase.SaveAssets(); AssetDatabase.Refresh();
    Debug.Log("Auto-created SpriteAtlases for " + sheets.Length + " sheets.");
  }
}
```

Unity CLI로 실행:
```bash
unity -projectPath /workspace/UnityProject \
  -batchmode -quit \
  -executeMethod AutoCreateAtlases.CreateAtlases \
  -logFile build/unity_atlas.log
```

# 4) CI 스텝(요지)
1. **툴 버전 고정**: Aseprite/TexturePacker/Unity(에디터) 버전을 명시(도커 이미지나 설치 스크립트 해시 고정).
2. **아트 생성물 수집**: `ci-pipeline/art/raw/` 또는 `out/selected/`에 복사.
3. **Aseprite 내보내기 → TexturePacker 패킹**.
4. **Unity 프로젝트에 복사 후 Editor 메서드 실행**.
5. **아티팩트 업로드**: `out/`와 `Assets/Art/Atlases/*.spriteatlas`.

# 샘플 스크립트
`tools/aseprite_export.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail
aseprite -b assets/character.aseprite \
  --sheet out/sheets/character_sheet.png \
  --data  out/data/character_sheet.json \
  --sheet-pack
```

`tools/pack_with_texturepacker.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail
TexturePacker --format unity-texture2d \
  --data out/data/hero.tpsheet \
  --sheet out/sheets/hero.png \
  --multipack --max-size 4096 --trim-mode None out/selected/*
```

`tools/unity_create_atlas.cs` → 위 C# 스니펫과 동일(파일명 자유)

# 운영 팁
- **유니티 임포터 호환**: TexturePacker는 `--format unity-texture2d`를 권장. (.tpsheet를 쓰면 TexturePacker Unity Importer도 선택 가능)
- **이름 체계**: Aseprite `--data` JSON의 태그/슬라이스 이름으로 스프라이트 네이밍 규칙을 통일해두면 코드 참조가 쉬움.
- **결정론 보장**: 동일 입력에 동일 출력이 되도록
  - 툴 버전 고정, 알파 프리멀티/트리밍 옵션 고정
  - 정렬/소팅 기준 고정(파일명 기준 등)
- **멀티팩 기준**: 해상도 정책(예: 2048/4096), 모바일 대상이면 메모리 예산 고려해 시트 쪼개기.
- **캐시**: `out/`을 CI 캐시에 얹어 반복 빌드 가속.
- **AssetDatabase.Refresh()**를 반드시 호출(위 스크립트 포함).

---

필요하시면 **GitHub Actions용 워크플로(yml)**, **Dockerfile(툴 버전 고정)**, **Aseprite JSON→Unity Sprite 이름 맵핑 스크립트**까지 바로 만들어드릴게요.
