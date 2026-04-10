import time
from playwright.sync_api import Page
from login_page import LoginPage
from signup_page import SignupPage
from memos_page import MemosPage


def test_signup_login_create_memo(page: Page) -> None:
    username = f"user_{int(time.time())}"
    password = "Password123!"

    signup_page = SignupPage(page)
    signup_page.signup(username, password)

    login_page = LoginPage(page)
    login_page.login(username, password)

    memos_page = MemosPage(page)
    memo_text = "注册后创建的备忘录"
    memos_page.create_memo(memo_text)
    assert memos_page.memo_exists(memo_text)
