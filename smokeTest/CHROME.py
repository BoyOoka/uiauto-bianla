import unittest
from selenium import webdriver
from HTMLTestRunner_Chart.HTMLTestRunner_Chart import HTMLTestRunner



class chome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.imgs = []
        # self.addCleanup(self.cleanup)
    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_case_01_a(self):
        '''测试1'''
        self.driver.get("https://www.baidu.com")
        self.add_img()
        self.driver.find_element_by_id('kw').send_keys('qwe')
        self.add_img()
        self.driver.find_element_by_id('su').click()
        self.add_img()
    def test_case_02(self):
        '''测试2'''
        self.driver.get("https://new.ztestin.com/tasks/index")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(chome('test_case_01_a'))

    # suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    runner = HTMLTestRunner(
        title='测试',
        description='描述',
        stream = open("./demo.html", "wb"),
        verbosity=2,
        retry=0,
        save_last_try=True
    )
    runner.run(suite)
