from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_role("textbox", name="username")
        self.password = page.get_by_role("textbox", name="password")
        self.login_button = page.get_by_role("button", name="Sign in")

    def open(self) -> None:
        self.page.goto("http://localhost:8081/auth")

    def login(self, username: str, password: str) -> None:
        self.open()
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
