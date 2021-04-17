import time

import pytest
import yaml
from selenium.webdriver.support.wait import WebDriverWait

from python03.get_cookie import getcookie
from python03.initclass import TestInit


class TestAddmember(TestInit):
    def test_cookie(self):
        # 访问扫码登录页面
        getcookie()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("./conf/data.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            print(yaml_data)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # time.sleep(5)
        # self.driver.find_element_by_link_text('添加成员').click()
        while True:
            self.driver.find_element_by_link_text('添加成员').click()
            if self.driver.find_elements_by_link_text('保存'):
                break
        self.driver.find_element_by_id("username").send_keys('张三')
        self.driver.find_element_by_id("memberAdd_acctid").send_keys('zhangsan')
        self.driver.find_element_by_id("memberAdd_phone").send_keys('12345678911')
        # 定位保存元素-1 ，full xpath
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
        # 定位保存元素-2，full xpath
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        # 定位保存元素，linktext
        # self.driver.find_element_by_link_text('保存').click()
        # self.driver.find_elements_by_link_text('添加成员')[1].click()
        # 定位保存元素，通过class属性，先找到所有元素，再点击其中1个
        self.driver.find_elements_by_class_name('js_btn_save')[0].click()
        time.sleep(5)

    # 过程测试使用，请忽略
    @pytest.mark.skip
    def test_ele(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("./conf/data.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            print(yaml_data)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 等待条件无效，因为这个点击的相应事件是绑定的js事件 js事件没加载完的时候 点了也没有效果
        # def wait(x):
        #     return len(self.driver.find_elements_by_link_text('添加成员')) >= 1

        while True:
            self.driver.find_element_by_link_text('添加成员').click()
            if self.driver.find_elements_by_link_text('保存'):
                break
        time.sleep(5)

        # time.sleep(5)
        # self.driver.find_element_by_link_text('添加成员').click()
        # self.driver.find_elements_by_link_text('添加成员')[1].click()
        # time.sleep(5)
        # eles = self.driver.find_elements_by_link_text('保存')
        # print(len(eles))
        # for ele in eles:
        #     print(ele)
