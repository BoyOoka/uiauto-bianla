from ddt import ddt, data, unpack
from selenium import webdriver
import csv, unittest, time


def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    # 跳过第一行
    next(reader, None)
    for row in reader:
        rows.append(row)
    # print(rows)
    return rows


@ddt
class SearchTestDDTCSV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*get_data('testdata.csv'))
    @unpack
    def test_search_csv(self, search_value, expect_value):
        """搜索测试_CSV"""
        serch_filed = self.driver.find_element_by_id('kw')
        serch_filed.clear()
        serch_filed.send_keys(search_value)
        self.driver.find_element_by_id('su').click()
        time.sleep(0.8)
        title_text = self.driver.title
        self.assertEqual(title_text, expect_value)


if __name__ == '__main__':
   unittest.main()
