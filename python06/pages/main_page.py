from appium.webdriver.common.mobileby import MobileBy

from python06.pages.base_page import BasePage
from python06.pages.contact_page import ContactPage


class MainPage(BasePage):
    __contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact_page(self):
        # 首页，点击通讯录，进入到通讯录页面
        self.find(*self.__contact_element).click()
        return ContactPage(self.driver)
