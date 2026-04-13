"""
备忘录页面模块 - 页面对象模型(Page Object Model)
该模块封装了备忘录页面的所有交互操作，包括创建、编辑、置顶、取消置顶等功能
通过页面对象模型，使测试代码更清晰、更易维护
"""

from playwright.sync_api import Page  # 导入 Playwright 的页面对象，用于浏览器自动化


class MemosPage:
    """
    备忘录页面类 - 封装备忘录页面的所有操作
    
    这个类代表应用程序的备忘录页面，提供了以下功能：
    - 创建备忘录
    - 编辑备忘录
    - 置顶/取消置顶备忘录
    - 查询备忘录是否存在
    
    所有操作都通过页面对象模型进行，提高了代码的复用性和可维护性。
    """
    
    def __init__(self, page: Page):
        """
        初始化备忘录页面对象
        
        在这个方法中，我们查找并保存页面上的重要元素，以便后续使用。
        这个方法在创建 MemosPage 对象时自动调用。
        
        参数：
            page (Page): Playwright 的页面对象，代表浏览器中的网页
        """
        # 保存页面对象，供后续操作使用
        self.page = page
        # 查找备忘录输入框,get_by_role 是 Playwright 推荐的元素定位方式，基于元素的角色和名称进行查找
        self.memo_input = page.get_by_role("textbox", name="Any thoughts...")
        # 查找"保存"按钮，点击这个按钮会保存输入的备忘录内容
        self.save_button = page.get_by_role("button", name="Save")
        #定位第一个memo的操作栏，loator 是更通用的元素定位方式，可以使用 CSS 选择器等多种方式进行查找
        self.more_button = page.locator(".lucide-ellipsis-vertical").first
        #定位置顶按钮
        self.pin_option=page.get_by_role("menuitem", name="pin").click()
        #定位编辑按钮
        self.edit_option=page.get_by_role("menuitem", name="Edit")
        #定位删除按钮
        self.page.get_by_role("menuitem", name="Delete")
        #定位取消置顶
        self.unpin_button=self.page.locator(".lucide.lucide-bookmark > path")
        #鼠标悬停在备忘录上显示的发布时间
        self.published_at = self.page.locator("relative-time")
        #定位表情按钮
        self.smile_button=page.locator(".lucide.lucide-smile-plus").first
        #点赞按钮
        self.delete_button=page.get_by_role("button", name="👍", exact=True)
        #定位删除按钮
        self.delete_option=self.page.get_by_role("menuitem", name="删除").click()
        

    def open(self) -> None:
        """
        打开备忘录页面
        
        该方法访问备忘录页面的 URL
        在大多数测试中，用户登录后会自动进入这个页面。
        
        返回值：None（无返回值）
        """
        # 导航到备忘录页面的 URL
        self.page.goto("http://localhost:8081/auth")

    def create_memo(self, memo_content: str) -> None:
        """
        创建一条新的备忘录
        
        参数：
            memo_content (str): 备忘录的内容（要输入的文本）
        
        返回值：None（无返回值）
        """
        # 第一步：在输入框中填入备忘录内容
        self.memo_input.fill(memo_content)
        
        # 第二步：点击保存按钮，保存备忘录
        self.save_button.click()

    def get_memo_card(self, memo_content: str):
        """
        获取备忘录卡片元素
        
        这个方法根据备忘录内容找到对应的备忘录卡片 HTML 元素。
        备忘录卡片是显示在页面上的备忘录矩形框。
        
        参数：
            memo_content (str): 要查找的备忘录内容
        
        返回值：
            定位器对象，指向找到的备忘录卡片元素
        
        实现原理：
        1. 首先查找所有 <article> 元素（备忘录卡片是 article 标签）
        2. 然后过滤出包含该备忘录内容的卡片
        3. 具体通过查找 data-memo-content="true" 的元素，再看其中的文本是否匹配
        """
        # 使用 locator 方法查找所有 <article> 元素
        # filter 方法用来筛选条件：has 参数表示查找包含特定子元素的卡片
        # 条件是：包含了具有指定文本内容的元素
        return self.page.locator("article").filter(
            has=self.page.locator('[data-memo-content="true"]').get_by_text(memo_content)
        )

    def open_memo_menu(self, memo_content: str) -> None:
        """
        打开备忘录的操作菜单
        
        找到指定的备忘录卡片，然后点击其菜单按钮（通常是三个点的图标）。
        这会弹出一个菜单，包含编辑、删除、置顶等操作选项。
        
        参数：
            memo_content (str): 目标备忘录的内容
        
        返回值：None（无返回值）
        """
        # 第一步：获取备忘录卡片元素
        memo_card = self.get_memo_card(memo_content)
        
        # 第二步：在卡片中查找有 aria-haspopup="menu" 属性的按钮（菜单按钮）
        # aria-haspopup="menu" 是无障碍标准中表示"这个按钮会打开一个菜单"的属性
        # 第三步：点击这个菜单按钮
        memo_card.locator('button[aria-haspopup="menu"]').click()

    def pin_memo(self, memo_content: str) -> None:
        """
        置顶一条备忘录
        
        置顶后，该备忘录会显示在备忘录列表的顶部。
        
        参数：
            memo_content (str): 要置顶的备忘录的内容
        
        返回值：None（无返回值）
        """
        # 第一步：打开备忘录的菜单
        self.open_memo_menu(memo_content)
        
        # 第二步：在菜单中点击 "Pin" 选项
        self.page.get_by_role("menuitem", name="Pin").click()

    def unpin_memo(self, memo_content: str) -> None:
        """
        取消置顶一条备忘录
        
        取消置顶后，该备忘录会回到普通列表位置。
        
        参数：
            memo_content (str): 要取消置顶的备忘录的内容
        
        返回值：None（无返回值）
        """
        # 第一步：打开备忘录的菜单
        self.open_memo_menu(memo_content)
        
        # 第二步：在菜单中点击 "Unpin" 选项
        self.page.get_by_role("menuitem", name="Unpin").click()

    def edit_memo(self, memo_content: str, new_content: str) -> None:
        """
        编辑一条备忘录
        
        用新的内容替换原有的内容。
        
        参数：
            memo_content (str): 原始备忘录的内容（用来定位备忘录）
            new_content (str): 新的备忘录内容
        
        返回值：None（无返回值）
        """
        # 第一步：打开备忘录的菜单
        self.open_memo_menu(memo_content)
        
        # 第二步：在菜单中点击 "Edit" 选项
        self.page.get_by_role("menuitem", name="Edit").click()
        
        # 第三步：清除原有内容并输入新的内容
        self.memo_input.fill(new_content)
        
        # 第四步：点击保存按钮，保存编辑结果
        self.save_button.click()

    def memo_exists(self, memo_content: str) -> bool:
        """
        检查备忘录是否存在
        
        该方法返回一个布尔值（True 或 False），用于验证备忘录是否存在。
        
        参数：
            memo_content (str): 要查找的备忘录内容
        
        返回值：
            bool: 
                True - 备忘录存在
                False - 备忘录不存在
        """
        # 获取备忘录卡片元素，然后检查是否找到了任何元素
        # count() 方法返回找到的元素个数
        # 如果 count() > 0，说明找到了至少一个备忘录卡片，返回 True
        # 否则返回 False
        return self.get_memo_card(memo_content).count() > 0
