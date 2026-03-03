---
type: chatgpt-export-conversation
topic: "MSW-VampireSurvivors"
title: "Unity Importer 자동화 — 시트 자르고 클립 생성까지 한 번에"
conversation_id: "699b6baa-55ac-83a8-9bc1-3df356e6e6f4"
imported_at_utc: "2026-03-03T05:32:14+00:00"
turn_count: 1
chars: 3073
topic_score: 3
---

# Unity Importer 자동화 — 시트 자르고 클립 생성까지 한 번에

- topic: `MSW-VampireSurvivors`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/699b6baa-55ac-83a8-9bc1-3df356e6e6f4_Unity_Importer.txt`
- conversation_id: `699b6baa-55ac-83a8-9bc1-3df356e6e6f4`
- matched_keywords: unity, 유니티
- card: [[workspace-links/_catalog/cards/MSW-VampireSurvivors|MSW 본편 개발]]

## Summary
## 1. assistant 유니티에서 **픽셀 아트 스프라이트시트를 자동으로 “가져오기→그리드 슬라이스→행(애니메이션) 단위로 클립 생성”**까지 한 번에 처리하는 최소 패턴을 정리했어요. > 목표: 32×32 타일 고정 스프라이트시트를 임포트하면 자동으로 Multiple 슬라이스하고, 각 “행”을 한 세트로 묶어 애니메이션 클립(.anim)을 만들어 저장. --- ### 어떻게 동작하나요? - **OnPreprocessTexture**: TextureImporter를 `Sprite/Multiple`로 바꾸고, 고정된 타일 크기(예: 32×32)와 행/열 수에 맞춰 `SpriteMetaData[]`를 생성해 자동 슬라이스. - *...

## Transcript

## 1. assistant

유니티에서 **픽셀 아트 스프라이트시트를 자동으로 “가져오기→그리드 슬라이스→행(애니메이션) 단위로 클립 생성”**까지 한 번에 처리하는 최소 패턴을 정리했어요.  

> 목표: 32×32 타일 고정 스프라이트시트를 임포트하면 자동으로 Multiple 슬라이스하고, 각 “행”을 한 세트로 묶어 애니메이션 클립(.anim)을 만들어 저장.

---

### 어떻게 동작하나요?
- **OnPreprocessTexture**: TextureImporter를 `Sprite/Multiple`로 바꾸고, 고정된 타일 크기(예: 32×32)와 행/열 수에 맞춰 `SpriteMetaData[]`를 생성해 자동 슬라이스.
- **OnPostprocessSprites**: 방금 생긴 `Sprite[]`를 이름 규칙(예: `r00_c00`)에서 **행 키(r00, r01, …)** 로 그룹핑 → 행마다 `AnimationClip` 생성 → `SpriteRenderer.m_Sprite`에 시간축으로 키를 심어 12fps 루프.

---

### 바로 붙여 넣는 최소 예시 (드롭 위치: `Assets/Editor/AutoSpriteImporter.cs`)
```csharp
using UnityEditor;
using UnityEngine;
using System.Linq;

public class AutoSpriteImporter : AssetPostprocessor
{
    void OnPreprocessTexture()
    {
        var ti = (TextureImporter)assetImporter;
        ti.textureType = TextureImporterType.Sprite;
        ti.spriteImportMode = SpriteImportMode.Multiple;

        // ===== 프로젝트 규칙에 맞게 수정 =====
        int w = 32, h = 32;   // 타일 크기
        int cols = 4, rows = 8; // 스프라이트시트 열/행 수
        // ==================================

        var metas = new System.Collections.Generic.List<SpriteMetaData>();
        for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++)
        {
            metas.Add(new SpriteMetaData{
                name = $"r{y:00}_c{x:00}",
                // 유니티는 좌하(0,0) 기준: 위에서부터 y를 뒤집어서 계산
                rect = new Rect(x * w, (rows - 1 - y) * h, w, h),
                pivot = new Vector2(0.5f, 0.5f),
                alignment = (int)SpriteAlignment.Center
            });
        }
        ti.spritesheet = metas.ToArray();
    }

    void OnPostprocessSprites(Texture2D tex, Sprite[] sprites)
    {
        // 이름의 'rYY_cXX' 앞부분인 rYY로 그룹핑 → 한 행 = 한 애니메이션
        var byRow = sprites.GroupBy(s => s.name.Split('_')[0]);
        foreach (var g in byRow)
        {
            var clip = new AnimationClip { frameRate = 12f }; // 12fps
            var binding = EditorCurveBinding.PPtrCurve("", typeof(SpriteRenderer), "m_Sprite");

            var keys = g
                .OrderBy(s => s.name) // c00, c01, ... 순서 보장
                .Select((s, i) => new ObjectReferenceKeyframe {
                    time = i * (1f / 12f),
                    value = s
                })
                .ToArray();

            AnimationUtility.SetObjectReferenceCurve(clip, binding, keys);

            // 저장 위치는 프로젝트에 맞게 조정
            var dir = "Assets/Animations";
            if (!AssetDatabase.IsValidFolder(dir))
            {
                AssetDatabase.CreateFolder("Assets", "Animations");
            }
            AssetDatabase.CreateAsset(clip, $"{dir}/{g.Key}.anim");
        }
        AssetDatabase.SaveAssets();
    }
}
```

---

### 사용 팁
- **타일 규격/행열 수**만 프로젝트 규칙에 맞게 바꾸면 됩니다(`w/h/cols/rows`).
- 파일 이름 규칙이 다르면 `GroupBy` 로직(예: `_` 구분자, `rYY_cXX`)만 조정하세요.
- 8방향, 아이들/런/점프 등 **행=동작** 구조의 시트에 특히 유용합니다.
- 클립 저장 경로(`Assets/Animations`)는 팀 폴더 구조에 맞게 변경하세요.

---

필요하시면 **가변 타일 크기 자동 추론**, **프리픽스별 다른 fps 적용**, **AnimatorController 자동 생성(상태 전이 포함)** 버전으로도 확장해드릴게요.
