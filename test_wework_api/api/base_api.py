import json
import logging

import requests


class BaseApi:
    def request(self,data: dict):
        if "url" in data:
            return self.http_request(data)
        # data.get("procotol")获取字典某个key的value
        if "rpc" == data.get("procotol"):
            return self.rpc_request(data)

    def http_request(self,data):
        r = requests.request(**data)
        # 换成logging
        logging.info("调用http_request请求")
        logging.info(f"请求的数据为{data}")
        logging.info(f"返回的数据为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r

    def rpc_request(self,data):
        pass

    def tcp_request(self,data):
        pass
