import uiautomator2 as u2
import unittest
from uiauto import *
import HTMLReport
import datetime
import time


class BianLaTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.d = u2.connect("10.20.122.241")
        self.d.screen_on()
        self.d.swipe(552, 1771, 552, 950, 0.2)
        self.d.app_start("com.bianla.app")
        if(self.d(resourceId="com.bianla.app:id/btn_register_login").wait(2)):
           wait_click(self.d, "id", "com.bianla.app:id/btn_register_login")
           wait_click(self.d, "id", "com.bianla.app:id/tv_login")
           wait_sendkeys(self.d, "id", "com.bianla.app:id/login_account_et", "10000000963")
           wait_sendkeys(self.d, "id", "com.bianla.app:id/login_password_et", "123456")
           wait_click(self.d, "id", "com.bianla.app:id/login")
           wait_click(self.d, "id", "com.bianla.app:id/iv_i_know")
    @classmethod
    def tearDownClass(self):
        # self.d.app_stop("com.bianla.app")
        pass

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
        # self.d.toast.get_message()
        # self.d.toast.show("Hello world")
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

        fft_left = self.d(resourceId="com.bianla.app:id/fft",instance=0).get_text()
        fft_right = self.d(resourceId="com.bianla.app:id/fft",instance=1).get_text()
        optimal_weight_left = self.d(resourceId="com.bianla.app:id/optimal_weight", instance=0).get_text()
        optimal_weight_right = self.d(resourceId="com.bianla.app:id/optimal_weight", instance=1).get_text()
        optimal_fat_left = self.d(resourceId="com.bianla.app:id/optimal_fat", instance=0).get_text()
        optimal_fat_right = self.d(resourceId="com.bianla.app:id/optimal_fat", instance=1).get_text()
        bmi_left = self.d(resourceId="com.bianla.app:id/bmi",instance=0).get_text()
        bmi_right = self.d(resourceId="com.bianla.app:id/bmi", instance=1).get_text()
        for i in range(0, 10):
            title_left.append(self.d(resourceId="com.bianla.app:id/title", instance=i).get_text())
            value_left.append(self.d(resourceId="com.bianla.app:id/t_value", instance=i).get_text())
            grade_left.append(self.d(resourceId="com.bianla.app:id/hit", instance=i).get_text())

        for j in range(10, 19):
            title_right.append(self.d(resourceId="com.bianla.app:id/title", instance=j).get_text())
            value_right.append(self.d(resourceId="com.bianla.app:id/t_value", instance=j).get_text())
            grade_right.append(self.d(resourceId="com.bianla.app:id/hit", instance=j).get_text())
        fat_reduce = self.d(resourceId="com.bianla.app:id/tv_fat_value").get_text()
        weight_reduce = self.d(resourceId="com.bianla.app:id/tv_weight_value").get_text()
        date_before = self.d(resourceId="com.bianla.app:id/tv_fat_loss_before").get_text()
        date_after = self.d(resourceId="com.bianla.app:id/tv_fat_loss_after").get_text()
        day_num = self.d(resourceId="com.bianla.app:id/tv_day_num").get_text()
        date_before_strp = datetime.datetime.strptime(date_before, "%Y-%m-%d")
        date_after_strp = datetime.datetime.strptime(date_after, "%Y-%m-%d")
        reduce_days = date_after_strp-date_before_strp
        print(title_left)
        print(value_left)
        print(grade_left)
        print(title_right)
        print(value_right)
        print(grade_right)
        print(fft_left, fft_right, optimal_fat_left, optimal_fat_right, optimal_weight_left, optimal_weight_right, bmi_left, bmi_right)
        self.d.press('back')
        wait_click(self.d, "id", "com.bianla.app:id/btn_cancel")
        loss_fat = round(float(value_left[3]) - float(value_right[3]), 1)
        loss_weight = round(float(value_left[1]) - float(value_right[1]), 1)
        self.assertEqual(int(day_num), reduce_days.days, "减脂天数")
        self.assertEqual(float(fat_reduce), loss_fat, '减脂')
        self.assertEqual(float(weight_reduce), loss_weight, '减重')
        #单位切换
        wait_click(self.d, "text", "我的")
        wait_click(self.d, "text", "系统设置")
        if fft_left.endswith('g'):
            wait_click(self.d, "id", "com.bianla.app:id/tv_05kg")
        else:
            wait_click(self.d, "id", "com.bianla.app:id/tv_kg")
        wait_click(self.d, "id", "com.bianla.app:id/iv_back")
        wait_click(self.d, "id", "com.bianla.app:id/home_bottom_button_image")

        title_left = []
        value_left = []
        grade_left = []
        title_right = []
        value_right = []
        grade_right = []
        wait_click(self.d, "id", "com.bianla.app:id/iv_share")
        wait_click(self.d, "id", "com.bianla.app:id/share_style_01")
        self.d(resourceId="com.bianla.app:id/title").click()

        fft_left = self.d(resourceId="com.bianla.app:id/fft", instance=0).get_text()
        fft_right = self.d(resourceId="com.bianla.app:id/fft", instance=1).get_text()
        optimal_weight_left = self.d(resourceId="com.bianla.app:id/optimal_weight", instance=0).get_text()
        optimal_weight_right = self.d(resourceId="com.bianla.app:id/optimal_weight", instance=1).get_text()
        optimal_fat_left = self.d(resourceId="com.bianla.app:id/optimal_fat", instance=0).get_text()
        optimal_fat_right = self.d(resourceId="com.bianla.app:id/optimal_fat", instance=1).get_text()
        bmi_left = self.d(resourceId="com.bianla.app:id/bmi", instance=0).get_text()
        bmi_right = self.d(resourceId="com.bianla.app:id/bmi", instance=1).get_text()
        for i in range(0, 10):
            title_left.append(self.d(resourceId="com.bianla.app:id/title", instance=i).get_text())
            value_left.append(self.d(resourceId="com.bianla.app:id/t_value", instance=i).get_text())
            grade_left.append(self.d(resourceId="com.bianla.app:id/hit", instance=i).get_text())

        for j in range(10, 19):
            title_right.append(self.d(resourceId="com.bianla.app:id/title", instance=j).get_text())
            value_right.append(self.d(resourceId="com.bianla.app:id/t_value", instance=j).get_text())
            grade_right.append(self.d(resourceId="com.bianla.app:id/hit", instance=j).get_text())
        fat_reduce = self.d(resourceId="com.bianla.app:id/tv_fat_value").get_text()
        weight_reduce = self.d(resourceId="com.bianla.app:id/tv_weight_value").get_text()
        date_before = self.d(resourceId="com.bianla.app:id/tv_fat_loss_before").get_text()
        date_after = self.d(resourceId="com.bianla.app:id/tv_fat_loss_after").get_text()
        day_num = self.d(resourceId="com.bianla.app:id/tv_day_num").get_text()
        #返回首页
        self.d.press('back')
        wait_click(self.d, "id", "com.bianla.app:id/btn_cancel")

        date_before_strp = datetime.datetime.strptime(date_before, "%Y-%m-%d")
        date_after_strp = datetime.datetime.strptime(date_after, "%Y-%m-%d")
        reduce_days = date_after_strp - date_before_strp
        loss_fat = round(float(value_left[3]) - float(value_right[3]), 1)
        loss_weight = round(float(value_left[1]) - float(value_right[1]), 1)

        #断言
        self.assertEqual(int(day_num), reduce_days.days, "减脂天数")
        self.assertEqual(float(fat_reduce), loss_fat, '减脂')
        self.assertEqual(float(weight_reduce), loss_weight, '减重')

    def share_02(self):
        pass

    def share_03(self):
        pass

    def share_04(self):
        pass

    def history_weight01(self):
        self.d(resourceId="com.bianla.app:id/tv_title", text="更多").click()
        wait_click(self.d, "text", "历史体重")
        wait_click(self.d, "id", "com.bianla.app:id/fat_weight_container")
        wait_click(self.d, "id", "com.bianla.app:id/button3")
        visitor_text = ""
        if(self.d(text="添加访客").wait()):
            visitor_text = self.d(text="添加访客").get_text()
            self.d(resourceId="com.bianla.app:id/title_left_bt").click()
        wait_click(self.d, "id", "com.bianla.app:id/fat_weight_container")
        wait_click(self.d, "id", "com.bianla.app:id/button1")
        wait_click(self.d, "des", "转到上一层级")
        wait_click(self.d, "id", "com.bianla.app:id/iv_green_delete")
        wait_click(self.d, "id", "com.bianla.app:id/cancel")
        wait_click(self.d, "id", "com.bianla.app:id/iv_green_delete")
        wait_click(self.d, "id", "com.bianla.app:id/delete")
        wait_click(self.d, "id", "com.bianla.app:id/fat_weight_container")
        wait_click(self.d, "id", "com.bianla.app:id/button2")

        #列表清除多余数据
        wait_click(self.d, "id", "com.bianla.app:id/ll_list_model_")
        wait_click(self.d, "id", "com.bianla.app:id/tv_management")
        wait_click(self.d, "id", "com.bianla.app:id/iv_green_delete")
        wait_click(self.d, "id", "com.bianla.app:id/delete")
        wait_click(self.d, "id", "com.bianla.app:id/tv_management")
        time.sleep(0.8)
        wait_click(self.d, "id", "com.bianla.app:id/fat_weight_container")
        #获取身体数据
        time.sleep(1)
        self.d.swipe(552, 1771, 552, 950, 0.8)
        title_hostory = []
        value_hostory = []
        grade_hostory = []
        for i in range(0, 10):
            title_hostory.append(self.d(resourceId="com.bianla.app:id/title", instance=i).get_text())
            value_hostory.append(self.d(resourceId="com.bianla.app:id/t_value", instance=i).get_text())
            grade_hostory.append(self.d(resourceId="com.bianla.app:id/hit", instance=i).get_text())
        wait_click(self.d, "des", "转到上一层级")
        wait_click(self.d, "id", "com.bianla.app:id/iv_back")

        #获取健康报告数据
        wait_click(self.d, "text", "健康报告")
        time.sleep(1)
        self.d.swipe(552, 1771, 552, 950, 0.8)
        title_report = []
        value_report = []
        grade_report = []

        for i in range(0, 10):
            title_report.append(self.d(resourceId="com.bianla.app:id/title", instance=i).get_text())
            value_report.append(self.d(resourceId="com.bianla.app:id/t_value", instance=i).get_text())
            grade_report.append(self.d(resourceId="com.bianla.app:id/hit", instance=i).get_text())
        print(title_hostory, value_hostory, grade_hostory)
        self.d.press('back')
        self.d.press('back')
        #断言
        self.assertEqual("添加访客", visitor_text, "访客页面")
        self.assertEqual(title_hostory, title_report, "标题")
        self.assertEqual(value_hostory, value_report, "数值")
        self.assertEqual(grade_hostory, grade_report, "等级")

    def weight_input(self):
        self.d(resourceId="com.bianla.app:id/tv_title", text="更多").click()
        wait_click(self.d, "text", "录入体重")
        if self.d(resourceId="com.bianla.app:id/btn_cancel").exists:
            sugest = self.d(resourceId="com.bianla.app:id/suggest_tv").get_text()
            self.assertEqual(sugest, "手动记录的身体数据不能代表您的真实身体数据如需获取个人真实数据，请使用体脂秤进行数据检测。","建议")
            wait_click(self.d, "id", "com.bianla.app:id/btn_cancel")
        self.d(resourceId="com.bianla.app:id/selection_roller_view").scroll(20)
        time.sleep(0.5)
        weight_in = self.d(resourceId="com.bianla.app:id/tv_selected_weight").get_text()
        wait_click(self.d, "id", "com.bianla.app:id/btn_add_weight")
        weight_get = self.d(resourceId="com.bianla.app:id/t_value",instance=1).get_text()

        if self.d(resourceId="com.bianla.app:id/t_unit").get_text() == '斤':
            self.assertEqual(round(float(weight_in),1)*2, float(weight_get), "体重")
        else:
            self.assertEqual(weight_in, weight_get, "体重")


def Test_Suite():
# 构建测试集并添加Case
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    #suite.addTests(loader.loadTestsFromTestCase(bianlaTest))
    suite.addTest(BianLaTest('visitor_01_add'))
    suite.addTest(BianLaTest('visitor_02_check'))
    suite.addTest(BianLaTest('visitor_03_delete'))
    suite.addTest(BianLaTest('share_01'))
    suite.addTest(BianLaTest('history_weight01'))
    suite.addTest(BianLaTest('weight_input'))
    return suite

if __name__ == '__main__':
    # 启动指定的测试集
    # runner = unittest.TextTestRunner()
    runner = HTMLReport.TestRunner(report_file_name='test'+datetime.datetime.now().strftime('%Y%m%d%H%M%S'),  # 报告文件名，如果未赋值，将采用“test+时间戳”
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
