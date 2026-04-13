"""
测试流程模块 - API 自动化测试
该模块用于测试完整的用户流程：注册 -> 登录 -> 创建备忘录
"""
import time
from playwright.sync_api import Page
from API_Testing.pages.login_page import LoginPage
from API_Testing.pages.signup_page import SignupPage
from API_Testing.pages.memos_page import MemosPage


def test_signup_login_create_memo(page: Page) -> None:
    """
    测试用户完整流程：注册、登录、创建备忘录
    
    该测试函数执行以下步骤：
    1. 使用唯一用户名进行注册
    2. 使用注册的凭证进行登录
    3. 创建一条备忘录
    4. 验证备忘录是否成功创建
    
    参数：
        page (Page): Playwright 浏览器页面对象
    """
    # 使用当前时间戳生成唯一的用户名，避免重复注册
    #f-string “格式化字符串”可以在 { } 里写变量/表达式的字符串
    username = f"user_{int(time.time())}"
    # 设置测试密码
    password = "Password123!"

    # 第一步：执行注册流程
    signup_page = SignupPage(page)
    signup_page.signup(username, password)

    # 第二步：执行登录流程
    login_page = LoginPage(page)
    login_page.login(username, password)

    # 第三步：创建备忘录并验证
    memos_page = MemosPage(page)
    memo_text = "注册后创建的备忘录"
    memos_page.create_memo(memo_text)
    # 断言：验证备忘录是否存在
    assert memos_page.memo_exists(memo_text)
