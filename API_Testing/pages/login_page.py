from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_role("textbox", name="用户名")
        self.password = page.get_by_role("textbox", name="密码")
        self.login_button = page.get_by_role("button", name="登录")

    def open(self) -> None:
        self.page.goto("http://localhost:8081/auth")

    def login(self, username: str, password: str) -> None:
        self.open()
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
