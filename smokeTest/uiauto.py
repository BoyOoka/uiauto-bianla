


def wait_click(d,selector,text):
    if(selector == "id"):
        if(d(resourceId=text).wait(3)):
            d(resourceId=text).click()
    if(selector == "text"):
        if (d(text=text).wait(3)):
            d(text=text).click()
def wait_sendkeys(d,selector,text,keys):
    if(selector == "id"):
        if(d(resourceId=text).wait(3)):
            d(resourceId=text).set_text(keys)