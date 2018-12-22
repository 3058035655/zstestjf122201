# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
import unittest
from telnetlib import EC

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.config import APP_REPORT

appreport_path = APP_REPORT+"\\shotcut"

class Test_Androidlogin(unittest.TestCase):
    def test_androidLogin(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.yrtz.qiankundai"
        caps["appActivity"] = ".activity.LoginActivity"
        caps["deviceName"] = "demo"
        caps["noReset"] = "false"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.find_element_by_id("com.yrtz.qiankundai:id/edit_uid").send_keys("14510000051")
        driver.find_element_by_id("com.yrtz.qiankundai:id/edit_psw").send_keys("a12345")
        #登录
        driver.find_element_by_id("com.yrtz.qiankundai:id/btn_login").click()
        time.sleep(0.5)
        driver.back()
        time.sleep(3)
        #邀请好友
        # WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView")))
        yqhy=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView")
        self.assertEqual(yqhy.text,"邀请好友")
        #截图
        print("开始截屏了")
        # # driver.long_press_keycode (24,26)  # 音量+     25音量-
        # # driver.long_press_keycode(26)  #电源键
        # driver.press_keycode(24+26)
        # driver.press_keycode(3)
        # print("点了home")
        driver.get_screenshot_as_file (appreport_path+"\\android截图.JPG")
        time.sleep(1)
        driver.quit()
if __name__ == '__main__':
    unittest.main ()
