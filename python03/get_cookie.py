import yaml
from selenium import webdriver


def getcookie():
    # 复用只支持chrome浏览器
    options = webdriver.ChromeOptions()
    # 设置debug地址
    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    driver.implicitly_wait(5)
    # 获取cookie信息
    cookie = driver.get_cookies()
    # 把cookie存如yaml文件内
    with open("./conf/data.yml", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)
