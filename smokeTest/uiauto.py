


def wait_click(d,selector,text):
    if(selector == "id"):
        if(d(resourceId=text).wait(3)):
            d(resourceId=text).click()
    if(selector == "text"):
        if (d(text=text).wait(3)):
            d(text=text).click()
def wait_sendkeys(d,reId,keys):

    if(d(resourceId=reId).wait(3)):
        d(resourceId=reId).send_keys(keys)