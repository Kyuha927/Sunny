# 퍼플렉시티 대화내역 모두 내보내는 법퍼플렉시티에서는 대화내역 전체 일괄 내보내기계정 전체 export 기능은 아직 없고 각 스레드대화방 단위로만 내보내기가 가능합니다 1 왼쪽의 History기록  라이브러리 아이콘을 눌러 내보내고 싶은 스레드를 엽니다 2 스레드 상단또는 각 답변 박스 하단에 있는 Export 버튼을 클릭합니다 3 원하는 포맷을 선택합니다 PDF Markdown DOCX 등 지원 포맷 선택 가능 이렇게 하면 해당 스레드의 답변필요 시 전체 대화 맥락 포함을 파일로 저장할 수 있습니다 현재 헬프 센터 기준으로 모든 History를 한 번에 파일로 받는 기능은 안내되어 있지 않습니다 여러 스레드를 백업하려면 History에서 하나씩 열고 Export를
URL: https://www.perplexity.ai/search/peopeulregsiti-daehwanaeyeog-m-OAK_90i8RvWMnwSNXTDFUg

답변
링크
이미지
비디오
공유
퍼플렉시티 대화내역 모두 내보내는 법
1 단계 완료

퍼플렉시티에서는 “대화내역 전체 일괄 내보내기(계정 전체 export)” 기능은 아직 없고, 각 스레드(대화방) 단위로만 내보내기가 가능합니다.
perplexity
​

개별 스레드 내보내기 방법

왼쪽의 History(기록 / 라이브러리) 아이콘을 눌러 내보내고 싶은 스레드를 엽니다.
perplexity
​

스레드 상단(또는 각 답변 박스 하단)에 있는 Export 버튼을 클릭합니다.
perplexity
+1

원하는 포맷을 선택합니다.

PDF

Markdown

DOCX 등 지원 포맷 선택 가능.
perplexity
+1

이렇게 하면 해당 스레드의 답변(필요 시 전체 대화 맥락 포함)을 파일로 저장할 수 있습니다.
perplexity
+1

전체 대화내역 일괄 백업을 원할 때

현재 헬프 센터 기준으로, “모든 History를 한 번에 파일로 받는 기능”은 안내되어 있지 않습니다.
perplexity
+1

여러 스레드를 백업하려면:

History에서 하나씩 열고 Export를 반복하거나

브라우저 자동화(예: Selenium, Playwright)로 Export 클릭을 스크립트로 반복하는 방법 정도만 가능합니다.

Deep Research / Assets 사용 시

Deep Research 결과나 Create files and apps로 만든 문서는 자체적으로 Export 기능(PDF, DOCX, PPTX, XLSX 등) 을 지원합니다.
perplexity
+2

이 경우에도 개별 결과/파일 단위 Export이므로, 계정 전체 히스토리 일괄 Export와는 별개입니다.
perplexity
+1

원하시면 “브라우저 자동화로 History 전부 export 하는 스크립트 설계” 식으로 워크플로우를 같이 짜 드릴 수 있습니다.

11개 출처
확장프로그램 통해서라도 실행
1 단계 완료

확장프로그램(크롬 익스텐션)으로도 퍼플렉시티 대화내역을 직접 일괄-export 해주는 공식 기능/도구는 아직 없습니다.
perplexity
+1

현재 가능한 방향

Comet 브라우저 + 확장프로그램 활용

퍼플렉시티는 Comet이라는 크로뮴 기반 브라우저에서 일반 크롬 확장프로그램 사용을 지원합니다.
comet-help.perplexity
+1

따라서 아래처럼 “일반 브라우저 자동화용 확장/스크립트”를 조합해서 반자동으로 처리할 수 있습니다.

현실적인 워크플로우(개발자 관점)

History(https://www.perplexity.ai/library)를 연 상태에서:

(1) 탭/윈도우 매니저 계열 확장으로 스레드 링크들을 한 번에 새 탭으로 연 뒤

(2) Tampermonkey 같은 사용자 스크립트 확장이나 Selenium / Playwright 같은 외부 자동화 스크립트로

각 탭에서 .Export 버튼 클릭

포맷(PDF/Markdown/DOCX) 선택

다운로드 완료까지 대기

탭 닫기

를 루프 돌리는 방식으로 사실상 “전체 백업에 가까운” 동작을 만들 수 있습니다.
perplexity
+1

한계 사항

헬프센터 기준으로 공식 API나 “모든 Threads를 한 번에 파일로 받는 엔드포인트/기능”은 문서화되어 있지 않습니다.
perplexity
+1

결국 지금은 UI 상의 Export 기능을 자동으로 반복 트리거하는 방식밖에 없습니다.
perplexity
​

원하시면

크롬(또는 Comet)에서 동작하는 사용자 스크립트(예: Tampermonkey용 JS) 나

Playwright / Selenium 스크립트 (Python/TS) 형태로

History에서 N개 스레드 URL 수집

새 탭 열기 → Export 클릭 → 다운로드 완료 감지
를 수행하는 샘플 코드를 구체적으로 짜 드릴 수 있습니다.

11개 출처
크롬 확장중에 찾아서 실행
4 단계 완료

크롬 웹스토어에서 찾은 퍼플렉시티 대화내역 일괄 export 확장 두 가지입니다.

✅ 추천 1: Perplexity to Notion – Batch Export

크롬 웹스토어 링크
chromewebstore.google
​

2,000명 사용 / 평점 4.5★

핵심 기능:

전체 퍼플렉시티 대화내역 Notion으로 일괄 Batch Export
chatgpt2notion
​

Markdown 파일로 다운로드 (Obsidian 호환)

Spaces별 필터링 후 export 가능

날짜 범위 지정 가능

자동 예약 동기화 (스케줄 설정)

브라우저 내 처리 (서버로 데이터 전송 없음)

단점: Notion 계정 연동 필요, Markdown 로컬 저장은 별도

✅ 추천 2: Perplexity Exporter – Extract chat convos easily

크롬 웹스토어 링크
chromewebstore.google
​

핵심 기능:

Markdown / TXT / JSON / CSV 형식으로 로컬 저장
extpose
​

Notion 없이도 로컬로만 저장 가능

체크박스로 원하는 대화만 선택적 export

단점: 2025년 7월 리뷰 기준 업데이트가 중단된 것 같다는 사용자 보고 있음
extpose
​

✅ 보너스: Save my Chatbot – AI Conversation Exporter

크롬 웹스토어 링크
chromewebstore.google
​

ChatGPT, Claude, Perplexity 등 여러 AI를 통합 export

Markdown 형식 저장

설치 후 사용 순서 (Batch Export 기준)

위 링크에서 Chrome에 추가 클릭

퍼플렉시티 라이브러리(perplexity.ai/library) 접속

확장 아이콘 클릭 → Notion 연동 or Markdown 다운로드 선택

Batch Export 실행 → 전체 대화 일괄 저장

Notion 없이 로컬 Markdown만 원하신다면 Perplexity Exporter가 더 간단합니다.

5개 출처
크롬이 아니라서 안되나? 이것도 연결안되었다뜨네
무료인데 벌크 익스포트 가능한 확장
노션에서 엠디파일로 벌크 익스포트가 돼?




후속 질문하기