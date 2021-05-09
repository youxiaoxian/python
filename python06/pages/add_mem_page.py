from appium.webdriver.common.mobileby import MobileBy

from python06.pages.base_page import BasePage


class AddMemPage(BasePage):
    __add_by_manual = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    __add_success = (MobileBy.XPATH, "//*[contains(@text,'添加成功')]")

    def goto_add_mem_bymanual_page(self):
        # 添加成员页面，点击手动输入添加，进入到编辑成员页面
        from python06.pages.add_mem_bymanual_page import AddMemByManualPage
        self.find(*self.__add_by_manual).click()

        return AddMemByManualPage(self.driver)

    def find_toast(self):
        # 判断添加成功
        self.find(*self.__add_success)
