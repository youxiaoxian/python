import json

import allure

from test_wework_api.api.base_api import BaseApi


class WeWork(BaseApi):
    token: str = None
    def get_token(self,corpsecret):
        data={
            'url': "https://qyapi.weixin.qq.com/cgi-bin/gettoken?",
            'method': "get",
            'params': {
                "corpid": "ww782d957a1dfa5f5f",
                "corpsecret": corpsecret
            }
        }
        r = self.http_request(data)
        assert r.status_code == 200
        self.token = r.json()['access_token']

    @allure.step("请求数据和响应结果的保存")
    def save(self, data, r):
        allure.attach(f"{json.dumps(data, indent=2, ensure_ascii=False)}", "请求的数据", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"{json.dumps(r.json(), indent=2, ensure_ascii=False)}", "响应的数据",
                      attachment_type=allure.attachment_type.TEXT)