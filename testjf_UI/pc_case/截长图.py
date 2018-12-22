#-*- coding:utf-8 -*-
import unittest
import time
import sys

from datetime import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.log import logger
import os
sys.path.append('D:\\jftest1_CG\\test1')
#
from utils.config import Config
url = Config().get ('QTURL')

class Test_Pclogin(unittest.TestCase):
    def test_pcLogin(self):
        # driver = webdriver.Chrome ()
        fp = webdriver.FirefoxProfile (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\hwtosi65.default")
        driver = webdriver.Firefox (fp)  #启动带插件的firefox
        # driver=webdriver.Firefox()  #启动不带插件的firefox
        driver.maximize_window ()
        # driver.get_cookies()
        # driver.delete_all_cookies()   #清理浏览器缓存
        driver.get(url)
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
        driver.find_element_by_id ('login').send_keys ('14510000051')
        js = "document.getElementById('password').style.display='block'"  # 编写JS语句
        driver.execute_script (js)  # 执行JS
        driver.find_element_by_id ('password').send_keys ('a12345')
        driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").click()
        time.sleep (2)
        t=driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/p").text
        print(t)
        self.assertEqual(t,"总资产")
        # driver.find_element_by_id ("input_tranAmt").send_keys (Keys.CONTROL, 's')  crtr+s 保存
        driver.find_element_by_xpath ("html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/p").send_keys(Keys.CONTROL, Keys.SHIFT,'!')
        time.sleep(5)


        logger.info(t)
        driver.close()

if __name__ == '__main__':
    unittest.main ()

