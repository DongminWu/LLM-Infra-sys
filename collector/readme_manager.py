import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict

class Article:
    def __init__(self, title: str, url: str, summary: str, date: str = None):
        self.title = title
        self.url = url
        self.summary = summary
        self.date = date or datetime.now().strftime("%Y%m%d")

class ReadmeManager:
    """
    负责读写 README.md，对外只暴露 insert_article
    内部自动按月份分组、插入到最前、持久化
    """

    def __init__(self, path: str = "../README.md"):
        self.path = Path(path)

    # -------------------- 对外唯一 API --------------------
    def insert_article(self, article: Article):
        """幂等插入：若月份不存在则新建月份，否则插入到该月最前面"""
        print(f"[LOG] 开始插入文章到README: {article.title}")
        lines = self._load_lines()
        ym = article.date[:6]  # 202509
        print(f"[LOG] 文章日期: {ym}")
        lines = self._insert_or_create_month(lines, ym, article)
        print(f"[LOG] 保存README文件")
        self._save(lines)
        print(f"[LOG] 文章插入完成: {article.title}")

    # -------------------- 内部细节 --------------------
    def _load_lines(self) -> List[str]:
        if not self.path.exists():
            return ["# LLM-AI-Infra-system 好文分享\n"]
        return self.path.read_text(encoding="utf-8").splitlines()

    def _save(self, lines: List[str]):
        self.path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def _insert_or_create_month(self, lines: List[str], ym: str, article: Article) -> List[str]:
        """找到或创建 ## 202509 段落，并把文章插到该段落最前面"""
        ym_header = f"## {ym}"
        new_entry = self._format_entry(article)

        # 找月份行号
        idx = -1
        for i, line in enumerate(lines):
            if line.strip() == ym_header:
                idx = i
                break

        if idx == -1:  # 本月不存在，新建
            # 找到第一个 ## 位置，插到它前面
            first_month_idx = -1
            for i, line in enumerate(lines):
                if re.match(r"^## \d{6}$", line.strip()):
                    first_month_idx = i
                    break
            if first_month_idx == -1:  # 一个月份都没有
                lines.extend(["", ym_header, "", new_entry])
            else:
                lines[first_month_idx:first_month_idx] = ["", ym_header, "", new_entry, ""]
            return lines

        # 本月已存在，插到该月第一个条目之前
        # 先找下一个 ## 或文件尾
        next_month_idx = len(lines)
        for j in range(idx + 1, len(lines)):
            if re.match(r"^## \d{6}$", lines[j].strip()):
                next_month_idx = j
                break
        # 在该月区域内找第一个空行后插入
        insert_pos = idx + 2
        lines[insert_pos:insert_pos] = [new_entry, ""]
        return lines

    def _format_entry(self, a: Article) -> str:
        return f"## [{a.title}]({a.url})\n\n{a.summary}\n"