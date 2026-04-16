from playwright.sync_api import Page
from ..pages.memos_page import MemosPage
from ..pages.login_page import LoginPage  


def test_add_reaction(page:Page) -> None:
    
    loginPage=LoginPage(page)
    loginPage.login("dyy2026", "dongyuanyuan2000.")

    memos_page = MemosPage(page)
   
    memos_page.add_reaction()

    
