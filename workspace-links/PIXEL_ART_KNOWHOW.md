---
type: concept
tags:
  - workspace-links
created: 2026-03-25
summary: ""
---
# 🧠 픽셀 아트 프롬프트 엔지니어링 노하우 축적소

> 이 문서는 AI 이미지 생성에서 축적된 **실전 노하우**입니다.
> 에이전트가 이 문서를 참조할수록, 생성 퀄리티가 올라갑니다.

---

## 1. 스타일 앵커 테크닉

### 교훈: "Nanobanana style"처럼 추상적 키워드는 퀄리티를 보장하지 못한다
- ❌ `"Nanobanana style"` → AI가 자유 해석, 결과 편차 큼
- ✅ `"Mana Seed" inspired, Chrono Trigger SNES overworld proportions` → **실존 레퍼런스 게임명**을 앵커로 박으면 색 수, 비율, 외곽선 스타일이 자동으로 수렴

### 유효한 스타일 앵커 목록
| 앵커 | 효과 |
|---|---|
| `"Mana Seed" inspired` | 3~4색, 깔끔한 실루엣, 인디 RPG 표준 |
| `Chrono Trigger SNES overworld` | 머리:몸 1:1.5 비율, JRPG 황금기 색감 |
| `Octopath Traveler HD-2D` | 고품질 도트 + 현대적 라이팅 |
| `Eastward game style` | 부드러운 팔레트, 현대 인디 감성 |
| `Dead Cells sprite quality` | 극도로 매끄러운 프레임 전환 |

---

## 2. 부정 키워드 3중 적용 법칙

### 교훈: AI는 "예쁘게 만들려는 본능"이 있어 안티앨리어싱을 자동 삽입한다
- ❌ `no anti-aliasing` (1회) → 높은 확률로 무시됨
- ✅ `NO anti-aliasing, NO gradients, NO dithering, hard pixel edges only` → **3중 부정**으로 강제 차단

---

## 3. 캐릭터성 극대화 법칙

### 교훈: "기사, 마법사, 궁수"처럼 generic하게 쓰면 generic한 결과가 나온다

**v1 (실패)**: `"a heroic Knight wearing steel blue armor"` → 무난한 판타지 기사
**v3 (성공)**: `"overwhelmingly COOL dark knight, massive spiked shoulder armor, glowing ice-blue visor slit"` → 압도적 존재감

### 캐릭터성 극대 공식
```
[감정 형용사를 대문자로 강조] + [구체적 시각 디테일 3개 이상] + [포즈에서 성격 드러내기]
```

| 노선 | 감정 키워드 | 시각 디테일 예시 |
|---|---|---|
| 멋있음 | `overwhelmingly COOL` | 발광 바이저, 스파이크 장갑, 거대검 어깨에 걸침 |
| 예쁨 | `ethereally PRETTY` | 실버 롱헤어, 크리스탈 티아라, 별무늬 로브, 반짝이는 파티클 |
| 에지 | `dangerously EDGY` | 흉터, 빛나는 한쪽 눈, 찢어진 망토, 기계 팔 |
| 귀여움 | `irresistibly CUTE` | 큰 둥근 눈, 볼터치, 몸보다 큰 소품, 치비 비율 |
| 스타일리시 | `impossibly STYLISH` | 나부끼는 스카프, 마스크, 팔짱 포즈, 자신감 미소 |
| 광기 | `hilariously ECCENTRIC` | 뻗친 머리카락, 오버사이즈 고글, 스파크, 미친 웃음 |

---

## 4. 실루엣 우선 설계 법칙

### 교훈: 검은 실루엣만으로 직업이 구별 안 되면 디자인 실패다
- 각 클래스를 설계할 때 **실루엣 차별 포인트를 먼저 결정**한 뒤 프롬프트 작성
- 실루엣 테스트는 "solid black silhouette" 프롬프트로 검증 가능

---

## 5. 색상 통제 법칙

### 교훈: 색상 수를 명시하지 않으면 AI는 5~8색 이상을 자유롭게 사용한다
- ✅ `maximum 4 flat colors (black outline, peach skin, [primary], [secondary])` 형태로 **구체적 헥스 코드까지 명시**
- 헥스 코드를 넣으면 AI가 해당 색상 범위 안에서 작업하는 경향이 강해짐

---

## 6. 프롬프트 구조 공식 (5-Block)

모든 캐릭터 프롬프트는 아래 5블록 순서로 작성:
```
[1. 스타일 앵커] "Mana Seed" inspired, Chrono Trigger proportions
[2. 기술 제약] strict 16-bit pixel art, 1px outline, 4 colors, NO AA
[3. 캐릭터 묘사] 감정 형용사 + 시각 디테일 3개+
[4. 포즈/구도] 포즈에서 성격이 드러나게
[5. 출력 제약] solid white background, centered, game-ready asset
```

---

## 7. Image-to-Image 일관성 법칙

### 교훈: 스프라이트 시트 확장 시 반드시 `ImagePaths`에 베이스 레퍼런스를 주입
- `ImagePaths` 파라미터에 원본 이미지 경로를 배열로 삽입
- 프롬프트에 `"STRICT character consistency"`, `"EXACT character"` 키워드를 반드시 포함
- 이 두 조건 중 하나라도 빠지면 캐릭터 외형이 달라짐

---

## 8. v1 → v3 진화 기록

| 버전 | 문제 | 해결 |
|---|---|---|
| v1 | 추상적 스타일 키워드 | 실존 게임명 앵커로 교체 |
| v1 | 색상 5~8개 범람 | 4색 + 헥스코드 명시 |
| v1 | 안티앨리어싱 잔재 | 3중 부정 키워드 |
| v2 | 무난한 캐릭터성 | 감정 형용사 대문자 강조 + 시각 디테일 3개+ |
| v3 | ✅ 확실한 노선의 캐릭터성 | 완성 |

---

## 9. 인외(非人間) 캐릭터 법칙

### 교훈: 모든 캐릭터가 인간형일 필요는 없다. 오히려 비인간일수록 캐릭터성이 극대화된다

- **귀여움** → 인간 치비보다 **정령/슬라임/요정** 형태가 더 귀여울 수 있음
- **강함** → 인간 기사보다 **골렘/드래곤나이트/갑옷 입은 거대 짐승**이 더 압도적
- **예쁨** → 인간 엘프보다 **피닉스/유니콘/빛나는 나비 정령**이 더 환상적
- **에지** → 인간 로그보다 **그림자 늑대/까마귀 변신체**가 더 위험

### 설계 원칙
```
캐릭터 노선을 정한 뒤 → "이 감정을 가장 극대화하는 형태가 인간인가?" 자문
→ 아니라면 비인간 형태를 적극 채택
→ 단, 같은 파티 내에서 인간/비인간 혼재는 오히려 다양성과 매력을 높인다
```
