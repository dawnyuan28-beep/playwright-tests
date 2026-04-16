from playwright.sync_api import Page
from ..pages.login_page import LoginPage

def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.login("dyy2026", "dongyuanyuan2000.")

    

