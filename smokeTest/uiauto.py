from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from atx.ext.chromedriver import ChromeDriver
import atx


def wait_click(d, selector, text, time = 3):
    if (selector == "id"):
        d(resourceId=text).wait(time)
        d(resourceId=text).click()
    if (selector == "text"):
        d(text=text).wait(time)
        d(text=text).click()
    if (selector == "des"):
        d(description=text).wait(time)
        d(description=text).click()




def wait_sendkeys(d, selector, text, keys, time=3):
    if(selector == "id"):
        if(d(resourceId=text).wait(time)):
            d(resourceId=text).set_text(keys)


def find_toast(d, toast):
    dx = atx.connect(d.device_info['serial'])
    info = d.current_app()
    driver = ChromeDriver(dx).driver(info['package'], True, info['activity'], info['package'])
    try:
        ele = WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located((By.XPATH, './/*[contains(@text,'+'\''+toast+'\''+')]')))
        return True
    except:
        return False


def web_driver(d):
    dx = atx.connect(d.device_info['serial'])
    info = d.current_app()
    driver = ChromeDriver(dx).driver(info['package'], True, info['activity'], info['package'])
    return driver
