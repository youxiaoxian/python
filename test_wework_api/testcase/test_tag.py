import allure
import pytest
from jsonpath import jsonpath
from test_wework_api.api.externalcontact.tag import Tag


@allure.feature("管理企业标签")
class TestTag:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()
        # 清除所有tag
        self.tag.clear()

    def teardown_class(self):
        # 如果进程被临时终止，teardown*方法可能得不到执行，所以为了稳定，尽量不要在teardown*中放入重要的逻辑。
        pass

    @pytest.mark.run(order=1)
    @allure.story("获取企业标签库")
    @allure.title("成功获取企业标签库")
    def test_get_tag(self):
        r = self.tag.get_tag()
        assert r.json()['errcode'] == 0
        assert len(r.json()['tag_group']) == 0

    @pytest.mark.run(order=2)
    @allure.story("添加企业客户标签")
    @allure.title("成功添加企业客户标签")
    @pytest.mark.parametrize('group_name,tag_list',
                             [["test0521001_group1", [{"name": "test111"}, {"name": "test112"}]]])
    def test_add_tag(self, group_name, tag_list):
        with allure.step("第一步：调用增加标签方法"):
            r = self.tag.add_tag(group_name, tag_list)
        with allure.step("第二步：断言添加标签方法errcode为0"):
            assert r.json()['errcode'] == 0
        with allure.step("第三步：获取所有标签"):
            r = self.tag.get_tag()
        with allure.step("第四步：断言获取标签方法errcode为0"):
            assert r.json()['errcode'] == 0
        with allure.step("第五步：断言新增的标签组是否在获取标签的响应结果中"):
            assert 'test0521001_group1' in [group['group_name'] for group in r.json()['tag_group']]
        tag_name_list = ["test111", "test112"]
        # 判断集合相等
        with allure.step("第六步：断言新增的tag列表是否在获取标签的响应结果中"):
            assert set(tag_name_list) == set(jsonpath(r.json(), '$..tag[*].name'))
        # 判断set(tag_list)是set(jsonpath(r.json(), '$..tag[*].name'))的子集
        with allure.step("同第六步：断言新增的tag列表是否在获取标签的响应结果中"):
            assert set(tag_name_list).issubset(set(jsonpath(r.json(), '$..tag[*].name')))

    @pytest.mark.run(order=3)
    @allure.story("编辑企业客户标签")
    @allure.title("成功编辑企业客户标签")
    @pytest.mark.parametrize('tag_name_old,tag_name_new', [["test111", "test"]])
    def test_edit_tag(self, tag_name_old, tag_name_new):
        tag_id = self.tag.get_tag_id(tag_name_old)
        r = self.tag.edit_tag(tag_id, tag_name_new)
        assert r.json()['errcode'] == 0

        r = self.tag.get_tag()
        assert tag_name_new in jsonpath(r.json(), '$..name')

    # @pytest.mark.run(order=4)
    # @pytest.mark.parametrize('tag_name_list', [["test","test112"]])
    # def test_delete_tag(self, tag_name_list):
    #     tag_id_list = self.tag.get_tag_id_list(tag_name_list)
    #     # print(tag_id_list)
    #     r = self.tag.delete_tag(tag_id_list)
    #     # print(r)
    #     assert r.json()['errcode'] == 0
    #     r = self.tag.get_tag()
    #     for tag_id in tag_id_list:
    #         # print(tag_id)
    #         # 判断删除的内容是否已经消失在search结果里
    #         # $..*所有元素
    #         assert tag_id not in jsonpath(r.json(),'$..*')

    @pytest.mark.run(order=4)
    @allure.story("删除企业标签库")
    @allure.title("成功删除企业标签库")
    @pytest.mark.parametrize('tag_name_list', [["test", "test112"]])
    def test_delete_tag(self, tag_name_list):
        tag_id_list = self.tag.get_tag_id_list_2(tag_name_list)
        r = self.tag.delete_tag(tag_id_list)
        assert r.json()['errcode'] == 0
        r = self.tag.get_tag()
        for tag_id in tag_id_list:
            # 判断删除的内容是否已经消失在search结果里
            # $..*所有元素
            assert tag_id not in jsonpath(r.json(), '$..*')

    @allure.story("全流程测试")
    @allure.title("成功全流程测试")
    def test_smoke_flow(self):
        # 冒烟测试
        # 线上巡检测试
        # 重要的测试数据
        # 全流程测试用例 添加 修改 删除 查询
        pass
