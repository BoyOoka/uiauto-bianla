from appium import webdriver
from selenium.webdriver.common.by import By
import time
Desired_Cap = {
  "platformName": "Android",
  "platformVersion": "8.1",
  "deviceName": "3487e851",
  # "app": "C:/Users/gaya/Desktop/weixin.apk",
  "app": "C:/Users/gaya/Desktop/3.9dev.apk",
   "appPackage":"com.bianla.app",
    "appActivity":"com.bianla.app.splash.SplashActivity",
# "chromeOptions": {'androidProcess': 'com.tencent.mm:tools'},
  "noReset": "true"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Desired_Cap)
time.sleep(10)
print(driver.contexts)
print(driver.context)
# driver._switch_to.context('WEBVIEW_com.tencent.mm:tools')
driver._switch_to.context('WEBVIEW_com.bianla.app')
print(driver.current_url)
print(driver.context)
# driver.find_element(By.ID, "globalSearch").click()
driver.find_element_by_class_name("pic").click()
