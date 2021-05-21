"""HTTP-specific events."""
import json
import mitmproxy.http
class Events:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        #匹配规则
        if "http://192.168.7.147:22000/apis/topicinfo/getpagelist?topicid=" in flow.request.url:
            old_data = json.loads(flow.response.text)
            new_data = self.recursion(old_data,2)
            # 返回给客户端
            # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
            flow.response.text = json.dumps(new_data,ensure_ascii=False)

    def recursion(self, base_data, int_data = 1):
        """
        :param base_data: 原始的数据
        :param int_data: 倍增的倍数
        :return: 在原始数据基础之上，对int类型数据做翻倍操作
        """
        #
        if isinstance(base_data, dict):
            # 如果是字典类型，继续递归value值
            # for k, v in base_data.items():
            #     if k in ('code','pageNum','pageSize','id','status','total'):
            #         continue
            #     else:
            #         base_data[k] = self.recursion(v, int_data)
            for k, v in base_data.items():
                if k in ('data','rows','devNums'):
                    base_data[k] = self.recursion(v, int_data)
                else:
                    continue
        elif isinstance(base_data, list):
            # 递归算法，如果是list 就继续遍历列表中的元素
            for i in base_data:
                self.recursion(i, int_data)
            # [self.recursion(i, int_data) for i in base_data]
        elif isinstance(base_data, int):
            # 对int型数据做倍增
            base_data = base_data * int_data
        else:
            base_data = base_data
        return base_data

addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    # 使用debug模式启动mitmdump
    # mitmdump(['-p', '8888', '-s', __file__])
    # mitmdump -p 8888 -s /Users/youxian/Desktop/work02/python08_mock/recursion.py
    # 端口需要使用字符串
    mitmdump(['-p', '8888', "-s", __file__])

