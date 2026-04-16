"""
备忘录功能测试模块 - 测试备忘录的创建、置顶和取消置顶功能
该模块包含对备忘录各项功能的自动化测试用例
"""

from playwright.sync_api import Page  # 导入 Playwright 的页面对象，用于浏览器自动化
from ..pages.login_page import LoginPage  # 导入登录页面类
from ..pages.memos_page import MemosPage  # 导入备忘录页面类

def test_create_memo(page: Page) -> None:
    """
    测试用例：创建备忘录并置顶
    
    该测试验证以下流程：
    1. 以指定账户登录
    2. 创建一条新的备忘录
    
    参数：
        page (Page): pytest-playwright 插件自动提供的浏览器页面对象
    """
    # 第一步：创建登录页面对象
    login_page = LoginPage(page)
    # 执行登录操作，使用测试账户凭证
    
    login_page.login("dyy2026", "dongyuanyuan2000.")
    # 第二步：创建备忘录页面对象
    memos_page = MemosPage(page)
    print(f"当前页面标题是: {page.title()}")
    
    # 第三步：创建一条新的备忘录，内容为 "这是一个测试备忘录"
    memos_page.create_memo("测试0416")

    memos_page.pin_and_unpin_memo()
  


