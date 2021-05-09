from appium import webdriver

from python06.pages.base_page import BasePage
from python06.pages.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 初始化
            caps = {}
            caps["platformName"] = "android"
            # 包名
            caps["appPackage"] = "com.tencent.wework"
            # 启动页
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "test"
            # 等待页面空闲的时间
            caps["settings[waitForIdleTimeout]"] = 0
            # caps['dontStopAppOnReset'] = True
            caps["noReset"] = "true"
            caps["skipDeviceInitialization"] = "true"
            # 客户端与服务端建立连接
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 隐式等待，中间任何时间等到某个元素都停止查找，继续往后执行
            # 每次调用find_element的时候都会激活这种等待方式
            self.driver.implicitly_wait(20)

        else:
            self.driver.launch_app()

        # 为了可以调用实例本身的方法
        return self

    def quit(self):
        self.driver.quit()

    def stop(self):
        self.driver.close_app()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main_page(self):
        # 进入到app首页
        return MainPage(self.driver)
