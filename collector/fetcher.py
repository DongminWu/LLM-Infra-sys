import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from markdownify import markdownify
from utils import random_ua

class WechatArticleFetcher:
    """
    负责把微信文章 URL -> (title, markdown_body)
    后续想支持播客，只需再实现一个 PodcastFetcher 实现相同接口即可
    """
    
    def __init__(self):
        """初始化浏览器实例，避免反复打开关闭浏览器"""
        self.driver = None
        self._init_driver()

    def _init_driver(self):
        """初始化Chrome浏览器驱动"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 无头模式运行
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(f"--user-agent={random_ua()}")
        chrome_options.add_argument("--window-size=1920,1080")
        # 禁用图片加载以提高速度
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        
        # 尝试启动浏览器，如果失败则不使用特定的chromedriver路径
        try:
            self.driver = webdriver.Edge(options=chrome_options)
        except Exception as e:
            print(f"[LOG] 使用默认ChromeDriver路径失败: {e}, 尝试自动查找ChromeDriver...")
            self.driver = webdriver.Edge(options=chrome_options)

    def _ensure_driver(self):
        """确保浏览器驱动可用，如果不可用则重新初始化"""
        if self.driver is None:
            self._init_driver()
        else:
            try:
                # 尝试访问一个简单页面来检查浏览器是否仍然可用
                self.driver.current_url
            except Exception:
                # 如果浏览器不可用，重新初始化
                self._init_driver()

    def fetch(self, url: str) -> tuple[str, str]:
        print(f"[LOG] 开始抓取URL: {url}")
        self._ensure_driver()
        
        try:
            print(f"[LOG] 打开页面...")
            self.driver.get(url)
            
            # 等待页面加载完成，最多等待10秒
            print(f"[LOG] 等待页面内容加载...")
            max_wait_time = 10
            wait_interval = 0.5
            waited = 0
            
            # 等待主要内容加载完成
            while waited < max_wait_time:
                try:
                    # 尝试找到内容元素
                    content_element = self.driver.find_element(By.CLASS_NAME, "rich_media_content")
                    if content_element:
                        break
                except NoSuchElementException:
                    pass
                
                time.sleep(wait_interval)
                waited += wait_interval
            
            if waited >= max_wait_time:
                print(f"[LOG] 页面加载超时，但仍尝试提取内容...")
            
            print(f"[LOG] 页面加载完成，正在提取内容...")
            
            # 提取标题
            title = "无题"
            try:
                title_element = self.driver.find_element(By.CLASS_NAME, "rich_media_title")
                title = title_element.text.strip()
                print(f"[LOG] 提取到标题: {title}")
            except NoSuchElementException:
                print(f"[LOG] 未找到标题元素，使用默认标题")
                # 尝试其他可能的标题选择器
                try:
                    title_element = self.driver.find_element(By.ID, "activity-name")
                    title = title_element.text.strip()
                    print(f"[LOG] 提取到标题 (备用选择器): {title}")
                except NoSuchElementException:
                    print(f"[LOG] 使用备用选择器也未找到标题，使用默认标题")
            
            # 提取正文内容
            content = ""
            try:
                content_element = self.driver.find_element(By.CLASS_NAME, "rich_media_content")
                content = content_element.text.strip()
                print(f"[LOG] 成功提取文本内容")
            except NoSuchElementException:
                print(f"[LOG] 未找到内容元素，尝试其他选择器")
                # 尝试备用选择器
                try:
                    content_element = self.driver.find_element(By.ID, "js_content")
                    content = content_element.text.strip()
                    print(f"[LOG] 使用备用选择器成功提取内容")
                except NoSuchElementException:
                    print(f"[LOG] 所有内容选择器都失败，无法提取内容")
                    raise RuntimeError("无法提取文章内容，可能页面结构变化或需要登录")
            
            # 将文本内容转换为markdown格式
            # 由于Selenium获取的是纯文本，我们简单地将换行转换为markdown格式
            # 如果需要更准确的HTML到Markdown转换，我们可以获取innerHTML
            try:
                content_element = self.driver.find_element(By.CLASS_NAME, "rich_media_content")
                inner_html = content_element.get_attribute("innerHTML")
                md = markdownify(inner_html, heading_style="ATX")
                print(f"[LOG] HTML到Markdown转换完成")
            except Exception as e:
                print(f"[LOG] HTML转换失败，使用文本内容: {e}")
                # 如果HTML转换失败，使用纯文本并简单格式化
                md = content.replace('\n', '\n\n')  # 将换行符转换为markdown段落分隔

            print(f"[LOG] 文章抓取完成")
            return title, md
            
        except TimeoutException:
            print(f"[LOG] 页面加载超时: {url}")
            raise RuntimeError(f"页面加载超时: {url}")
        except Exception as e:
            print(f"[LOG] 抓取失败: {e}")
            raise RuntimeError(f"抓取失败: {e}")

    def __del__(self):
        """析构函数，确保浏览器关闭"""
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass