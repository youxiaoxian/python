import time

from selenium.webdriver.common.by import By

from python04.page.base import Base


class AddDepartment(Base):
    # 输入部门名称
    __ele_departement = (By.NAME, 'name')
    # 点击所属部门
    __ele_click_select_depa = (By.CSS_SELECTOR, '.js_parent_party_name')
    # 选择所属部门
    __ele_select_depa = (By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688850737158532_anchor']")
    # 点击确定
    __ele_confirm = (By.LINK_TEXT, "确定")

    def add_department_success(self, department):
        '''
        添加部门信息并保存成功
        :return:
        '''
        from python04.page.contact import Contact
        # self.driver.find_element(By.CSS_SELECTOR,'[name=name]').send_keys('测试')
        self.find(self.__ele_departement).send_keys(department)
        self.find(self.__ele_click_select_depa).click()
        self.find(self.__ele_select_depa).click()
        self.find(self.__ele_confirm).click()
        return Contact(self.driver)

    def add_department_fail(self, department):
        '''
        添加部门信息失败
        :return:
        '''
        pass
