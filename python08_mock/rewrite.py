"""HTTP-specific events."""
import json
import mitmproxy.http

class Events:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        # # 匹配规则
        # if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url \
        #         and "x=" in flow.request.url:
        #     print("雪球"*10)
    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # if 条件代表匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url \
                and "x=" in flow.request.url:
            # print(flow.response.text)
            # print(type(flow.response.text)) #str
            # 数据的模拟
            data = json.loads(flow.response.text)
            # 修改股票名称数据
            # print(data["data"]["items"][0]["quote"]["name"])
            # data["data"]["items"][0]["quote"]["name"] = "游仙测试1"
            # data["data"]["items"][1]["quote"]["name"] = "游仙测试2"
            # data["data"]["items"][2]["quote"]["name"] = "游仙测试3"
            # 修改股票涨跌幅数据
            data["data"]["items"][0]["quote"]["percent"] = "0.01"
            data["data"]["items"][1]["quote"]["percent"] = "-0.01"
            data["data"]["items"][2]["quote"]["percent"] = "0"

            # 修改响应
            flow.response.text = json.dumps(data)

addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    # 使用debug模式启动mitmdump
    # mitmdump(['-p', '8080', '-s', __file__])
    # mitmdump -p 8080 -s /Users/youxian/Desktop/work02/python08_mock/rewrite.py
    # 端口需要使用字符串
    mitmdump(['-p', '8080', "-s", __file__])