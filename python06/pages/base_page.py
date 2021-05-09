from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging

# pytest对logging进行了改写，此处设置无效
logging.basicConfig(level=logging.info)


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, value):
        logging.info(by)
        logging.info(value)
        # 查找元素
        ele = self.driver.find_element(by, value)
        return ele

    def swipe_find(self, text, num=2):
        # num,默认查找次数
        self.driver.implicitly_wait(1)

        for i in range(0, num):
            try:
                ele = self.find(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return ele

            except NoSuchElementException:
                print('未找到,滑动')

            # 滑动一页，继续查找
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height']
            start_x = width / 2
            start_y = height * 0.8

            end_x = start_x
            end_y = height * 0.3
            duration = 2000  # ms
            # 完成滑动操作
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)

        if i == num - 1:
            self.driver.implicitly_wait(5)
            raise NoSuchElementException(f'找了{i + 1}次，未找到')
