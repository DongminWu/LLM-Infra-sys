#!/usr/bin/env python3
"""
测试修改后的 WechatArticleFetcher
"""
from fetcher import WechatArticleFetcher

def test_fetcher():
    # 从urls.txt文件中读取URL进行测试
    try:
        with open("urls.txt", "r", encoding="utf-8") as f:
            test_urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("urls.txt文件未找到，使用示例URL进行测试")
        # 这里可以放一个真实的微信公众号链接用于测试（如果有的话）
        test_urls = []
    
    if not test_urls:
        print("没有找到测试URL，跳过功能测试")
        print("创建WechatArticleFetcher实例以测试初始化...")
        try:
            fetcher = WechatArticleFetcher()
            print("WechatArticleFetcher初始化成功")
            # 简单测试浏览器是否正常工作
            fetcher.driver.get("https://www.baidu.com")
            print("浏览器访问测试页面成功")
            del fetcher
        except Exception as e:
            print(f"WechatArticleFetcher初始化失败: {e}")
        return
    
    fetcher = WechatArticleFetcher()
    
    for url in test_urls:
        try:
            print(f"正在测试URL: {url}")
            title, content = fetcher.fetch(url)
            print(f"成功获取文章: {title}")
            print(f"内容长度: {len(content)}")
            print("-" * 50)
        except Exception as e:
            print(f"获取文章失败: {e}")
    
    # 手动清理浏览器实例
    import time
    time.sleep(2)  # 等待一些时间确保操作完成
    del fetcher

if __name__ == "__main__":
    test_fetcher()