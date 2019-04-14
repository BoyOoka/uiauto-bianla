from seleniumTestDDT.searchtestCSV import SearchTestDDTCSV
from seleniumTestDDT.searchtestData import SearchDDTData
from seleniumTestDDT.searchtestExcel import SearchTestDDTExcel
import unittest
from HTMLTestRunner_Chart.HTMLTestRunner_Chart import HTMLTestRunner

test1 = unittest.TestLoader().loadTestsFromTestCase(SearchTestDDTCSV)
test2 = unittest.TestLoader().loadTestsFromTestCase(SearchDDTData)
test3 = unittest.TestLoader().loadTestsFromTestCase(SearchTestDDTExcel)

smoke_test = unittest.TestSuite([test1, test2, test3])

runner = HTMLTestRunner(
    title='冒烟测试',
    stream=open('./testsuite.html', 'wb'),
    retry=0,
    description='',
    save_last_try=True,
    verbosity=2
)
runner.run(smoke_test)
