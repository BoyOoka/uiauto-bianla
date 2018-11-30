import uiautomator2 as u2
import time

# d = u2.connect("192.168.13.250")
# d.app_start("com.bianla.app")
# print(d.device_info)
time1 = time.time()
now = time.localtime(time1)
rightnow = time.strftime("%Y-%m-%d %H:%M:%S", now)
print(rightnow)