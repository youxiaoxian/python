import allure
import pytest

from python06.pages.app import App
from python06.utils.make_contactinfo import ContactInfo


@allure.feature("添加和删除联系人")
class TestContact:
    def setup_class(self):
        self.app = App()
        self.make_contactinfo = ContactInfo()

    def setup(self):
        # 启动app
        self.startapp = self.app.start()

    def teardown(self):
        self.app.stop()

    def teardown_class(self):
        self.app.quit()

    # @pytest.mark.skip
    # 添加联系人成功
    @allure.story("添加联系人成功")
    # @pytest.mark.parametrize('name,phonenum', [['test', '11122223333']])
    def test_add_contact_success(self):
        name = self.make_contactinfo.get_name()
        phonenum = self.make_contactinfo.get_num()
        self.startapp.goto_main_page().goto_contact_page(). \
            goto_add_mem_page().goto_add_mem_bymanual_page(). \
            add_mem_success(name, phonenum).find_toast()

    # @pytest.mark.skip
    # 添加联系人失败<手机已存在于通讯录，无法添加>
    @allure.story("添加联系人失败")
    @pytest.mark.parametrize('name,phonenum', [['test', '12200000000']])
    def test_add_contact_fail(self, name, phonenum):
        # name = self.make_contactinfo.get_name()
        # phonenum = self.make_contactinfo.get_num()
        self.startapp.goto_main_page().goto_contact_page(). \
            goto_add_mem_page().goto_add_mem_bymanual_page(). \
            add_mem_fail(name, phonenum)

    @allure.story("删除联系人成功")
    @pytest.mark.parametrize('name', ['test'])
    def test_del_contact_success(self, name):
        resultlist = self.startapp.goto_main_page().goto_contact_page(). \
            goto_per_info_page(name).goto_per_info_more_page(). \
            goto_edit_mem_page().goto_contact_page().find_del_mem(name)
        assert resultlist == []
