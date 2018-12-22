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
fp = webdriver.FirefoxProfile (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\hwtosi65.default")
driver = webdriver.Firefox (fp)  # 启动带插件的firefox
# driver=webdriver.Firefox()  #启动不带插件的firefox
driver.maximize_window ()
# driver.get_cookies()
driver. get(url)
driver. delete_all_cookies()  # 清理浏览器缓存
driver. get(url)
WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
#保存截图
driver.find_element_by_id ('login').send_keys (Keys.CONTROL,Keys.SHIFT, '!')
time.sleep(3)
t = datetime.now ().strftime ('%Y%m%d%H%M%S')
rule_name = '金服PC白名单登录后的首页' + t
# os.system("D:\\Documents\\jt_lingcunwei.exe")
os.system("D:\\Documents\\jt_lingcunwei.exe"+ " " + rule_name)
# #保存网页
# driver.find_element_by_id ('login').send_keys (Keys.CONTROL,'s')
# t = datetime.now ().strftime ('%Y%m%d%H%M%S')
# rule_name3 = '金服PC充值页面' + t
# # 调用exe保存网页
# # os.system ("D:\\Documents\\auto_lingcunwei2.exe" + " " + rule_name3)
# os.system ("D:\\Documents\\auto_lingcunwei2.exe" + " " + rule_name3)