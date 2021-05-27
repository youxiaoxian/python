import allure
import pystache
import yaml
from jsonpath import jsonpath

from test_wework_api.api.wework_api import WeWork


class Member(WeWork):

    @allure.step("读取成员")
    def get_member(self, userid):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get?",
            "method": "GET",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("创建成员")
    def add_member(self, userid, name, mobile, department):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create?",
            "method": "POST",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
            }
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("获取部门成员")
    def get_department_member(self, department_id, FETCH_CHILD):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?",
            "method": "GET",
            "params": {
                "access_token": self.token,
                "department_id": department_id,
                "fetch_child": FETCH_CHILD

            }
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("创建成员,mustache框架")
    def add_member_mustache(self, userid, name, mobile, department):
        with open("../data/create_data.yaml", encoding="UTF-8") as f:
            body = yaml.safe_load(f)
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create?",
            "method": "POST",
            "params": {
                "access_token": self.token
            },
            "json": body
        }
        template = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }

        body["userid"] = pystache.render(body["userid"], template)
        body["name"] = pystache.render(body["name"], template)
        body["mobile"] = pystache.render(body["mobile"], template)
        # 结果为字符串str类型'[1, 2]'
        a = pystache.render(body["department"], template)
        # 将字符串转为列表['1', ' 2']
        b = a[1:len(a) - 1].strip(',').split(',')
        # 将列表中的字符转换为int，最后拼接成list
        body["department"] = []
        for i in b:
            d = int(i)
            body["department"].append(d)
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("删除成员")
    def delete_member(self, userid):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete?",
            "method": "GET",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("批量删除成员")
    def delete_all_member(self, useridlist):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?",
            "method": "POST",
            "params": {
                "access_token": self.token
            },
            "json": {
                "useridlist": useridlist
            }
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("数据清理")
    def clear(self):
        r = self.get_department_member(1, 1)
        useridlist = jsonpath(r.json(), '$..userid')
        useridlist_excludemy = []
        for userid in useridlist:
            if userid != 'DaXia':
                useridlist_excludemy.append(userid)
        r = self.delete_all_member(useridlist_excludemy)
        return r
