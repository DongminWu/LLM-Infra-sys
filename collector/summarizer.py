import openai
import json
import os
from utils import ensure_env

class Summarizer:
    """
    大模型摘要器，基于 OpenAI，后续可派生 ClaudeSummarizer 等
    """

    def __init__(self, config_path="llm_config.json"):
        print(f"[LOG] 初始化摘要器...")
        # 从配置文件读取设置
        if os.path.exists(config_path):
            print(f"[LOG] 从配置文件加载LLM设置: {config_path}")
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        
        api_key = config.get("OPENAI_API_KEY")
        base_url = config.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
        model = config.get("OPENAI_MODEL", "gpt-3.5-turbo")
        
        print(f"[LOG] 使用模型: {model}")
        print(f"[LOG] API基础URL: {base_url}")
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = model
        print(f"[LOG] 摘要器初始化完成")

    def summarize(self, title: str, markdown_body: str) -> str:
        """返回一段 120~150 字的中文简介"""
        print(f"[LOG] 开始生成文章摘要: {title}")
        print(f"[LOG] 正文长度: {len(markdown_body)} 字符")
        prompt = f"""
请用中文为以下技术文章写一段 120~150 字的简介，要求信息密度高、客观、准确：
标题：{title}
正文：
{markdown_body}
"""
        print(f"[LOG] 向LLM发送摘要请求...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=200
        )
        summary = response.choices[0].message.content.strip()
        print(f"[LOG] 摘要生成完成，长度: {len(summary)} 字符")
        return summary