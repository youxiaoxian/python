import pytest
from jsonpath import jsonpath
from python09_api.wework_api import Wework


class TestWework:
    def setup_class(self):
        self.wework = Wework()

    def test_get_tag(self):
        r = self.wework.get_tag()
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize('group_name,tag_name', [["test0521001_group1", "test111"]])
    def test_add_tag(self, group_name, tag_name):
        r = self.wework.add_tag(group_name, tag_name)
        assert r.json()['errcode'] == 0
        r = self.wework.get_tag()
        assert tag_name in jsonpath(r.json(), '$..name')

    @pytest.mark.parametrize('tag_name_old,tag_name_new', [["test111", "test"]])
    def test_edit_tag(self, tag_name_old, tag_name_new):
        tag_id = self.wework.get_tag_id(tag_name_old)
        r = self.wework.edit_tag(tag_id, tag_name_new)
        assert r.json()['errcode'] == 0
        r = self.wework.get_tag()
        assert tag_name_new in jsonpath(r.json(), '$..name')

    @pytest.mark.parametrize('tag_name', ["test"])
    def test_delete_tag(self, tag_name):
        tag_id = self.wework.get_tag_id(tag_name)
        r = self.wework.delete_tag(tag_id)
        assert r.json()['errcode'] == 0
        r = self.wework.get_tag()
        assert tag_id not in jsonpath(r.json(), '$..id')
