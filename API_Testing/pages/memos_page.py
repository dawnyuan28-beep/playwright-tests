"""
备忘录页面模块 - 页面对象模型(Page Object Model)
该模块封装了备忘录页面的所有交互操作，包括创建、编辑、置顶、取消置顶等功能
通过页面对象模型，使测试代码更清晰、更易维护
"""

from playwright.sync_api import Page  # 导入 Playwright 的页面对象，用于浏览器自动化
from playwright.sync_api import expect
  

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
        self.memo_input = page.get_by_role("textbox", name="此刻的想法...")
        # 查找"保存"按钮，点击这个按钮会保存输入的备忘录内容
        self.save_button = page.get_by_role("button", name="保存")

        """
        定位备忘录列表中的第一个memo的备忘录项，使用 CSS 选择器定位
        loator 是更通用的元素定位方式，可以使用 CSS 选择器来查找元素
        操作栏有置顶、编辑、删除等功能
        """
        #定位第一个memo的操作栏
        self.more_button = page.locator(".lucide-ellipsis-vertical").first
        #定位置顶按钮
        self.pin_option=page.get_by_role("menuitem", name="置顶")
        #定位编辑按钮
        self.edit_option=page.get_by_role("menuitem", name="编辑")
        #定位删除按钮
        self.delete_option=page.get_by_role("menuitem", name="删除")
       
        #定位取消置顶
        self.unpin_button=self.page.locator(".lucide.lucide-bookmark").first
        

        #每个memo的编辑后保存按钮
        self.edit_save_button=page.get_by_role("button", name="保存").nth(1)
        #鼠标悬停在备忘录上显示的发布时间
        self.published_at = self.page.locator("relative-time").first
        #定位表情按钮
        self.smile_button=page.locator(".lucide.lucide-smile-plus").first
        #表情选择框
        self.dialog = page.get_by_role("dialog")
        #点赞按钮
        self.delete_button=page.get_by_role("button", name="👍", exact=True)
        
        
        #删除的二次确定弹窗
        self.confirm_delete_dialog= page.get_by_role("dialog", name="您确定要删除此条备忘录吗？")
        #删除弹窗的取消按钮
        self.cancel_delete_button=page.get_by_role("button", name="取消")
        #删除弹窗的确认删除按钮
        self.confirm_delete_button=page.get_by_role("button", name="删除")


    def open(self) -> None:
        """
    
        打开备忘录页面
        
        该方法访问备忘录页面的 URL
        在大多数测试中，用户登录后会自动进入这个页面。
        
        返回值：None（无返回值）
        """
        # 导航到备忘录页面的 URL
        self.page.goto("http://localhost:8081")

    def create_memo(self, memo_content: str) -> None:
        """
        创建一条新的备忘录
        """
        # 第一步：在输入框中填入备忘录内容
        
        self.memo_input.wait_for(state="visible", timeout=10000)  
        self.memo_input.fill(memo_content)
        # 第二步：点击保存按钮，保存备忘录
        self.save_button.click()
     
        
    def pin_and_unpin_memo(self) -> None:
        #置顶和取消置顶备忘录
        
        # 点击第一条备忘录的更多操作按钮，打开操作菜单
        self.more_button.click()
        # 在操作菜单中选择"置顶"选项，将备忘录置顶
        self.pin_option.wait_for(state="visible", timeout=2000)
        self.pin_option.click()
        # 验证备忘录已被置顶，可以通过检查页面上是否存在表示置顶状态的元素来实现
        expect(self.unpin_button).to_be_visible()
        
        self.page.wait_for_timeout(10000)  # 等待一段时间，确保页面状态更新
        
        self.unpin_button.click()
      
        self.page.wait_for_timeout(10000)  # 等待一段时间，确保页面状态更新
    
    #在弹出的 reaction 面板里，找到某个“表情按钮”
    def reaction_btn(self, reaction):
        btn = self.page.get_by_role("dialog").get_by_text(reaction)
        btn.wait_for(state="visible", timeout=2000)
        return btn
    
    # 给备忘录添加表情反应
    def add_reaction(self) -> None:
        # 鼠标悬停在文本框，等待微笑元素可见
        self.published_at.hover() 
       # 点击第一条备忘录的微信按钮，打开表情选择菜单
        self.smile_button.wait_for(state="visible", timeout=10000)  # 等待表情按钮可见
        self.smile_button.click()
        # 在表情选择菜单中选择一个表情（例如 "👍"），点击该表情按钮，添加反应
        reaction_btn = self.reaction_btn("👍")
        reaction_btn.click()

   

    #编辑memo
    def edit_memo(self, new_content: str) -> None:
        self.more_button.click()
        self.edit_option.wait_for(state="visible", timeout=2000)
        self.edit_option.click()
        self.memo_input.fill(new_content)
        self.edit_save_button.click() 


    def delete_memo(self) -> None:
        self.more_button.click()
        self.delete_option.wait_for(state="visible", timeout=2000)
        self.delete_option.click()
        self.confirm_delete_dialog.wait_for(state="visible", timeout=2000)
        self.confirm_delete_button.click()