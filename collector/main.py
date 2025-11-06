#!/usr/bin/env python3
"""
主流程：读 url 文件 -> 抓文章 -> 摘要 -> 写入 README
新增播客/换模型只需换 Fetcher/Summarizer 实现，无需改这里
"""
import sys
from pathlib import Path

from utils import load_lines
from fetcher import WechatArticleFetcher
from summarizer import Summarizer
from readme_manager import ReadmeManager, Article
import time

def main(url_file: str):
    print("[LOG] 开始读取URL文件...")
    urls = load_lines(url_file)
    print(f"[LOG] 读取到 {len(urls)} 个URL")
    
    print("[LOG] 初始化抓取器...")
    fetcher = WechatArticleFetcher()
    print("[LOG] 初始化摘要器...")
    summarizer = Summarizer()
    print("[LOG] 初始化README管理器...")
    mgr = ReadmeManager()

    print("[LOG] 开始处理URL列表...")
    for i, url in enumerate(urls, 1):
        print(f"[LOG] 正在处理第 {i}/{len(urls)} 个URL: {url}")
        try:
            print(f"[LOG] 正在抓取文章内容...")
            title, md = fetcher.fetch(url)
            print(f"[LOG] 文章标题: {title}")
            print(f"[LOG] 正在生成摘要...")
            summary = summarizer.summarize(title, md)
            print(f"[LOG] 摘要生成完成")
            art = Article(title=title, url=url, summary=summary)
            print(f"[LOG] 正在插入文章到README...")
            mgr.insert_article(art)
            print(f"[OK] {title}")\
            time.sleep(3)
        except Exception as e:
            print(f"[FAIL] {url} -> {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python main.py urls.txt")
        sys.exit(1)
    main(sys.argv[1])