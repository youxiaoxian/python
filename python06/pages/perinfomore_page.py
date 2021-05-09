from appium.webdriver.common.mobileby import MobileBy

from python06.pages.base_page import BasePage
from python06.pages.editmem_page import EditMemPage


class PerInfoMorePage(BasePage):
    __edit_mem = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def goto_edit_mem_page(self):
        # 个人信息更多页面，点击编辑成员，进入编辑成员页面
        self.find(*self.__edit_mem).click()
        return EditMemPage(self.driver)
