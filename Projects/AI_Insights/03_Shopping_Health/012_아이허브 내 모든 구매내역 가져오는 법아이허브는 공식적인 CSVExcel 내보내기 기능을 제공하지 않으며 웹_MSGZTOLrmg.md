# 아이허브 내 모든 구매내역 가져오는 법아이허브는 공식적인 CSVExcel 내보내기 기능을 제공하지 않으며 웹사이트에서 기간별 조회를 하거나 Python으로 스크래핑하는 방법을 사용해야 합니다 가장 기본적인 방법으로 전체 기간 조회가 가능합니다 1 iherbcomhttpswwwiherbcom 로그인 2 우측 상단 내 계정 클릭 3 주문Orders 페이지 이동 4 주문 검색하기 드롭다운에서 원하는 기간 선택 전체 출고 완료 진행 중 취소 필터 포함 5 특정 주문 클릭  주문 세부 정보  주문서 확인 및 인쇄 가능   주문서 조회 및 인쇄는 모바일 앱이 아닌 데스크톱PC에서만 가능합니다 iHerb에 공식 export 기능이 없으므로 기술적 접근이
URL: https://www.perplexity.ai/search/aiheobeu-nae-modeun-gumaenaeye-0iawbBzaTYiwMSGZTOLrmg

답변
링크
이미지
공유
아이허브 내 모든 구매내역 가져오는 법
2 단계 완료

아이허브는 공식적인 CSV/Excel 내보내기 기능을 제공하지 않으며, 웹사이트에서 기간별 조회를 하거나 Python으로 스크래핑하는 방법을 사용해야 합니다.

방법 1: 웹사이트에서 수동 조회

가장 기본적인 방법으로, 전체 기간 조회가 가능합니다.
wannazone.co
​

iherb.com 로그인

우측 상단 내 계정 클릭

주문(Orders) 페이지 이동

"주문 검색하기" 드롭다운에서 원하는 기간 선택 (전체, 출고 완료, 진행 중, 취소 필터 포함)
information.iherb
+1

특정 주문 클릭 → 주문 세부 정보 → 주문서 확인 및 인쇄 가능
information.iherb
​

⚠️ 주문서 조회 및 인쇄는 **모바일 앱이 아닌 데스크톱(PC)**에서만 가능합니다.
wannazone.co
​

방법 2: Python으로 전체 내역 스크래핑

iHerb에 공식 export 기능이 없으므로, 기술적 접근이 필요합니다.

Selenium 활용 (로그인 세션 유지)

python
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://www.iherb.com/signin")

# 로그인 후 주문 페이지 접근
# driver.find_element(By.ID, "email").send_keys("your@email.com")
# ...

driver.get("https://www.iherb.com/orders")
time.sleep(3)

orders = []
# 주문 목록 파싱
items = driver.find_elements(By.CSS_SELECTOR, ".order-history-item")
for item in items:
    orders.append({
        "order_id": item.find_element(By.CSS_SELECTOR, ".order-number").text,
        "date": item.find_element(By.CSS_SELECTOR, ".order-date").text,
        "total": item.find_element(By.CSS_SELECTOR, ".order-total").text,
    })

df = pd.DataFrame(orders)
df.to_csv("iherb_orders.csv", index=False)


requests + BeautifulSoup (쿠키 세션 활용)

python
import requests
from bs4 import BeautifulSoup

session = requests.Session()
# 로그인 후 세션 쿠키를 브라우저에서 복사하여 적용
session.cookies.update({"YOUR_SESSION_COOKIE": "value"})

resp = session.get("https://www.iherb.com/orders")
soup = BeautifulSoup(resp.text, "html.parser")
# 주문 데이터 파싱...

방법 3: 브라우저 개발자 도구 활용

iHerb 주문 페이지가 API 호출을 통해 데이터를 로드하는지 확인 후 직접 추출할 수 있습니다.

iHerb 주문 페이지 열기

F12 → Network 탭 → Fetch/XHR 필터

페이지 새로고침 후 주문 데이터를 반환하는 API 엔드포인트 확인 (예: /api/orders 형태)

해당 요청의 헤더(쿠키 포함)를 복사하여 Python requests로 반복 호출

이 방법이 Selenium보다 훨씬 빠르며, 페이지네이션 파라미터를 조작해 전체 기간 데이터를 한 번에 가져올 수 있습니다.

어떤 목적으로 구매 내역을 가져오려 하시나요? (가계부 정리, 재구매 목록 분석 등) 목적에 따라 더 최적화된 방법을 안내해 드릴 수 있습니다.

Claude Sonnet 4.6 Thinking(으)로 준비됨
29개 출처
후속 조치
가계부 정리 및 지출 분석 목적이에요
재구매할 제품 목록 정리하려고요
세금 신고나 영수증 보관용이에요




후속 질문하기
모델