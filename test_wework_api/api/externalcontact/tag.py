import json

import allure
import requests
from jsonpath import jsonpath

from test_wework_api.api.wework_api import WeWork


class Tag(WeWork):

    @allure.step("获取标签")
    def get_tag(self):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?",
            "method": "post",
            "params": {
                "access_token": self.token
            },
            "json": {}
        }
        r = self.http_request(data)
        # self.save(data, r)
        return r

    @allure.step("增加标签")
    def add_tag(self, group_name, tag_list, **kwargs):
        if 'json' in kwargs:
            json_data = kwargs['json']
        else:
            json_data = {
                "group_name": group_name,
                "tag": tag_list
            }
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?",
            "method": "post",
            "params": {
                "access_token": self.token
            },
            "json": json_data
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("编辑标签")
    def edit_tag(self, tag_id, tag_name):
        json_data = {
            "id": tag_id,
            "name": tag_name
        }
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag?",
            "method": "post",
            "params": {
                "access_token": self.token
            },
            "json": json_data
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("删除标签")
    def delete_tag(self, tag_id_list):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag?",
            "method": "post",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": tag_id_list
            }
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    # 清理所有tag
    @allure.step("清理所有标签")
    def clear(self):
        r = self.get_tag()
        # 获取所有tag_id
        # tag_id_list = [tag['id'] for group in r.json()['tag_group'] for tag in group['tag']]
        tag_id_list = jsonpath(r.json(), '$..tag[*].id')
        r = self.delete_tag(tag_id_list)
        return r

    # 根据tag_name获取tag_id
    @allure.step("根据tag_name获取tag_id")
    def get_tag_id(self, tag_name):
        r = self.get_tag()
        # tags 二维数组
        tags = jsonpath(r.json(), '$..tag')
        # print(tags[1][0]['name'])
        for i in range(0, len(tags)):
            for j in range(0, len(tags[i])):
                if tag_name == tags[i][j]['name']:
                    # print(tags[i][j]['name'])
                    tag_id = tags[i][j]['id']
                    break
        return tag_id

    # 根据tag_name_list获取tag_id_list
    @allure.step("根据tag_name_list获取tag_id_list")
    def get_tag_id_list(self, tag_name_list):
        r = self.get_tag()
        tag_id_list = []
        # tags 二维数组
        tags = jsonpath(r.json(), '$..tag')
        # print(tags[0][0]['name'])
        for k in range(len(tag_name_list)):
            for i in range(0, len(tags)):
                for j in range(0, len(tags[i])):
                    if tag_name_list[k] == tags[i][j]['name']:
                        tag_id_list.append(tags[i][j]['id'])
        return tag_id_list

    # 根据tag_name_list获取tag_id_list，通过jsonpath
    @allure.step("根据tag_name_list获取tag_id_list，通过jsonpath")
    def get_tag_id_list_2(self, tag_name_list):
        r = self.get_tag()
        tag_id_list = []
        for tag_name in tag_name_list:
            # jsonpath返回结果为列表，[0]取出列表中的字符串
            tag_id_list.append(jsonpath(r.json(), f"$..tag[?(@.name=='{tag_name}')].id")[0])
        return tag_id_list

        # jsonpath https://blog.csdn.net/lwg_1540652358/article/details/84111339
        # [?(< expression >)] 过滤表达式。 表达式必须求值为一个布尔值。
        # .< name > 点，表示子节点
        # jsonpath返回结果为列表，[0]取出列表中的字符串
        # print(jsonpath(r, f"$..tag[?(@.name=='NAME1')].id")[0])

    @allure.step("请求数据和响应结果")
    def save(self, data, r):
        allure.attach(f"{json.dumps(data, indent=2, ensure_ascii=False)}", "请求的数据", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"{json.dumps(r.json(), indent=2, ensure_ascii=False)}", "响应的数据",
                      attachment_type=allure.attachment_type.TEXT)
