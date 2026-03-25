# 여기서 이미지를 업로드하고 매칭되는 오디오를 올리고 맞는 프롬프트를 입력하며 여러 영상을 생성하는 자동화현재 페이지는 Kling AI의 디지털 캐릭터AI Human 기능으로 이미지  오디오  프롬프트를 입력해 영상을 생성하는 구조입니다 왼쪽 사이드바에 API 메뉴가 있으므로 공식 API를 사용하는 것이 가장 안정적입니다 Kling AI API Key 사이드바 API 탭에서 발급 이미지 파일 목록 얼굴 사진 jpgpng 오디오 파일 목록 mp3wav 프롬프트 목록 import requests import time import json from pathlib import Path API_KEY  YOUR_KLING_API_KEY BASE_URL  httpsapiklingaicom HEADERS   Authorization
URL: https://www.perplexity.ai/search/yeogiseo-imijireul-eobrodeuhag-uyZjr_0nT.e4xBPV.f57Xg

답변
링크
이미지
비디오
공유
여기서 이미지를 업로드하고, 매칭되는 오디오를 올리고, 맞는 프롬프트를 입력하며 여러 영상을 생성하는 자동화
1 단계 완료
Kling AI 디지털 캐릭터 영상 자동 생성 자동화

현재 페이지는 Kling AI의 디지털 캐릭터(AI Human) 기능으로, 이미지 + 오디오 + 프롬프트를 입력해 영상을 생성하는 구조입니다.
app.klingai
​

방법 1: Kling AI 공식 API 활용 (권장)

왼쪽 사이드바에 API 메뉴가 있으므로, 공식 API를 사용하는 것이 가장 안정적입니다.
app.klingai
​

준비물

Kling AI API Key (사이드바 API 탭에서 발급)

이미지 파일 목록 (얼굴 사진 .jpg/.png)

오디오 파일 목록 (.mp3/.wav)

프롬프트 목록

Python 자동화 스크립트
python
import requests
import time
import json
from pathlib import Path

# ── 설정 ──────────────────────────────────────────
API_KEY = "YOUR_KLING_API_KEY"
BASE_URL = "https://api.klingai.com"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
}

# 작업 목록: 이미지, 오디오, 프롬프트를 쌍으로 정의
TASKS = [
    {
        "image": "images/face1.jpg",
        "audio": "audios/voice1.mp3",
        "prompt": "안녕하세요! 오늘 날씨가 정말 좋네요.",
    },
    {
        "image": "images/face2.jpg",
        "audio": "audios/voice2.mp3",
        "prompt": "저는 AI 캐릭터입니다. 잘 부탁드립니다.",
    },
    {
        "image": "images/face3.jpg",
        "audio": "audios/voice3.mp3",
        "prompt": "오늘도 열심히 해봅시다!",
    },
]

# ── 파일 업로드 함수 ───────────────────────────────
def upload_file(file_path: str, file_type: str) -> str:
    """이미지 또는 오디오 파일을 업로드하고 URL/ID 반환"""
    with open(file_path, "rb") as f:
        files = {"file": (Path(file_path).name, f)}
        resp = requests.post(
            f"{BASE_URL}/v1/files/upload",
            headers=HEADERS,
            files=files,
            params={"type": file_type},  # "image" or "audio"
        )
    resp.raise_for_status()
    return resp.json()["data"]["url"]  # 또는 file_id


# ── 영상 생성 요청 함수 ────────────────────────────
def create_ai_human_video(image_url: str, audio_url: str, prompt: str) -> str:
    """디지털 캐릭터 영상 생성 요청, task_id 반환"""
    payload = {
        "image_url": image_url,
        "audio_url": audio_url,
        "prompt": prompt,
        "resolution": "720p",
        "fps": 30,
    }
    resp = requests.post(
        f"{BASE_URL}/v1/ai-human/video",
        headers={**HEADERS, "Content-Type": "application/json"},
        json=payload,
    )
    resp.raise_for_status()
    task_id = resp.json()["data"]["task_id"]
    print(f"  → 작업 생성됨: {task_id}")
    return task_id


# ── 작업 상태 폴링 함수 ────────────────────────────
def poll_task(task_id: str, interval: int = 10, timeout: int = 600) -> dict:
    """완료될 때까지 상태 확인 후 결과 반환"""
    elapsed = 0
    while elapsed < timeout:
        resp = requests.get(
            f"{BASE_URL}/v1/tasks/{task_id}",
            headers=HEADERS,
        )
        resp.raise_for_status()
        data = resp.json()["data"]
        status = data["status"]
        print(f"  [{task_id}] 상태: {status} ({elapsed}s 경과)")

        if status == "succeed":
            return data
        elif status == "failed":
            raise RuntimeError(f"작업 실패: {data.get('fail_reason')}")

        time.sleep(interval)
        elapsed += interval

    raise TimeoutError(f"타임아웃: {task_id}")


