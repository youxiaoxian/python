import time

from selenium.webdriver.common.by import By

from python04.page.add_department import AddDepartment
from python04.page.base import Base


class Contact(Base):
    def goto_add_department(self):
        '''
        跳转到添加部门弹窗
        :return:
        '''
        # self.driver.find_element(By.CSS_SELECTOR,'.member_colLeft_top_addBtn').click()
        self.driver.find_element(By.XPATH, '//*[@class="member_colLeft_top_addBtn"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_create_party').click()
        time.sleep(5)
        return AddDepartment(self.driver)

    def get_department_list(self):
        '''
        获取部门列表
        :return:
        '''
        time.sleep(3)
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, '.jstree-anchor')
        print(ele_list)
        department_list = []
        # 遍历元素列表，通过元素的text 属性，提取文本数据信息
        for ele in ele_list:
            department_list.append(ele.text)
        print(department_list)
        return department_list
