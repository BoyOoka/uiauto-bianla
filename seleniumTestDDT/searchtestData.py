from selenium import webdriver
import unittest
from ddt import ddt, data, unpack
import time


@ddt
class SearchDDTData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(('test1', 'test1_百度搜索'), ('test2', 'test_百度搜索'))
    @unpack
    def test_search_data(self, search_value, expect_value):
        """搜索测试"""
        serch_filed = self.driver.find_element_by_id('kw')
        serch_filed.clear()
        serch_filed.send_keys(search_value)
        self.driver.find_element_by_id('su').click()
        time.sleep(0.8)
        title_text = self.driver.title
        self.assertEqual(title_text, expect_value)


if __name__ == '__main__':

    unittest.main(verbosity=2)
