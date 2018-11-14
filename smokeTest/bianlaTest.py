import uiautomator2 as u2
import unittest
from uiauto import *
import time
# import HTMLReport





class bianlaTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.d = u2.connect("192.168.13.250")
        self.d.screen_on()
        self.d.swipe(552, 1771, 552, 950, 0.3)
        self.d.app_start("com.bianla.app")
        if(self.d(resourceId="com.bianla.app:id/btn_register_login").wait(3)):
           wait_click(self.d, "id", "com.bianla.app:id/btn_register_login")
           wait_click(self.d, "id", "com.bianla.app:id/tv_login")
           wait_sendkeys(self.d, "id", "com.bianla.app:id/login_account_et", "10000000960")
           wait_sendkeys(self.d, "id", "com.bianla.app:id/login_password_et", "123456")
           wait_click(self.d, "id", "com.bianla.app:id/login")
    @classmethod
    def tearDownClass(self):
        pass
        self.d.app_stop("com.bianla.app")

    def visitor_01_add(self):
        wait_click(self.d,"id", "com.bianla.app:id/iv_user")
        wait_click(self.d,"text", "添加访客")
        self.d(resourceId="com.bianla.app:id/et_nick").set_text("1")
        wait_sendkeys(self.d,"id", "com.bianla.app:id/et_nick","auto访客女")
        wait_sendkeys(self.d, "id", "com.bianla.app:id/age_tv", "34")
        wait_click(self.d, "id", "com.bianla.app:id/height")
        wait_click(self.d, "id", "com.bianla.app:id/confirm")
        wait_sendkeys(self.d, "id", "com.bianla.app:id/phone","13281549858")
        self.d.press("back")
        wait_click(self.d, "id", "com.bianla.app:id/signup_commit")
        self.d.toast.get_message(5.0,1,"添加访客成功")
        self.d.toast.show("Hello world")


        print("visitor_01_add", self.d.device_info)
        pass
    def visitor_02_check(self):
        print("visitor_02_add", self.d.device_info)
        pass
    def visitor_03_delete(self):
        pass


def Test_Suite():
# 构建测试集并添加Case
    suite = unittest.TestSuite()
    suite.addTest(bianlaTest('visitor_01_add'))
    suite.addTest(bianlaTest('visitor_02_check'))
    return suite

if __name__ == '__main__':
    # 启动指定的测试集
    runner = unittest.TextTestRunner()
    runner.run(Test_Suite())
