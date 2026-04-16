from playwright.sync_api import Page
from..pages.login_page import LoginPage
from..pages.memos_page import MemosPage

def test_delete_memo(page:Page) -> None:
    Login_Page=LoginPage(page)
    Login_Page.login("dyy2026", "dongyuanyuan2000.")
    Memos_Page=MemosPage(page)
    Memos_Page.delete_memo()