import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddmember:
    def setup(self):
        # 初始化
        caps = {}
        caps["platformName"] = "android"
        # 包名
        caps["appPackage"] = "com.tencent.wework"
        # 启动页
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "test"
        caps["settings[waitForIdleTimeout]"] = 0
        caps["noReset"] = "true"
        # 客户端与服务端建立连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        # 资源销毁
        self.driver.quit()

    @pytest.mark.parametrize('name,phonenumber', [['测试10', '11122224441'], ['测试9', '11122224449']])
    def test_add_member(self, name, phonenumber):
        # 测试用例
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找某个元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()

        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ays").send_keys(name)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys(phonenumber)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'添加成功')]")
