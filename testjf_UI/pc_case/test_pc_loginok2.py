#-*- coding:utf-8 -*-
import unittest
import time
import sys
import autoit

from datetime import datetime
import selenium
import win32api

import win32con
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
        driver.get(url)
        driver.delete_all_cookies()   #清理浏览器缓存
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
        # os.path.basename (文件路径)  # 获取文件名
        # os.path.dirname ("")  # 获取目录
        # driver.get_screenshot_as_file("D:/t金服_测试线上/report/shotcut/pc登录后截图.png")
        # pic = ImageGrab.grab()
        # pic.save('D:/t金服_测试/report/shotcut/总资产全屏.jpg')
        # action = ActionChains (driver)
        # action.move_by_offset (0, 0).click ().perform ();
        # action.context_click(on_element=None)# ——点击鼠标右键
        # ActionChains(driver).context_click (on_element=None).send_keys ('K').perform ()  #——谷歌浏览器点击鼠标右键
        # ActionChains (driver).context_click (on_element=None).perform ()  #firefox右键不工作 bug
        # #右键 ctrl+s 保存网页
        # #ctrl+shift+! screengrab网页截图插件
        # driver.find_element_by_xpath ("html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/p").send_keys (Keys.CONTROL, Keys.SHIFT,'!')
        # t = datetime.now ().strftime ('%Y%m%d%H%M%S')
        # rule_name='金服PC白名单登录后的首页'+t
        # #调用exe保存网页
        # # rule_name便是你的动态文件名，可根据上下文获取
        # # os.system ('auto_lingcunwei.exe ' + 'D:\\Documents' + 'jinfu123456' + '.jar')
        # # os.system (r'"D:\\Documents\\auto_lingcunwei.exe"')
        # os.system ("D:\\Documents\\jtlingcunwei.exe")
        # # os.system ("D:\\Documents\\auto_lingcunwei.exe" + " " + rule_name3)
        # 获取浏览器窗口 截取整个网页图片
        autoit.win_activate ('鸿坤金服——社区金融超市 - Mozilla Firefox')
        print ('1111')
        # #再点击一次shift键  释放长按shift 以免后续操作不方便
        # win32api.keybd_event (17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键ctrl
        # win32api.keybd_event (16, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键shift
        # win32api.keybd_event (49, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键1 ！
        autoit.send ('{LCTRL down}'+'{LSHIFT down}'+'{! down}')
        time.sleep (2)
        autoit.win_wait ('截取的图片另存为...')
        autoit.control_focus ("截取的图片另存为...", "1001")
        autoit.win_wait ("[Class:#32770]", 10)
        t = datetime.now ().strftime ("%Y%m%d%H%M%S")
        name ="白名单用户登录后金服首页"+t
        autoit.control_set_text ("截取的图片另存为...", "Edit1", name)

        autoit.control_click ("截取的图片另存为...", "Button1")
        # #再点击一次shift键  释放长按shift 以免后续操作不方便
        win32api.keybd_event (17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键ctrl
        win32api.keybd_event (16, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键shift
        win32api.keybd_event (49, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键1 ！
        logger.info(t)
        driver.close()

if __name__ == '__main__':
    unittest.main ()

