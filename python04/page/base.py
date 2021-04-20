import yaml
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class Base:
    def __init__(self, base_driver: WebElement = None):
        """
        driver 重复实例化会 导致页面启动多次
        解决driver 重复实例化的问题
        :param base_driver:
        """
        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            with open("../conf/data.yml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                # print(yaml_data)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver
