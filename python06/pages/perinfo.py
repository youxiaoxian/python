from appium.webdriver.common.mobileby import MobileBy

from python06.pages.base_page import BasePage
from python06.pages.perinfomore_page import PerInfoMorePage


class PerInfoPage(BasePage):
    __more = (MobileBy.XPATH,
              "//*[@text='个人信息']/../../../../../android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")

    def goto_per_info_more_page(self):
        # 个人信息页面，点击页面右上角竖着的3个点，进入个人信息更多页面
        self.find(*self.__more).click()
        return PerInfoMorePage(self.driver)
