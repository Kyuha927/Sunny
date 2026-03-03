---
type: chatgpt-export-conversation
topic: "MSW-VampireSurvivors-Pro"
title: "ModifiedValues + UpgradeSystem으로 완성하는 퍼크 구조"
conversation_id: "699b6ba3-0380-83aa-9d40-b3b080d6b83e"
imported_at_utc: "2026-03-03T05:32:13+00:00"
turn_count: 1
chars: 3055
topic_score: 3
---

# ModifiedValues + UpgradeSystem으로 완성하는 퍼크 구조

- topic: `MSW-VampireSurvivors-Pro`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/699b6ba3-0380-83aa-9d40-b3b080d6b83e_ModifiedValues_UpgradeSystem.txt`
- conversation_id: `699b6ba3-0380-83aa-9d40-b3b080d6b83e`
- matched_keywords: msw, pro, 프로
- card: [[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro|MSW 실험 트랙]]

## Summary
## 1. assistant 게임에 “레벨업→선택→영구/일시 버프” 흐름을 간단히 붙이고 싶다면, **ModifiedValues(= Improx/ModifiedValues)**와 **UpgradeSystem**(둘 다 MIT 라이선스, C#) 조합이 깔끔해요. ModifiedValues는 스탯 합/곱 레이어와 제거 가능한 모디파이어를 “결정론적”으로 계산해주고, UpgradeSystem은 스크립터블 오브젝트(SO) 기반으로 업그레이드 아이템·선택 UI 저작면을 제공합니다. 핵심은 **수학(스택/버프)은 ModifiedValues**, **선택/콘텐츠 작성은 UpgradeSystem**으로 분리해 테스트 가능하고 유지보수 쉬운 구조를...

## Transcript

## 1. assistant

게임에 “레벨업→선택→영구/일시 버프” 흐름을 간단히 붙이고 싶다면, **ModifiedValues(= Improx/ModifiedValues)**와 **UpgradeSystem**(둘 다 MIT 라이선스, C#) 조합이 깔끔해요. ModifiedValues는 스탯 합/곱 레이어와 제거 가능한 모디파이어를 “결정론적”으로 계산해주고, UpgradeSystem은 스크립터블 오브젝트(SO) 기반으로 업그레이드 아이템·선택 UI 저작면을 제공합니다. 핵심은 **수학(스택/버프)은 ModifiedValues**, **선택/콘텐츠 작성은 UpgradeSystem**으로 분리해 테스트 가능하고 유지보수 쉬운 구조를 만드는 것.

---

### 왜 이 조합이 좋은가
- **결정론적 스탯 계산**: Add→Mul→Post 순서 고정, 동일 입력 = 동일 결과.
- **모듈성**: 전투/이코노미 로직과 UI·콘텐츠 저작을 분리.
- **가벼운 의존성**: 둘 다 최소 구성, 기존 프로젝트에 드롭인.

### 설치(요약)
1) 두 패키지 폴더를 Unity 프로젝트에 추가(또는 UPM Git).  
2) `PlayerStats` 같이 **ModifiedValue**들을 보관할 컴포넌트를 하나 둠(예: HP, Damage, MoveSpeed…).  
3) UpgradeSystem에 **Upgrade(Perk) SO**들을 만들어 “이 업그레이드가 적용될 때 ModifiedValues에 어떤 모디파이어를 붙일지”를 정의.

### 예시 구조
```csharp
// 1) 스탯 컨테이너
public class PlayerStats : MonoBehaviour {
    public ModifiedValue damage = new ModifiedValue(10f); // 기본 10
    public ModifiedValue moveSpeed = new ModifiedValue(5f);
}

// 2) 업그레이드 정의 (SO)
[CreateAssetMenu(menuName="Upgrades/DamageUp x20%")]
public class DamageMul20 : ScriptableObject, IUpgrade {
    public string Id => "damage_mul_20";
    public string Title => "데미지 +20%";
    public string Desc => "모든 공격 데미지가 20% 증가";
    Modifier _mod;
    public void Apply(GameObject target){
        var stats = target.GetComponent<PlayerStats>();
        _mod = Modifier.Multiplier(0.2f, source: this);   // 곱연산 20%
        stats.damage.AddModifier(_mod);
    }
    public void Remove(GameObject target){
        var stats = target.GetComponent<PlayerStats>();
        if (_mod != null) stats.damage.RemoveModifier(_mod);
    }
}
```

### 레벨업 흐름(간단 연결)
1) **XP 획득**: 적 처치/픽업 시 XP 증가 → `while (xp >= xpToNext) { LevelUp(); }`  
2) **선택 UI 호출**: UpgradeSystem의 “3개 중 1개 선택” 팝업 띄움.  
3) **적용**: 선택된 SO의 `Apply(player)` → ModifiedValues에 모디파이어 등록 → HUD 즉시 반영.

```csharp
public class Leveling : MonoBehaviour {
    public int lv = 1; public float xp, xpToNext = 10;
    public UpgradeCatalog catalog; // 등록된 업그레이드 리스트
    public PlayerStats stats;

    public void GainXp(float v){
        xp += v;
        while (xp >= xpToNext) {
            xp -= xpToNext; lv++;
            xpToNext = Mathf.Ceil(xpToNext * 1.25f);
            ShowChoicesAndApply();
        }
    }
    void ShowChoicesAndApply(){
        var choices = catalog.Roll(3);           // 임의 3개 뽑기
        UpgradeUI.Show(choices, onPick: (u)=> {
            u.Apply(gameObject);                 // 선택 즉시 적용
            UpgradeUI.Hide();
        });
    }
}
```

### 제작 팁
- **합/곱 레이어 분리**: +평면(예: +5 데미지)와 ×평면(예: +20%)을 섞되, 곱은 가능한 모아서(버프 간 순서 논쟁 제거).  
- **모디파이어 태깅**: `source`/`tag`를 넣어 나중에 이벤트 종료 시 일괄 제거 쉬움(예: “라운드 한정 버프” 회수).  
- **저작 파이프라인**: 밸런스 담당자는 **Upgrade SO**만 늘리면 되고, 엔진 로직은 손대지 않게.

### 바로 적용(당신의 MSW/Stage2 루프에)
- 적 처치 → `GainXp(killXp)` 호출
- 레벨업 팝업(UpgradeSystem) 표시 → 선택 시 ModifiedValues 모디파이어 부착
- HUD에는 `currentDamage = stats.damage.Value`처럼 **실시간 평가 값**만 표시

원하시면 Unity 패키지 구조(폴더 레이아웃), 간단한 **에디터 템플릿**(Upgrade SO 자동 생성·아이콘/색상 프리셋), 그리고 **테스트 코드**(모디파이어 적용/제거 스냅샷 테스트)까지 한 번에 만들어 드릴게요.
