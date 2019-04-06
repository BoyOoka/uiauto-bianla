import unittest
from selenium import webdriver
from HTMLTestRunner_Chart.HTMLTestRunner_Chart import HTMLTestRunner


class chrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_case_01_a(self):
        '''测试1'''
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys('qwe')
        self.driver.find_element_by_id('su').click()
    def test_case_02(self):
        '''测试2'''
        self.driver.get("https://new.ztestin.com/tasks/index")

if __name__ == '__main__':

    suite = unittest.TestSuite
    suite.addTest(chrome("test_case_01_a"))
    runner = HTMLTestRunner(
        title='测试',
        description='描述',
        stream = open("./demo.html", "wb"),
        verbosity=2,
        retry=0,
        save_last_try=True
    )
    runner.run(suite)
