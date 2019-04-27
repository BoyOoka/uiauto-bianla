from atx.ext.chromedriver import ChromeDriver
import uiautomator2 as u2
import time

# d = atx.connect()
d = u2.connect('192.168.1.100')
# d.start_app('com.tencent.mm')
d.app_start('com.tencent.mm')
time.sleep(9)
driver = ChromeDriver(d).driver(package='com.tencent.mm', attach=True, activity='com.tencent.mm.ui.LauncherUI', process='com.tencent.mm:tools')

print(1)
print(driver.current_url)
driver.find_element_by_id('globalSearch').click()
time.sleep(3)
driver.find_element_by_id('serachInput').send_keys('彭义号')
driver.quit()
