import requests
from jsonpath import jsonpath


class Wework:
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
        params = {
            "corpid": "ww782d957a1dfa5f5f",
            "corpsecret": "XzWffUR_06xA1rktB3uCGkToykg88RrJCySCJAY39D0"
        }
        r = requests.get(url=url, params=params)
        token = r.json()['access_token']
        return token

    def get_tag(self):
        token = self.get_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?"
        params = {
            "access_token": token
        }
        data = {}
        r = requests.post(url=url, params=params, json=data)
        return r

    def add_tag(self,group_name,tag_name):
        token = self.get_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?"
        params = {
            "access_token": token
        }
        data = {
            "group_name": group_name,
            "tag": [{
                "name": tag_name,
            }],
        }
        r = requests.post(url=url, params=params, json=data)
        return r

    def edit_tag(self,tag_id,tag_name):
        token = self.get_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag?"
        params = {
            "access_token": token
        }
        data = {
            "id": tag_id,
            "name": tag_name
        }
        r = requests.post(url=url, params=params, json=data)
        return r

    def delete_tag(self,tag_id):
        token = self.get_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag?"
        params = {
            "access_token": token
        }
        data = {
            "tag_id": [
                tag_id
            ]
        }
        r = requests.post(url=url, params=params, json=data)
        return r

    def get_tag_id(self,tag_name):
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


