#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, urljoin

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md
except ImportError:
    print("⚠️  pip install requests beautifulsoup4 markdownify 가 필요합니다.")
    sys.exit(1)

try:
    from obsidian_agent_tools import write_lesson_learned
except ImportError:
    print("⚠️  obsidian_agent_tools.py 를 찾을 수 없습니다.")
    sys.exit(1)

# Paths
VAULT_DIR = Path("/home/khyha/projects/Sunny")
DISCOVER_DIR = VAULT_DIR / "Google Discover"
CONFIG_FILE = DISCOVER_DIR / "sites.json"
SCRAPED_FILE = DISCOVER_DIR / ".scraped_urls"
INPUT_FILE = Path.home() / "sync" / "tasker" / "google_discover.jsonl"

def load_config() -> dict:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"allowed_domains": [], "blocked_domains": [], "blocked_keywords": [], "sites": {}}

def load_scraped_urls() -> set:
    if SCRAPED_FILE.exists():
        return set(SCRAPED_FILE.read_text().strip().splitlines())
    return set()

def save_scraped_url(url: str):
    with open(SCRAPED_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{url}\n")

def is_valid_article(title: str, url: str, config: dict) -> bool:
    domain = urlparse(url).netloc.replace("www.", "") if url else ""
    if any(bd in domain for bd in config.get("blocked_domains", [])):
        return False
    if title:
        for kw in config.get("blocked_keywords", []):
            if kw in title:
                return False
    return True

def fetch_and_parse(url: str, site_config: dict) -> str:
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        content_html = ""
        selector = site_config.get("content_selector")
        if selector:
            elements = soup.select(selector)
            if elements:
                content_html = "".join(str(el) for el in elements)
        
        if not content_html:
            for tag in soup(['nav', 'header', 'footer', 'script', 'style', 'aside', 'iframe', '.ad', '#ad']):
                tag.decompose()
            article = soup.find('article')
            if article:
                content_html = str(article)
            else:
                body = soup.find('body')
                content_html = str(body) if body else response.text
                
        markdown_text = md(content_html, heading_style="ATX", escape_asterisks=False)
        return re.sub(r'\n{3,}', '\n\n', markdown_text).strip()
    except Exception as e:
        print(f"⚠️  스크래핑 실패 ({url}): {e}")
        return ""

def generate_ontology_note(title: str, url: str, content: str, source: str, date_str: str, auto_enrich: bool = False):
    folder_path = "Google Discover/Articles"
    safe_title = re.sub(r'[\\/?*:"<>|]', "", title).strip()
    if len(safe_title) > 50:
        safe_title = safe_title[:50] + "..."
        
    full_content = f"> **출처**: {source} | **날짜**: {date_str} | [원문 링크]({url})\n\n---\n\n{content}\n\n---\n_Scraped by Agent at {datetime.now().strftime('%Y-%m-%d %H:%M')}_"
    tags = ["google-discover", "article", source.lower().replace(" ", "-").replace(".", "")]
    
    try:
        result = write_lesson_learned(
            folder_path, safe_title, full_content, tags=tags,
            note_type="reference", auto_enrich=auto_enrich
        )
        print(f"✅  노트 생성됨: {safe_title}")
    except Exception as e:
        print(f"⚠️  노트 생성 실패: {e}")

def scrape_latest(config: dict, scraped: set) -> int:
    """latest_only 모드인 사이트를 크롤링하여 최신글 가져오기"""
    print("\n🌐  팔로우 중인 사이트의 최신글을 수집합니다...")
    count = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    for domain, site in config.get("sites", {}).items():
        if site.get("mode") == "latest_only":
            url = site.get("url")
            source_name = site.get("name", domain)
            selector = site.get("content_selector")
            print(f"  [최신글 수집] {source_name} ({url})")
            try:
                # GeekNews 특화: topic_row 안의 링크들 추출
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 메인 페이지에서 각 토픽 링크 수집 (최대 5개)
                links = soup.select(".topictitle a")[:5]
                for a_tag in links:
                    article_url = urljoin(url, a_tag['href'])
                    title = a_tag.text.strip()
                    
                    if article_url in scraped:
                        continue
                        
                    print(f"    ⏳ 스크래핑: {title}...")
                    
                    # 상세 페이지 접속
                    article_resp = requests.get(article_url, headers=headers, timeout=10)
                    article_soup = BeautifulSoup(article_resp.text, 'html.parser')
                    
                    # 본문 찾기 (.article 또는 .topic_content 등)
                    content_html = ""
                    if selector:
                        elements = article_soup.select(selector)
                        if elements:
                            content_html = "".join(str(el) for el in elements)
                            
                    if not content_html:
                        content_html = str(article_soup)
                        
                    markdown_text = md(content_html, heading_style="ATX", escape_asterisks=False)
                    content = re.sub(r'\n{3,}', '\n\n', markdown_text).strip()
                    
                    if content and len(content) > 50:
                        generate_ontology_note(title, article_url, content, source_name, date_str,
                                              auto_enrich=getattr(args, 'enrich', False) if 'args' in dir() else False)
                        count += 1
                        
                    save_scraped_url(article_url)
                    scraped.add(article_url)
            except Exception as e:
                print(f"  ⚠️  최신글 수집 실패 ({source_name}): {e}")
                
    return count

def main():
    parser = argparse.ArgumentParser(description="Google Discover 전문 기사 스크래퍼 + 최신글 수집기")
    parser.add_argument("--input", "-i", type=Path, default=INPUT_FILE, help="알림 JSONL 파일")
    parser.add_argument("--skip-feeds", action="store_true", help="알림만 처리하고 최신글(latest) 수집은 건너뜀")
    parser.add_argument("--enrich", action="store_true", help="AI 보강 (Gemini로 요약+엔티티+WikiLink 자동 삽입)")
    args = parser.parse_args()
    
    config = load_config()
    scraped = load_scraped_urls()
    
    count_scraped = 0
    count_skipped = 0
    
    if args.input.exists():
        print(f"🔍  {args.input} 알림 로그 분석 중...")
        with open(args.input, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                try:
                    entry = json.loads(line)
                    url = entry.get("url")
                    title = entry.get("title", "제목 없음")
                    date_str = entry.get("date", datetime.now().strftime("%Y-%m-%d"))
                    source = entry.get("source") or (urlparse(url).netloc.replace("www.", "") if url else "Unknown")
                    
                    if not url:
                        continue
                        
                    if url in scraped:
                        continue
                        
                    if not is_valid_article(title, url, config):
                        print(f"  ⏭️  뉴스 필터링 됨: {title} ({source})")
                        count_skipped += 1
                        save_scraped_url(url)
                        scraped.add(url)
                        continue
                        
                    print(f"  ⏳  스크래핑 중: {title}...")
                    domain = urlparse(url).netloc.replace("www.", "")
                    site_config = config.get("sites", {}).get(domain, {})
                    
                    content = fetch_and_parse(url, site_config)
                    
                    if content and len(content) > 50:
                        source_name = site_config.get("name", source)
                        generate_ontology_note(title, url, content, source_name, date_str,
                                              auto_enrich=args.enrich)
                        count_scraped += 1
                    
                    save_scraped_url(url)
                    scraped.add(url)
                    
                except json.JSONDecodeError:
                    pass
                except Exception as e:
                    print(f"  ❌ 에러: {e}")
    
    # 팔로우 사이트 최신글 수집
    if not args.skip_feeds:
        count_scraped += scrape_latest(config, scraped)
                
    print(f"\n✨ 완료! 총 {count_scraped}개 기사 생성, {count_skipped}개 알림 필터링 됨.")

if __name__ == "__main__":
    main()
