import allure
import pytest
from jsonpath import jsonpath
from test_wework_api.api.contact.member import Member


@allure.feature("通讯录成员管理")
class TestMember:
    def setup_class(self):
        self.member = Member()
        corpsecret = "zQtwpLtp5SWVvX4zLJvapfoTNeWIatsxbcxkkz1mzGw"
        self.member.get_token(corpsecret)
        self.member.clear()

    @allure.story("读取成员信息")
    @allure.title("成功读取成员")
    @pytest.mark.parametrize('userid', ['DaXia'])
    def test_get_member(self, userid):
        with allure.step("第一步：调用读取成员方法"):
            r = self.member.get_member(userid)
        with allure.step("第二步：断言读取成员方法errcode为0"):
            assert r.json()['errcode'] == 0
        with allure.step("第三步：断言userid:DaXia的name是测试"):
            assert r.json()['name'] == "测试"

    @allure.story("获取部门成员信息")
    @allure.title("成功获取部门成员")
    @pytest.mark.parametrize('department_id,FETCH_CHILD', [[[1], 1]])
    def test_get_department_member(self, department_id, FETCH_CHILD):
        with allure.step("第一步：调用获取部门成员方法"):
            r = self.member.get_department_member(department_id, FETCH_CHILD)
        with allure.step("第二步：断言获取部门成员方法的errcode为0"):
            assert r.json()['errcode'] == 0
        with allure.step("第二步：断言获取的部门成员list长度为1，因为因为在setup_class清理了除管理员外所有成员"):
            assert len(r.json()['userlist']) == 1

    @allure.story("创建成员")
    @allure.title("成功创建成员")
    @pytest.mark.parametrize('userid,name,mobile,department', [['zhangsan', 'zhangsan', '13800000000', [1]]])
    def test_add_member(self, userid, name, mobile, department):
        with allure.step("第一步：调用创建成员方法"):
            r = self.member.add_member(userid, name, mobile, department)
        with allure.step("第二步：断言调用创建成员方法errcode为0"):
            assert r.json()['errcode'] == 0
        with allure.step("第三步：断言调用创建成员方法errmsg为created"):
            assert r.json()['errmsg'] == "created"
        with allure.step("第四步：调用获取部门成员方法，部门1，不递归获取"):
            r = self.member.get_department_member(1, 0)
        with allure.step("第五步：断言新增的成员在获取部门1成员方法响应结果中"):
            assert userid in jsonpath(r.json(), '$..userid')

    @allure.story("创建成员")
    @allure.title("成功创建成员mustache框架")
    @pytest.mark.parametrize('userid,name,mobile,department', [['zhangsan1', 'zhangsan1', '13900000000', [3]]])
    def test_add_member_mustache(self, userid, name, mobile, department):
        with allure.step("第一步：调用创建成员方法，mustache框架"):
            r = self.member.add_member_mustache(userid, name, mobile, department)
        with allure.step("第二步：断言调用创建成员方法errcode为0"):
            assert r.json()['errcode'] == 0
        with allure.step("第三步：断言调用创建成员方法errmsg为created"):
            assert r.json()['errmsg'] == "created"
        with allure.step("第四步：调用获取部门成员方法，部门3，不递归获取"):
            r = self.member.get_department_member(3, 0)
        with allure.step("第五步：断言新增的成员在获取部门3成员方法响应结果中"):
            assert userid in jsonpath(r.json(), '$..userid')

    @allure.story("删除成员")
    @allure.title("成功删除成员")
    @pytest.mark.skip(reason="这个测试用例暂时不执行，因为下面有1个批量删除成员的方法")
    @pytest.mark.parametrize('userid', ['zhangsan1'])
    def test_delete_member(self, userid):
        with allure.step("第一步：调用删除成员方法"):
            r = self.member.delete_member(userid)
        with allure.step("第二步：断言调用删除成员方法errcode为0"):
            assert r.json()['errcode'] == 0
        with allure.step("第三步：断言调用删除成员方法errmsg为deleted"):
            assert r.json()['errmsg'] == "deleted"
        with allure.step("第四步：调用获取部门成员方法，部门1，递归获取"):
            r = self.member.get_department_member(1, 1)
        with allure.step("第五步：断言删除的成员不在获取所有部门成员方法的响应结果中"):
            assert userid not in jsonpath(r.json(), '$..userid')

    @allure.story("批量删除成员")
    @allure.title("成功批量删除成员")
    @pytest.mark.parametrize('useridlist', [['zhangsan1', 'zhangsan']])
    def test_delete_all_member(self, useridlist):
        with allure.step("第一步：调用批量删除成员方法"):
            r = self.member.delete_all_member(useridlist)
        with allure.step("第二步：断言调用批量删除成员方法errcode为0"):
            assert r.json()['errcode'] == 0
        with allure.step("第三步：断言调用批量删除成员方法errmsg为deleted"):
            assert r.json()['errmsg'] == "deleted"
        with allure.step("第四步：调用获取部门成员方法，部门1，递归获取"):
            r = self.member.get_department_member(1, 1)
        with allure.step("第五步：断言删除的成员不在获取所有部门成员方法的响应结果中"):
            for userid in useridlist:
                assert userid not in jsonpath(r.json(), '$..userid')
