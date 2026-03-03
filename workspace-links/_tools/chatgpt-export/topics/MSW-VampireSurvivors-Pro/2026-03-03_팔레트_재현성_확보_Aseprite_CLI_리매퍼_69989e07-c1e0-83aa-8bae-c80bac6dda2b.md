---
type: chatgpt-export-conversation
topic: "MSW-VampireSurvivors-Pro"
title: "팔레트 재현성 확보: Aseprite + CLI 리매퍼"
conversation_id: "69989e07-c1e0-83aa-8bae-c80bac6dda2b"
imported_at_utc: "2026-03-03T05:32:13+00:00"
turn_count: 1
chars: 2912
topic_score: 2
---

# 팔레트 재현성 확보: Aseprite + CLI 리매퍼

- topic: `MSW-VampireSurvivors-Pro`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/69989e07-c1e0-83aa-8bae-c80bac6dda2b_Aseprite_CLI.txt`
- conversation_id: `69989e07-c1e0-83aa-8bae-c80bac6dda2b`
- matched_keywords: pro, 프로
- card: [[workspace-links/_catalog/cards/MSW-VampireSurvivors-Pro|MSW 실험 트랙]]

## Summary
## 1. assistant 여기, **사이드스크롤러 픽셀 아트 자산에 “단일 고정 팔레트”를 강제로 맞추는 초간단 레시피**예요—로컬에선 Aseprite로 눈으로 확인하고, CI에선 Pillow+NumPy로 100% 재현 가능한 리매핑을 돌리면 끝입니다. --- # 왜 이렇게 하나요? - **아티스트 작업(수동 확인)**: Aseprite 스크립트/CLI로 빠르게 팔레트 적용·시각 QA. citeturn0search0turn0search28 - **빌드(자동/결정적)**: GUI 상태나 버전에 흔들리지 않도록 **순수 숫자 연산**으로 최근접 팔레트 매핑 → 매 빌드 동일 결과. (Pillow 이미지/팔레트 개념 참고) ...

## Transcript

## 1. assistant

여기, **사이드스크롤러 픽셀 아트 자산에 “단일 고정 팔레트”를 강제로 맞추는 초간단 레시피**예요—로컬에선 Aseprite로 눈으로 확인하고, CI에선 Pillow+NumPy로 100% 재현 가능한 리매핑을 돌리면 끝입니다.

---

# 왜 이렇게 하나요?
- **아티스트 작업(수동 확인)**: Aseprite 스크립트/CLI로 빠르게 팔레트 적용·시각 QA. citeturn0search0turn0search28  
- **빌드(자동/결정적)**: GUI 상태나 버전에 흔들리지 않도록 **순수 숫자 연산**으로 최근접 팔레트 매핑 → 매 빌드 동일 결과. (Pillow 이미지/팔레트 개념 참고) citeturn0search3turn0search7turn0search35

---

# A. 로컬 확인: Aseprite 배치 체크(수동/시각 QA)
1) 커뮤니티 팔레트 리덕션 스크립트 설치(`palettize.lua`).  
2) 프로젝트 파일에 스크립트를 적용해 결과를 새 파일로 저장.

```bash
aseprite -b project.aseprite \
  --script palettize.lua \
  --save-as project.remapped.aseprite
```

- `-b/--batch`에서 **스크립트 실행**과 **다른 이름으로 저장**이 가능합니다. citeturn0search0turn0search28  
- `palettize.lua` 설치/사용 안내(프로젝트 폴더에 복사 → 스크립트 리스캔). citeturn0search2turn0search10

원하면 Aseprite CLI로 PNG/스프라이트시트도 일괄 내보낼 수 있어요. citeturn0search0turn0search12turn0search24

---

# B. CI 고정: 결정적 팔레트 리매퍼(Python+Pillow+NumPy)
아래 스크립트를 `tools/remap_to_palette.py`로 저장하고, **기준 팔레트 이미지**(예: `palette.png`)를 만들어 둔 뒤 다음처럼 호출하세요:

```bash
python tools/remap_to_palette.py palette.png src.png out.png
```

```python
# tools/remap_to_palette.py
from PIL import Image
import numpy as np
import sys

def load_palette(pal_path):
    p = Image.open(pal_path).convert('RGBA')
    arr = np.array(p)
    cols, seen = [], set()
    for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
            rgba = tuple(int(v) for v in arr[y, x])
            if rgba not in seen:
                seen.add(rgba); cols.append(rgba)
    return np.array(cols, dtype=np.int32)

def remap(pal_path, src_path, out_path):
    pal = load_palette(pal_path)[:256]  # 256색 제한
    img = Image.open(src_path).convert('RGBA')
    a = np.array(img, dtype=np.int32)
    h, w = a.shape[:2]
    pixels = a[:, :, :3].reshape(-1, 3)
    p = pal[:, :3]
    dif = pixels[:, None, :] - p[None, :, :]
    d2 = (dif * dif).sum(axis=2)       # RGB 유클리드 거리^2
    idx = d2.argmin(axis=1).astype(np.uint8)
    out = Image.fromarray(p[idx].reshape(h, w, 3).astype(np.uint8), mode='RGB')
    out.save(out_path, optimize=True)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('usage: remap_to_palette.py palette.png src.png out.png'); sys.exit(2)
    remap(sys.argv[1], sys.argv[2], sys.argv[3])
```

- Pillow의 `Image`/팔레트 동작 개요(팔레트 모드 P, 변환 시 주의). citeturn0search3turn0search7turn0search31  
- 이 방식은 **난수·클러스터링 없이** RGB 최근접만 쓰므로, **입력 같으면 항상 같은 출력**을 보장합니다.

---

# 팀 적용 체크리스트
- **원천 자산 규칙**: 모든 최종 PNG는 `palette.png` 기준으로 리매핑 후 아틀라스에 포함.  
- **PR 게이트**: CI에서 임시 산출물과 리매핑 결과의 바이트 동일성 검사(비결정 연산 없음).  
- **로컬 QA**: 아티스트는 Aseprite 스크립트로 시각 확인 후 `.aseprite`/PNG 커밋. (CLI 플래그·스크립팅은 공식 문서 참고) citeturn0search0turn0search1turn0search9  
- **확장**: 고급 팔레트 적용/감산 스크립트도 커뮤니티에 다수 존재합니다. citeturn0search6turn0search14

---

원하시면 **GitHub Actions용 샘플 워크플로우**(리매퍼 실행 → 산출물 업로드 → 아틀라스 빌드)까지 바로 붙여 드릴게요.
