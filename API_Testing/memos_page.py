from playwright.sync_api import Page

class MemosPage:
    def __init__(self, page: Page):
        self.page = page
        self.memo_input = page.get_by_role("textbox", name="Any thoughts...")
        self.save_button = page.get_by_role("button", name="Save")

    def open(self) -> None:
        self.page.goto("http://localhost:8081/auth")

    def create_memo(self, memo_content: str) -> None:
        self.memo_input.fill(memo_content)
        self.save_button.click()

    def get_memo_card(self, memo_content: str):
        return self.page.locator("article").filter(
            has=self.page.locator('[data-memo-content="true"]').get_by_text(memo_content)
        )

    def open_memo_menu(self, memo_content: str) -> None:
        memo_card = self.get_memo_card(memo_content)
        memo_card.locator('button[aria-haspopup="menu"]').click()

    def pin_memo(self, memo_content: str) -> None:
        self.open_memo_menu(memo_content)
        self.page.get_by_role("menuitem", name="Pin").click()

    def unpin_memo(self, memo_content: str) -> None:
        self.open_memo_menu(memo_content)
        self.page.get_by_role("menuitem", name="Unpin").click()

    def edit_memo(self, memo_content: str, new_content: str) -> None:
        self.open_memo_menu(memo_content)
        self.page.get_by_role("menuitem", name="Edit").click()
        self.memo_input.fill(new_content)
        self.save_button.click()

    def memo_exists(self, memo_content: str) -> bool:
        return self.get_memo_card(memo_content).count() > 0


#测试是否合并分支git branchgit log --oneline 1016
print("test branch change")