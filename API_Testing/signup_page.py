from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_role("textbox", name="用户名")
        self.password = page.get_by_role("textbox", name="密码")
        self.signup_button = page.get_by_role("button", name="注册")

    def open(self) -> None:
        self.page.goto("http://localhost:8081/auth/signup")

    def signup(self, username: str, password: str) -> None:
        self.open()
        self.username.wait_for(state="visible", timeout=5000)
        self.username.fill(username)
        self.password.fill(password)
        self.signup_button.click()
