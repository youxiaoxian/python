
from test_wework_api.api.base_api import BaseApi


class WeWork(BaseApi):
    token: str = None
    def get_token(self):
        data={
            'url': "https://qyapi.weixin.qq.com/cgi-bin/gettoken?",
            'method': "get",
            'params': {
                "corpid": "ww782d957a1dfa5f5f",
                "corpsecret": "XzWffUR_06xA1rktB3uCGkToykg88RrJCySCJAY39D0"
            }
        }
        r = self.http_request(data)
        assert r.status_code == 200
        self.token = r.json()['access_token']