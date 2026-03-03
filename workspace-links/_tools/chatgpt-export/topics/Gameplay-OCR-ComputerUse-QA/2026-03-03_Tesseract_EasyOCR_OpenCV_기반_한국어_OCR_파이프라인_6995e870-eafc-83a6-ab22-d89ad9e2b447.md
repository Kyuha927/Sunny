---
type: chatgpt-export-conversation
topic: "Gameplay-OCR-ComputerUse-QA"
title: "Tesseract + EasyOCR + OpenCV 기반 한국어 OCR 파이프라인"
conversation_id: "6995e870-eafc-83a6-ab22-d89ad9e2b447"
imported_at_utc: "2026-03-03T05:32:13+00:00"
turn_count: 2
chars: 1528
topic_score: 2
---

# Tesseract + EasyOCR + OpenCV 기반 한국어 OCR 파이프라인

- topic: `Gameplay-OCR-ComputerUse-QA`
- source: `0de9e284f70b860fe63b5e28aaddc0ee7a22bd1dab6fc430bd0bf284a7a94070-2026-02-28-12-01-06-6b187fa97d244cc5beb7efa352c5af1f.zip::conversations-000.json`
- source_txt: `/mnt/c/Users/jhk92/OneDrive/문서/GitHub/ai/Moltbot/tools/handoff/bridge_outbox_tabs/6995e870-eafc-83a6-ab22-d89ad9e2b447_Tesseract_EasyOCR_OpenCV_OCR.txt`
- conversation_id: `6995e870-eafc-83a6-ab22-d89ad9e2b447`
- matched_keywords: ocr, use
- card: [[workspace-links/_catalog/cards/Gameplay-OCR-ComputerUse-QA|게임플레이 OCR 제어 QA]]

## Summary
## 1. assistant tiered OCR pipeline Tesseract Korean EasyOCR OpenCV template matching anchor localization UI screenshots 2026 ## 2. assistant 최근 OCR(이미지에서 텍스트를 뽑는 기술) 관련 기술들을 빠르게 조합해서 *더 정확하고 안정적인 한국어 UI 텍스트 추출 파이프라인*을 만드는 흐름이 부상하고 있어요. 기본 OCR만으로는 잡음 많고 UI 화면처럼 복잡한 스크린샷에서 원하는 텍스트를 추출하기 어려운 경우가 많기 때문입니다. citeturn0search0turn0search1 image_group{"layo...

## Transcript

## 1. assistant

tiered OCR pipeline Tesseract Korean EasyOCR OpenCV template matching anchor localization UI screenshots 2026

## 2. assistant

최근 OCR(이미지에서 텍스트를 뽑는 기술) 관련 기술들을 빠르게 조합해서 *더 정확하고 안정적인 한국어 UI 텍스트 추출 파이프라인*을 만드는 흐름이 부상하고 있어요. 기본 OCR만으로는 잡음 많고 UI 화면처럼 복잡한 스크린샷에서 원하는 텍스트를 추출하기 어려운 경우가 많기 때문입니다. citeturn0search0turn0search1

image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Tesseract OCR Korean OCR screenshot result","EasyOCR Korean text recognition example","OpenCV template matching example code","hybrid OCR pipeline python"]}

📌 **Tesseract OCR**  
구글이 개발을 주도하는 오픈소스 OCR 엔진으로 한국어를 포함한 다국어 인식이 가능해요. 4.x부터 LSTM 기반 엔진이 추가되어 문자 인식 능력이 크게 향상되었습니다. 하지만 이미지가 복잡하거나 품질이 낮으면 결과가 부정확할 수 있습니다. citeturn0search20

🧠 **EasyOCR**  
EasyOCR은 CRAFT 텍스트 탐지 + CRNN 기반 문자 인식 모델을 사용해서 다양한 언어(70개 이상)와 복잡한 레이아웃에서도 비교적 견고하게 작동합니다. 특히 잡음 많고 대비 떨어지는 UI 캡처에서도 더 잘 인식하는 경향이 있어요. citeturn0search1turn0search12

🧩 **OpenCV 템플릿 매칭**  
`cv2.matchTemplate()` 같은 기능으로 이미지에서 특정 UI 요소(예: Play 메뉴 같은 UI 앵커)를 찾아내고 그 영역만 잘라서 OCR에 넘기면 *원치 않는 다른 화면 요소를 피할 수 있는 안정성*이 생깁니다. 이 방식은 실제 Python + OpenCV OCR 튜토리얼에서도 많이 사용됩니다. citeturn0search3turn0search7

⚙️ **실용적인 하이브리드 전략 요약**  
1) OpenCV 템플릿 매칭으로 관심 영역(ROI)을 *미리 찾는다*.  
2) 그 ROI만 Tesseract로 빠르게 OCR 시도.  
3) Tesseract 결과가 신뢰할 수 없으면 EasyOCR로 *Fallback* 처리.  
4) 둘 다 실패하면 디버그 이미지 + 로깅으로 문제 확인. citeturn0search10

이런 *계층적 OCR 흐름*은 스크린샷처럼 잡음 많고 구조가 정해지지 않은 이미지에서 한글 UI 텍스트를 더 안정적으로 추출하는 데 실제로 쓰이고 있고, 커뮤니티에서도 좋은 성능을 얻는 팁으로 많이 언급되고 있어요. citeturn0search0turn0search1
