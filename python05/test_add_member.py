import pytest
from faker import Faker
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class TestAddmember:

    def setup_class(self):
        self.faker = Faker('zh-CN')
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

    def setup(self):
        # 首页的启动
        # 判断app的状态 http://appium.io/docs/en/commands/device/app/app-state/
        print(self.driver.query_app_state("com.tencent.wework"))
        if self.driver.query_app_state("com.tencent.wework") != 4:
            self.driver.launch_app()

    def teardown(self):
        # 首页的关闭
        self.driver.close_app()

    def teardown_class(self):
        # 资源销毁，销毁driver
        self.driver.quit()

    def swipe_find(self, text, num=2):
        # num,默认查找次数
        self.driver.implicitly_wait(1)
        for i in range(0, num):
            try:
                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return ele

            except NoSuchElementException:
                print('未找到,滑动')

            # 滑动一页，继续查找
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height']
            start_x = width / 2
            start_y = height * 0.8

            end_x = start_x
            end_y = height * 0.3
            duration = 2000  # ms
            # 完成滑动操作
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)

        if i == num - 1:
            self.driver.implicitly_wait(5)
            raise NoSuchElementException(f'找了{i + 1}次，未找到')

    @pytest.mark.parametrize('a', ['aa', 'bb'])
    def test_add_member(self, a):
        # 测试用例
        # faker
        name = self.faker.name()
        phonenum = self.faker.phone_number()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找某个元素
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()

        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.swipe_find('添加成员').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'添加成功')]")
