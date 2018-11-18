import uiautomator2 as u2
import atx
import unittest
from uiauto import *
import HTMLReport
import time
from atx.ext.chromedriver import ChromeDriver





class bianlaTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # self.d = u2.connect("192.168.13.250")
        self.d = u2.connect('192.168.0.133')
        # self.d = u2.connect('192.168.0.109')
        self.d.screen_on()
        self.d.swipe(552, 1771, 552, 950, 0.2)
        self.d.app_start("com.bianla.app")
        if(self.d(resourceId="com.bianla.app:id/btn_register_login").wait(2)):
           wait_click(self.d, "id", "com.bianla.app:id/btn_register_login")
           wait_click(self.d, "id", "com.bianla.app:id/tv_login")
           wait_sendkeys(self.d, "id", "com.bianla.app:id/login_account_et", "10000000962")
           wait_sendkeys(self.d, "id", "com.bianla.app:id/login_password_et", "123456")
           wait_click(self.d, "id", "com.bianla.app:id/login")
           wait_click(self.d, "id", "com.bianla.app:id/iv_i_know")
    @classmethod
    def tearDownClass(self):
        # self.d.app_stop("com.bianla.app")
        pass

    def test_visitor_01_add(self):
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
        # self.d.toast.get_message()
        # self.d.toast.show("Hello world")
        # time.sleep(6)
        # print(self.d.current_app(), self.d.device_info)
        # # driver = web_driver(self.d)
        # dx = atx.connect(self.d.device_info['serial'])
        # info = self.d.current_app()
        # driver = ChromeDriver(dx).driver(info['package'], True, info['activity'], info['package'])
        # print('打印网址', driver.current_url)
        # driver.close()
        # print(find_toast(self.d, '添加访客成功'))


        #添加访客男
        wait_click(self.d, "text", "添加访客")
        wait_click(self.d, "id", "com.bianla.app:id/male_icon")
        wait_sendkeys(self.d, "id", "com.bianla.app:id/et_nick", "auto访客男")
        wait_sendkeys(self.d, "id", "com.bianla.app:id/age_tv", "42")
        wait_click(self.d, "id", "com.bianla.app:id/height")
        wait_click(self.d, "id", "com.bianla.app:id/confirm")
        wait_sendkeys(self.d, "id", "com.bianla.app:id/phone", "13281549858")
        self.d.press("back")
        wait_click(self.d, "id", "com.bianla.app:id/signup_commit")

    def visitor_02_check(self):
        title_text = ""
        wait_click(self.d, "id", "com.bianla.app:id/icon")
        wait_click(self.d, "text", "上 秤")
        title_text =  self.d(resourceId="com.bianla.app:id/dialog_title_tv").get_text(3)
        wait_click(self.d, "id", "com.bianla.app:id/close")
        wait_click(self.d, "id", "com.bianla.app:id/title_left_bt")
        self.assertEqual(title_text, "同步数据")

    def visitor_03_delete(self):
        wait_click(self.d, "id", "com.bianla.app:id/text")
        wait_click(self.d, "id", "com.bianla.app:id/select_user_cb")
        self.d(resourceId="com.bianla.app:id/select_user_cb", className="android.widget.CheckBox", instance=1).click()
        wait_click(self.d, "id", "com.bianla.app:id/delete_select_tv")
        wait_click(self.d, "text", "确定")
        wait_click(self.d, "id", "com.bianla.app:id/title_left_bt")
    def share_01(self):
        title_left = []
        value_left = []
        grade_left = []
        title_right = []
        value_right = []
        grade_right = []
        wait_click(self.d, "id", "com.bianla.app:id/iv_share")
        wait_click(self.d, "id", "com.bianla.app:id/share_style_01")
        self.d(resourceId="com.bianla.app:id/title").click()
        for i in range(0, 10):
            title_left.append(self.d(resourceId="com.bianla.app:id/title", instance=i).get_text())
            value_left.append(self.d(resourceId="com.bianla.app:id/t_value", instance=i).get_text())
            grade_left.append(self.d(resourceId="com.bianla.app:id/hit", instance=i).get_text())
        print(title_left)
        print(value_left)
        print(grade_left)
        for j in range(10, 19):
            title_right.append(self.d(resourceId="com.bianla.app:id/title", instance=j).get_text())
            value_right.append(self.d(resourceId="com.bianla.app:id/t_value", instance=j).get_text())
            grade_right.append(self.d(resourceId="com.bianla.app:id/hit", instance=j).get_text())
        print(title_right)
        print(value_right)
        print(grade_right)
        pass
    def share_02(self):
        pass
    def share_03(self):
        pass
    def share_04(self):
        pass


def Test_Suite():
# 构建测试集并添加Case
    suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    # suite.addTests(loader.loadTestsFromTestCase(bianlaTest))
    suite.addTest(bianlaTest('test_visitor_01_add'))
    # suite.addTest(bianlaTest('visitor_02_check'))
    # suite.addTest(bianlaTest('visitor_03_delete'))
    suite.addTest(bianlaTest('share_01'))
    return suite

if __name__ == '__main__':
    # 启动指定的测试集
    # runner = unittest.TextTestRunner()
    runner = HTMLReport.TestRunner(report_file_name='test',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                   output_path='report',  # 保存文件夹名，默认“report”
                                   title='测试报告',  # 报告标题，默认“测试报告”
                                   description='无测试描述',  # 报告描述，默认“测试描述”
                                   thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                   thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                                   sequential_execution=False,  # 是否按照套件添加(addTests)顺序执行，
                                   # 会等待一个addTests执行完成，再执行下一个，默认 False
                                   # 如果用例中存在 tearDownClass ，建议设置为True，
                                   # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                   # lang='en'
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
    runner.run(Test_Suite())
