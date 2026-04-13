"""
注册页面模块 - 用于自动化测试注册功能
该模块是一个页面对象模型(Page Object Model)的实现，封装了注册页面的所有交互操作
"""
# 导入 Playwright 的页面对象，用于浏览器自动化
from playwright.sync_api import Page  


class SignupPage:
    """
    注册页面类 - 封装注册页面的所有操作
    
    这个类代表应用程序的注册页面，包含所有与注册相关的元素和操作。
    使用页面对象模型的设计模式，让测试代码更清晰、更易维护。
    """
    
    def __init__(self, page: Page):
        """
        初始化注册页面对象
        参数：
            page (Page): Playwright 的页面对象，代表浏览器中的网页
        """
        # 保存页面对象，供后续操作使用
        self.page = page
        
        # 通过角色 "textbox" 和名称查找用户名输入框
        # get_by_role 是一种推荐的元素定位方式，更稳定可靠
        self.username = page.get_by_role("textbox", name="用户名")
        
        # 通过角色 "textbox" 和名称查找密码输入框
        self.password = page.get_by_role("textbox", name="密码")
        
        # 通过角色 "button" 和名称查找注册按钮
        self.signup_button = page.get_by_role("button", name="注册")

    def open(self) -> None:
        """
        打开注册页面
        该方法访问注册页面的 URL。
        返回值：None（无返回值）
        """
        # 导航到注册页面的 URL
        self.page.goto("http://localhost:8081/auth/signup")

    def signup(self, username: str, password: str) -> None:
        """
        执行注册操作 - 输入用户名、密码并点击注册按钮 
        参数：
            username (str): 要注册的用户名
            password (str): 要注册的密码
            
        """
        # 第一步：打开注册页面
        self.open()
        
        # 第二步：等待用户名输入框出现（最多等待 5000 毫秒 = 5 秒）
        # 这个等待确保页面已完全加载，避免元素未找到的错误
        self.username.wait_for(state="visible", timeout=5000)
 
        # 第三步：在用户名输入框中输入用户名
        self.username.fill(username)
        
        # 第四步：在密码输入框中输入密码
        self.password.fill(password)
        print("username输入框值：", self.username.input_value())
        print("password输入框值：", self.password.input_value())
        # 第五步：点击注册按钮，提交注册表单
        self.signup_button.click()

        # 等待页面变化（关键）
        self.page.wait_for_load_state("networkidle")
        print("点击后URL：", self.page.url)

