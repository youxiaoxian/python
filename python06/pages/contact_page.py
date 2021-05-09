import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from python06.pages.add_mem_page import AddMemPage
from python06.pages.base_page import BasePage
from python06.pages.perinfo import PerInfoPage


class ContactPage(BasePage):

    def goto_add_mem_page(self):
        # 通讯录页面，点击添加成员，进入到添加成员页面
        self.swipe_find('添加成员').click()

        return AddMemPage(self.driver)

    def goto_per_info_page(self, name):
        # 通讯录页面，点击要删除的联系人，进入到个人信息页面

        self.swipe_find(name).click()
        return PerInfoPage(self.driver)

    def find_del_mem(self, name):
        # 通讯录页面，查找已删除的联系人
        # 如果能找到，说明删除失败，返回False；
        # 如果不能找到，说明删除成功，返回True
        # 滚动查找已删除的成员
        try:
            return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                            'new UiScrollable(new UiSelector()'
                                            '.scrollable(true).instance(0))'
                                            '.scrollIntoView(new UiSelector()'
                                            f'.text("{name}").instance(0));')
        except NoSuchElementException:
            return []
