from appium.webdriver.common.mobileby import MobileBy

from python06.pages.base_page import BasePage


class AddMemByManualPage(BasePage):
    __pername = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']")
    __phone = (MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']")
    __save = (MobileBy.XPATH, "//*[@text='保存']")
    __alert_fail = (MobileBy.XPATH, "//*[contains(@text,'手机已存在')]")

    def add_mem_success(self, name, phonenum):
        # 编辑成员页面，输入姓名和手机号，点击保存，进入到添加成员页面
        from python06.pages.add_mem_page import AddMemPage
        self.find(*self.__pername).send_keys(name)
        self.find(*self.__phone).send_keys(phonenum)
        self.find(*self.__save).click()

        return AddMemPage(self.driver)

    def add_mem_fail(self, name, phonenum):
        # 编辑成员页面，输入姓名和手机号，点击保存，进入到添加成员页面
        from python06.pages.add_mem_page import AddMemPage
        self.find(*self.__pername).send_keys(name)
        self.find(*self.__phone).send_keys(phonenum)
        self.find(*self.__save).click()
        # 保存失败<手机已存在于通讯录，无法添加>
        self.find(*self.__alert_fail).click()
