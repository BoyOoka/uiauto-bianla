from ddt import ddt, data, unpack
from selenium import webdriver
import xlrd, unittest, time


def get_data(file_name):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    # print(sheet.nrows)
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
        print(sheet.row_values(1,0))
        print(row_idx, sheet.ncols)
    # print(rows)
    return rows


@ddt
class SearchTestDDTExcel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*get_data('testdata.xlsx'))
    @unpack
    def test_search_excel(self, search_value, expect_value):
        """搜索测试_excel"""
        serch_filed = self.driver.find_element_by_id('kw')
        serch_filed.clear()
        serch_filed.send_keys(search_value)
        self.driver.find_element_by_id('su').click()
        time.sleep(0.8)
        title_text = self.driver.title
        self.assertEqual(title_text, expect_value)


if __name__ == '__main__':
   unittest.main()
