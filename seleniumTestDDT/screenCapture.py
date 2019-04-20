import unittest
from selenium import webdriver
# from castro import Castro


class ScreenCapture(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platform'] = 'WINDOWS'
        desired_caps['browserName'] = 'chrome'
        # cls.driver = webdriver.Chrome()
        cls.driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", desired_caps)
        cls.driver.get('https://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # cls.screenCapture.stop()

    def testCapture(self):
        # self.screenCapture = Castro()
        # self.screenCapture.start()
        self.driver.find_element_by_id('kw').send_keys('test')
        self.driver.find_element_by_id('su').click()
        # self.screenCapture.stop()


if __name__ == '__main__':
    unittest.main
