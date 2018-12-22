#-*- coding:utf-8 -*-
import unittest
import time
import sys
# import win32api
# import win32con
# import autoit
# from autoit import autoit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from utils.config import DATA_PATH, REPORT_PATH
# from utils.file_reader import ExcelReader
# from utils.log import logger
# from datetime import datetime
# import os
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage
# from PIL import ImageGrab
from utils.config import Config
url = Config().get ('QTURL')

class Test_PcIndexPage(unittest.TestCase):
    def test_getindexpage(self):
        # driver = webdriver.Chrome ()
        fp = webdriver.FirefoxProfile (r"C:\Users\mhf\AppData\Roaming\Mozilla\Firefox\Profiles\cv6txwo2.default")
        driver = webdriver.Firefox (fp)  # 启动带插件的firefox
        # driver=webdriver.Firefox() #启动不带插件的firefox
        driver.maximize_window ()
        driver.get (url)
        driver.delete_all_cookies()
        driver.get(url)
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
        sy=driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[1]/a").text
        smjj=driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[2]/a").text
        hydl=driver.find_element_by_xpath(".//*[@id='logindiv']/div/h1").text
        self.assertEqual(sy,"首页")
        self.assertEqual(smjj,"私募基金")
        self.assertEqual(hydl,"欢迎登录")
        driver.quit()
        # pic = ImageGrab.grab()
        # pic.save('D:/t金服_测试/report/shotcut/金服PC首页.jpg')
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/未登录时pc首页1.png")
        # # logger.info(t)
        # t=driver.find_element_by_xpath("html/body/div[4]/ul/li[1]/div/h3")#精英团队
        # t1=driver.find_element_by_xpath("html/body/div[4]/ul/li[1]/div/div/img")#精英团队图片
        # driver.execute_script("arguments[0].scrollIntoView();", t1)  #滚动到指定元素位置
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/未登录时pc首页2.png")
        # # 右键 ctrl+s 保存网页
        # driver.find_element_by_xpath ("html/body/div[4]/ul/li[1]/div/div/img").send_keys (Keys.CONTROL,'s')
        # t = datetime.now ().strftime ('%Y%m%d%H%M%S')
        # rule_name = '金服PC未登录时的首页' + t
        # # 调用exe保存网页
        # # rule_name便是你的动态文件名，可根据上下文获取
        # # os.system ('auto_lingcunwei.exe ' + 'D:\\Documents' + 'jinfu123456' + '.jar')
        # # os.system (r'"D:\\Documents\\auto_lingcunwei.exe"')
        # os.system ("D:\\Documents\\auto_lingcunwei.exe" + " " + rule_name)
        #         # 获取浏览器窗口 截取整个网页图片
        #         autoit.win_activate ('鸿坤金服——社区金融超市 - Mozilla Firefox')
        #         print ('1111')
        #         autoit.send ('{LCTRL down}' + '{LSHIFT down}' + '{! down}')
        #         # autoit.send(’{LCTRL down}’ + ‘{LALT down}’ + ‘{a down}’)
        #         # driver.find_element_by_id(‘login’).send_keys(Keys.CONTROL + Keys.SHIFT + ‘!’)
        #         time.sleep (2)
        #         autoit.win_wait ('截取的图片另存为...')
        #         autoit.control_focus ("截取的图片另存为...", "1001")
        #         autoit.win_wait ("[Class:#32770]", 10)
        #         t = datetime.now ().strftime ("%Y%m%d%H%M%S")
        #         name = "未登录时的金服首页" + t
        #         autoit.control_set_text ("截取的图片另存为...", "Edit1", name)
        #         autoit.control_click ("截取的图片另存为...", "Button1")
        #         # # 再点击一次shift键  释放长按shift 以免后续操作不方便
        # autoit.send ('{LCTRL}' + '{LSHIFT}')
        # win32api.keybd_event (17, 0, 0, 0)# ctrl键位码是17
        # win32api.keybd_event (86, 0, 0, 0)# v键位码是86
        # win32api.keybd_event (17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键ctrl
        # win32api.keybd_event (16, 0, win32con.KEYEVENTF_KEYUP, 0) # 释放按键shift
        # win32api.keybd_event (49, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键1 ！
        #         driver.close()
        #         win32api.keybd_event (17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键ctrl
        #         win32api.keybd_event (16, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键shift
        #         win32api.keybd_event (49, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键1 ！
        #         autoit.send ('{LCTRL up}')
        #         autoit.send ('{LSHIFT up}')
        #         autoit.send ('{! up}')
if __name__ == '__main__':
    unittest.main ()

