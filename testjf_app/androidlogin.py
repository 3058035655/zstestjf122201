# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
from appium import webdriver
# mCurrentFocus=Window{907e335 u0 com.yrtz.caixiangjia/com.yrtz.caixiangjia.ui.activity.SplashActivity
caps = {}
caps["platformName"] = "android"
caps["appPackage"] = "com.yrtz.caixiangjia"
caps["appActivity"] = ".ui.activity.SplashActivity"
caps["deviceName"] = "chuizi"
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
time.sleep(3)
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
def swipLeft(t):
    l=getSize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,t)
swipLeft(1000)
time.sleep(3)
swipLeft(1000)
time.sleep(3)
e3=driver.find_element_by_id("android:id/navigationBarBackground").click()
time.sleep(3)
e17=driver.find_element_by_id("com.yrtz.caixiangjia:id/edt_phone_number").send_keys("13301307172")
el8 = driver.find_element_by_id("com.yrtz.qiankundai:id/edit_psw")
el8.send_keys("a12345")
time.sleep(3)
