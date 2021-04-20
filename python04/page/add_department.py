import time

from selenium.webdriver.common.by import By

from python04.page.base import Base


class AddDepartment(Base):
    def add_department_success(self):
        '''
        添加部门信息并保存成功
        :return:
        '''
        from python04.page.contact import Contact
        # self.driver.find_element(By.CSS_SELECTOR,'[name=name]').send_keys('测试111')
        self.driver.find_element(By.NAME, 'name').send_keys('测试111')
        self.driver.find_element(By.CSS_SELECTOR, '.js_parent_party_name').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".qui_dialog_body.ww_dialog_body [id='1688850763146667_anchor']").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        # time.sleep(5)
        return Contact(self.driver)

    def add_department_fail(self):
        '''
        添加部门信息失败
        :return:
        '''
        pass
