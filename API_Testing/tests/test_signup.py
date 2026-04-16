from playwright.sync_api import Page
from ..pages.signup_page import SignupPage
import time


def test_signup(page: Page) -> None:
    """
    注册功能的测试函数 
    这是一个 pytest 测试用例，用于验证注册功能是否正常工作。
    pytest 会自动发现并运行以 'test_' 开头的函数。
    
    参数：
        page (Page): pytest-playwright 插件自动提供的浏览器页面对象
    """
    # 创建 SignupPage 对象，代表网页上的注册页面
    signup_page = SignupPage(page)
    
    # 调用 signup 方法，执行完整的注册流程
    username = f"user{int(time.time())}"
    password = "123456"
    signup_page.signup(username, password)
    print("当前URL：", page.url)
    print(username, password)
    # 关键：验证是否跳转成功
    assert "/auth" not in page.url