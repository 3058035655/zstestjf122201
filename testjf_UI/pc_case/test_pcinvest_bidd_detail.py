#-*- coding:utf-8 -*-
import unittest
import time
from datetime import datetime
import sys
import autoit
import win32api

import win32con
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.log import logger
import os
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage
# from PIL import ImageGrab
from utils.config import Config
url = Config().get ('QTURL')

class Test_PcInvet_bidd_detail(unittest.TestCase):
    def test_pcinvet_bidd_detail(self):
        # driver = webdriver.Chrome ()
        fp = webdriver.FirefoxProfile (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\hwtosi65.default")
        driver = webdriver.Firefox (fp)  # 启动带插件的firefox
        # driver=webdriver.Firefox() # 启动不带插件的firefox
        driver.maximize_window ()
        driver.get(url)
        driver.delete_all_cookies()
        driver.get (url)
        # driver.get_cookies()
        driver.delete_all_cookies()
        driver.get (url)
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
        driver.find_element_by_id ('login').send_keys ('14510000051')
        js = "document.getElementById('password').style.display='block'"  # 编写JS语句
        driver.execute_script (js)  # 执行JS
        driver.find_element_by_id ('password').send_keys ('a12345')
        driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").click ()
        time.sleep (2)
        # pic = ImageGrab.grab()
        # pic.save('D:/t金服_测试/report/shotcut/总资产全屏.jpg')
        #判断白名单用户能看到定期投资、安全保障、关于我们
        driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[2]/a").click() #定期投资
        time.sleep(2.5)
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/pc定期投资列表页.png")
        yyy=driver.find_element_by_xpath(".//*[@id='selone']/li[3]").text
        self.assertEqual("月月盈",yyy)
        # gywm=driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[8]/a").text

        # 获取浏览器窗口 截取整个网页图片 月月赢列表页
        autoit.win_activate ('定期投资 - 鸿坤金服 - Mozilla Firefox')
        print ('1111')
        autoit.send ('{LCTRL down}' + '{LSHIFT down}' + '{! down}')
        # autoit.send(’{LCTRL down}’ + ‘{LALT down}’ + ‘{a down}’)
        # driver.find_element_by_id(‘login’).send_keys(Keys.CONTROL + Keys.SHIFT + ‘!’)
        time.sleep (2)
        autoit.win_wait ('截取的图片另存为...')
        autoit.control_focus ("截取的图片另存为...", "1001")
        autoit.win_wait ("[Class:#32770]", 10)
        t = datetime.now ().strftime ("%Y%m%d%H%M%S")
        name = "金服PC定期投资列表页" + t
        autoit.control_set_text ("截取的图片另存为...", "Edit1", name)
        autoit.control_click ("截取的图片另存为...", "Button1")
        driver.find_element_by_xpath (".//*[@id='selone']/li[3]").click ()  # 月月盈
        time.sleep (2)
        text = driver.find_element_by_xpath ("html/body/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]").text  # 月月赢的标题
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/pc定期投资列表页.png")
        # 获取浏览器窗口 截取整个网页图片 定期投资月月表页
        autoit.win_activate ('定期投资 - 鸿坤金服 - Mozilla Firefox')
        print ('1111')
        autoit.send ('{LCTRL down}' + '{LSHIFT down}' + '{! down}')
        # autoit.send(’{LCTRL down}’ + ‘{LALT down}’ + ‘{a down}’)
        # driver.find_element_by_id(‘login’).send_keys(Keys.CONTROL + Keys.SHIFT + ‘!’)
        time.sleep (2)
        autoit.win_wait ('截取的图片另存为...')
        autoit.control_focus ("截取的图片另存为...", "1001")
        autoit.win_wait ("[Class:#32770]", 10)
        t = datetime.now ().strftime ("%Y%m%d%H%M%S")
        name = "金服PC定期投资月月盈列表页" + t
        autoit.control_set_text ("截取的图片另存为...", "Edit1", name)
        autoit.control_click ("截取的图片另存为...", "Button1")
        # bidd1=driver.find_element_by_xpath("html/body/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]")
        # driver.execute_script ("arguments[0].scrollIntoView();", bidd1)  # 向下滑动页面，捕捉立即投资按钮
        # time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='yxxm0']/a").click()   #立即投资
        time.sleep(1)
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/pc投资标的详情页.png")
        tzze=driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[1]/ul/li[1]/p").text #投资总额
        jhjs=driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[1]/ul/li[1]").text  #计划介绍
        self.assertEqual("投资总额",tzze)
        self.assertEqual("计划介绍",jhjs)

        autoit.win_activate (text+' - 鸿坤金服 - Mozilla Firefox')
        print ('1111')
        autoit.send ('{LCTRL down}' + '{LSHIFT down}' + '{! down}')
        # autoit.send(’{LCTRL down}’ + ‘{LALT down}’ + ‘{a down}’)
        # driver.find_element_by_id(‘login’).send_keys(Keys.CONTROL + Keys.SHIFT + ‘!’)
        time.sleep (2)
        autoit.win_wait ('截取的图片另存为...')
        autoit.control_focus ("截取的图片另存为...", "1001")
        autoit.win_wait ("[Class:#32770]", 10)
        t = datetime.now ().strftime ("%Y%m%d%H%M%S")
        name = "pc投资标的详情页" + t
        autoit.control_set_text ("截取的图片另存为...", "Edit1", name)
        autoit.control_click ("截取的图片另存为...", "Button1")
        # # 再点击一次shift键  释放长按shift 以免后续操作不方便
        # win32api.keybd_event (17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键ctrl
        # win32api.keybd_event (16, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键shift
        driver.close()
        win32api.keybd_event (17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键ctrl
        win32api.keybd_event (16, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键shift
        win32api.keybd_event (49, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键1 ！
        autoit.send ('{LCTRL up}')
        autoit.send ('{LSHIFT up}')
        autoit.send ('{! up}')

if __name__ == '__main__':
    unittest.main ()

