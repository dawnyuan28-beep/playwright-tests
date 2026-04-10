from playwright.sync_api import Page
from login_page import LoginPage
from memos_page import MemosPage


def test_create_and_pin_memo(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.login("dyy2026", "dongyuanyuan2000.")

    memos_page = MemosPage(page)
    memos_page.create_memo("这是一个测试备忘录")
    memos_page.pin_memo("这是一个测试备忘录")
    assert memos_page.memo_exists("这是一个测试备忘录")


def test_pin_and_unpin_memo(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.login("dyy2026", "dongyuanyuan2000.")

    memos_page = MemosPage(page)
    memos_page.create_memo("需要取消置顶的备忘录")
    memos_page.pin_memo("需要取消置顶的备忘录")
    memos_page.unpin_memo("需要取消置顶的备忘录")
    assert memos_page.memo_exists("需要取消置顶的备忘录")
