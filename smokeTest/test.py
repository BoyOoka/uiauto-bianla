import uiautomator2 as u2


d = u2.connect("192.168.13.250")
d.app_start("com.bianla.app")
print(d.device_info)
