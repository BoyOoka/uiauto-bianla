import atx
from atx.ext.chromedriver import ChromeDriver
import time

d = atx.connect()
d.start_app('com.tencent.mm')
driver = ChromeDriver(d).driver(package='com.tencent.mm', attach=True, activity='com.tencent.mm.ui.LauncherUI', process='com.tencent.mm:tools')
time.sleep(9)
print(1)
print(driver.current_url)
driver.find_element_by_id('globalSearch').click()
time.sleep(3)
driver.find_element_by_id('serachInput').send_keys('彭义号')
driver.quit()