# ── 결과 다운로드 함수 ─────────────────────────────
def download_video(video_url: str, save_path: str):
    resp = requests.get(video_url, stream=True)
    resp.raise_for_status()
    with open(save_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"  저장 완료: {save_path}")


# ── 메인 실행 ──────────────────────────────────────
def main():
    results = []

    for i, task in enumerate(TASKS):
        print(f"\n[{i+1}/{len(TASKS)}] 작업 시작: {task['image']}")

        # 1. 파일 업로드
        print("  이미지 업로드 중...")
        image_url = upload_file(task["image"], "image")

        print("  오디오 업로드 중...")
        audio_url = upload_file(task["audio"], "audio")

        # 2. 영상 생성 요청
        print("  영상 생성 요청 중...")
        task_id = create_ai_human_video(image_url, audio_url, task["prompt"])
        results.append({"task_id": task_id, "index": i})

    print("\n\n모든 작업 제출 완료. 결과 대기 중...\n")

    # 3. 병렬로 완료 대기 및 다운로드
    for result in results:
        i = result["index"]
        task_id = result["task_id"]
        print(f"\n[{i+1}] 완료 대기: {task_id}")
        try:
            data = poll_task(task_id)
            video_url = data["works"][0]["resource"]["resource"]
            save_path = f"output/video_{i+1:03d}.mp4"
            Path("output").mkdir(exist_ok=True)
            download_video(video_url, save_path)
        except Exception as e:
            print(f"  오류 발생: {e}")

    # 4. 결과 저장
    with open("output/results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\n완료! output/ 폴더를 확인하세요.")


if __name__ == "__main__":
    main()

방법 2: Selenium/Playwright UI 자동화

API 키 없이 브라우저를 직접 제어하는 방식입니다.

python
from playwright.async_api import async_playwright
import asyncio
from pathlib import Path

TASKS = [
    {"image": "images/face1.jpg", "audio": "audios/voice1.mp3", "prompt": "안녕하세요!"},
    {"image": "images/face2.jpg", "audio": "audios/voice2.mp3", "prompt": "반갑습니다!"},
]

async def run():
    async with async_playwright() as p:
        # 기존 브라우저 세션 재사용 (로그인 상태 유지)
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = context.pages[0]

        for i, task in enumerate(TASKS):
            print(f"\n[{i+1}] 작업 시작")
            await page.goto("https://app.klingai.com/global/ai-human/new?trackName=digital_human&ac=4")
            await page.wait_for_load_state("networkidle")

            # 이미지 업로드
            img_input = page.locator('input[type="file"][accept*="image"]').first
            await img_input.set_input_files(task["image"])
            await page.wait_for_timeout(2000)

            # 오디오 업로드 버튼 클릭
            await page.get_by_text("오디오 업로드").click()
            audio_input = page.locator('input[type="file"][accept*="audio"]').first
            await audio_input.set_input_files(task["audio"])
            await page.wait_for_timeout(2000)

            # 프롬프트 입력
            prompt_box = page.locator('textarea, [placeholder*="멘트"]').first
            await prompt_box.fill(task["prompt"])

            # 생성 버튼 클릭
            await page.get_by_text("생성").click()
            print(f"  생성 요청 완료!")

            # 다음 작업 전 대기 (크레딧 소모 방지)
            await page.wait_for_timeout(3000)

asyncio.run(run())


Playwright 실행 방법:

bash
pip install playwright
playwright install chromium
# Chrome을 디버그 모드로 실행 (기존 로그인 세션 사용)
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/Users/YourName/AppData/Local/Google/Chrome/User Data"
python script.py

방법 비교
항목	API 방식	Playwright UI 방식
안정성	높음	중간 (UI 변경에 취약)
속도	빠름 (병렬 가능)	느림 (순차적)
설정 난이도	API 키 필요	브라우저 세션 필요
비용 추적	쉬움	어려움
권장 워크플로우
text
tasks.json (이미지/오디오/프롬프트 목록)
    ↓
upload_files() → 이미지·오디오 URL 획득
    ↓
create_video() × N → task_id 목록 (병렬 제출)
    ↓
poll_all_tasks() → 완료 대기
    ↓
download_videos() → output/ 폴더에 저장


tasks.json 형식으로 작업 목록을 관리하면 수십 개의 영상도 한 번에 자동 처리할 수 있습니다. API 엔드포인트 세부 사항은 Kling AI 사이드바의 API 탭에서 최신 문서를 확인하세요.

1개 출처




후속 질문하기