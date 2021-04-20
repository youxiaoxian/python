import time

from selenium.webdriver.common.by import By

from python04.page.base import Base
from python04.page.contact import Contact


class MainPage(Base):
    def goto_contact(self):
        '''
        跳转到通讯录页面
        :return:
        '''
        self.driver.find_element(By.LINK_TEXT, '通讯录').click()
        return Contact(self.driver)
