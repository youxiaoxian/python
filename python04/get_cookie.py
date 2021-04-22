import yaml
from selenium import webdriver


def getcookie():
    # Windows/Linux命令为：chrome --remote-debugging-port=9222
    # Mac命令为：Google\ Chrome --remote-debugging-port=9222
    # 复用只支持chrome浏览器
    options = webdriver.ChromeOptions()
    # 设置debug地址
    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    driver.implicitly_wait(3)
    # 获取cookie信息
    cookie = driver.get_cookies()
    # 把cookie存如yaml文件内
    with open("./conf/data.yml", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)


if __name__ == '__main__':
    getcookie()
