

def wait_click(d, selector, text, time = 3):
    if(selector == "id"):
        if(d(resourceId=text).wait(time)):
            d(resourceId=text).click()
    if(selector == "text"):
        if (d(text=text).wait(time)):
            d(text=text).click()


def wait_sendkeys(d,selector,text,keys, time=3):
    if(selector == "id"):
        if(d(resourceId=text).wait(time)):
            d(resourceId=text).set_text(keys)