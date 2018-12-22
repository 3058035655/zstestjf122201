#-*- coding:utf-8 -*-
import unittest
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, ui
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.log import logger
from datetime import datetime
import os
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage
# from PIL import ImageGrab
from utils.config import Config
url = Config().get ('QTURL')
#Putforward   提现
class Test_Pc_Putforward(unittest.TestCase):
    def test_pc_putforward(self):
        driver = webdriver.Chrome ()
        # driver=webdriver.Firefox()
        driver.maximize_window ()
        driver.get (url)
        driver.delete_all_cookies()
        driver.get(url)
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
        driver.find_element_by_id ('login').send_keys ('14510000051')
        js = "document.getElementById('password').style.display='block'"  # 编写JS语句
        driver.execute_script (js)  # 执行JS
        driver.find_element_by_id ('password').send_keys ('a12345')
        driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").click ()
        time.sleep (2)
        # pic = ImageGrab.grab()
        # pic.save('D:/t金服_测试/report/shotcut/总资产全屏.jpg')
        # 我的账号
        driver.find_element_by_xpath ("html/body/div[2]/div[2]/div/ul/li[9]/a").click ()  #我的账号
        time.sleep(1)
        # # 右键 ctrl+s 保存网页
        # driver.find_element_by_xpath ("html/body/div[2]/div[2]/div/ul/li[9]/a").send_keys (Keys.CONTROL, 's')
        # t = datetime.now ().strftime ('%Y%m%d%H%M%S')
        # rule_name = '金服PC未登录时的首页' + t
        # # 调用exe保存网页
        # # rule_name便是你的动态文件名，可根据上下文获取
        # # os.system ('auto_lingcunwei.exe ' + 'D:\\Documents' + 'jinfu123456' + '.jar')
        # # os.system (r'"D:\\Documents\\auto_lingcunwei.exe"')
        # os.system ("D:\\Documents\\auto_lingcunwei.exe" + " " + rule_name)
        driver.find_element_by_link_text("提现").click()
        time.sleep(1)
        num2 = driver.window_handles  # 获取当前页句柄
        print (num2)
        # wait = ui.WebDriverWait (driver, 10)
        # wait.until (lambda driver: driver.find_element_by_xpath("html/body/div[2]/div[1]/div/div[1]/div[1]/div[1]"))
        driver.find_element_by_id ("tranAmt").send_keys ("0.01")
        tx = driver.find_element_by_xpath (".//*[@id='useroutmoney']/div/div[2]/ul/li[1]/span[1]").text  # 提现金额
        self.assertEqual("提现金额：",tx)
        driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/pc提现.png")
        driver.close()

if __name__ == '__main__':
    unittest.main ()

