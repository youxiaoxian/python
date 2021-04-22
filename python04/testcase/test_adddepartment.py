import pytest

from python04.page.main_page import MainPage


class TestAddDepartment:

    def setup_class(self):
        self.main_page = MainPage()
        # self.main_page.driver.maximize_window()
        # self.main_page.driver.implicitly_wait(3)

    def teardown_class(self):
        self.main_page.driver.quit()

    @pytest.mark.parametrize("department", ['测试'])
    def test_add_department(self, department):
        department_list = self.main_page.goto_contact().goto_add_department().add_department_success(
            department).get_department_list()
        assert '测试' in department_list

    @pytest.mark.parametrize("department", ['测试'])
    def test_add_department_fail(self, department):
        pass
        # department_list = self.main_page.goto_contact().goto_add_department().add_department_fail(department)
