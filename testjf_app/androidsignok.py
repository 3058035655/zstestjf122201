# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["appPackage"] = "com.yrtz.qiankundai"
caps["appActivity"] = ".activity.LoginActivity"
caps["deviceName"] = "demo"
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.yrtz.qiankundai:id/edit_psw")
el1.click()
el1.send_keys("txsynyh88")
el3 = driver.find_element_by_id("com.yrtz.qiankundai:id/btn_login")
el3.click()
driver.back()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView")
el2.click()
# el6 = driver.find_element_by_id("com.yrtz.qiankundai:id/vi_shanghu")
# el6.click()
time.sleep(2)
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.GridView/android.widget.RelativeLayout[7]")
el7.click()
el8 = driver.find_element_by_id("com.yrtz.qiankundai:id/iv_tbb_back")
el8.click()
el9 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.ImageView")
el9.click()

# el3 = driver.find_element_by_id("com.yrtz.qiankundai:id/rl_11_personal")
# el3.click()
# el4 = driver.find_element_by_id("com.yrtz.qiankundai:id/btn_out")
# el4.click()
# el5 = driver.find_element_by_id("com.yrtz.qiankundai:id/bt_right")
# el5.click()

driver.quit()