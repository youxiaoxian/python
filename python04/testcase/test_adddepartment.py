from python04.page.main_page import MainPage


class TestAddDepartment:

    def setup(self):
        self.main_page = MainPage()
        self.main_page.driver.maximize_window()
        self.main_page.driver.implicitly_wait(5)

    def teardown(self):
        self.main_page.driver.quit()

    def test_add_department(self):
        self.main_page.goto_contact().goto_add_department().add_department_success().get_department_list()
