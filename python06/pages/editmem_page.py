from appium.webdriver.common.mobileby import MobileBy

from python06.pages.base_page import BasePage


class EditMemPage(BasePage):
    __confirm = (MobileBy.XPATH, "//*[@text='确定']")

    def goto_contact_page(self):
        from python06.pages.contact_page import ContactPage
        # 编辑成员页面，点击删除成员，再点击确定，进入通讯录页面
        self.swipe_find('删除成员').click()
        self.find(*self.__confirm).click()
        return ContactPage(self.driver)
