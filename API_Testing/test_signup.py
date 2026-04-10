from playwright.sync_api import Page
from signup_page import SignupPage


def test_signup(page: Page) -> None:
    signup_page = SignupPage(page)
    signup_page.signup("dyy2026", "dongyuanyuan2000")
