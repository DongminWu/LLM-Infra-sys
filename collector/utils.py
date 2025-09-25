import random
import os
from typing import List

def load_lines(path: str) -> List[str]:
    """读取文件，去掉空行和前后空格"""
    print(f"[LOG] 正在读取文件: {path}")
    with open(path, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        print(f"[LOG] 文件读取完成，共 {len(lines)} 行")
        return lines

def random_ua() -> str:
    """随机 UA，防止被简单反爬"""
    ua_pool = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 "
        "(KHTML, like Gecko) Version/16.4 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 "
        "(KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    ]
    return random.choice(ua_pool)

def ensure_env(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise RuntimeError(f"环境变量 {key} 未设置")
    return val