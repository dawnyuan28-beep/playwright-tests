
from playwright.sync_api import Page
from..pages.memos_page import MemosPage
from..pages.login_page import LoginPage

def test_edit_memo(page:Page) -> None:  
    Login_Page=LoginPage(page)
    Login_Page.login("dyy2026", "dongyuanyuan2000.")
    Memos_Page=MemosPage(page)
    Memos_Page.edit_memo("这是一个编辑后的测试备忘录")