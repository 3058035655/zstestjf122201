#-*- coding:utf-8 -*-
import unittest
import time
import sys
from datetime import datetime

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
import autoit
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage
# from PIL import ImageGrab
from utils.config import Config
url = Config().get ('QTURL')

class Test_PcBlacklistSy(unittest.TestCase):
    def test_blacklistsy(self):
        # driver = webdriver.Chrome ()
        fp = webdriver.FirefoxProfile (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\hwtosi65.default")
        driver = webdriver.Firefox (fp)  #启动带插件的firefox
        # driver=webdriver.Firefox()
        driver.maximize_window ()
        driver.get(url)
        driver.delete_all_cookies()
        driver.get (url)
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
        driver.find_element_by_id ('login').send_keys ('13301307172')
        js = "document.getElementById('password').style.display='block'"  # 编写JS语句
        driver.execute_script (js)  # 执行JS
        driver.find_element_by_id ('password').send_keys ('a12345')
        driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").click ()
        time.sleep (2)
        # pic = ImageGrab.grab()
        # pic.save('D:/t金服_测试/report/shotcut/总资产全屏.jpg')
        #判断黑名单用户，只能看到私募基金、海外基金
        sy = driver.find_element_by_xpath ("html/body/div[2]/div[2]/div/ul/li[1]/a").text
        smjj=driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[2]/a").text
        hwjj=driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[3]/a").text
        self.assertEqual (sy, "首页")
        self.assertEqual(smjj,"私募基金")
        self.assertEqual(hwjj,"海外基金")
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/pc黑名单用户查看首页1.png")
        # # logger.info(t)html/body/div[4]/ul/li[1]/div/h3
        # t=driver.find_element_by_xpath("html/body/div[4]/ul/li[1]/div/h3")#精英团队
        # # t1=driver.find_element_by_xpath("html/body/div[4]/ul/li[1]/div/div/img")#精英团队图片
        # driver.execute_script("arguments[0].scrollIntoView();", t)  #滚动到指定元素位置
        # time.sleep(1)
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/pc黑名单用户查看首页2.png")
        # t3=driver.find_element_by_xpath("html/body/div[7]/div[2]/div[2]/a")#信托产品
        # driver.execute_script("arguments[0].scrollIntoView();", t3)  # 滚动到指定元素位置
        # time.sleep(1)
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/pc黑名单用户查看首页3.png")
        # # 保存首页网页
        # driver.find_element_by_xpath ("html/body/div[7]/div[2]/div[2]/a").send_keys (
        #     Keys.CONTROL, 's')
        # t = datetime.now ().strftime ('%Y%m%d%H%M%S')
        # rule_name1 = '金服PC黑名单登录后首页' + t
        # # 调用exe保存网页
        # os.system ("D:\\Documents\\auto_lingcunwei.exe" + " " + rule_name1)
        # time.sleep (2)
        # # #鼠标点击一下空白处，收回下载弹出框
        # # action = ActionChains(driver)
        # # action.move_by_offset(0,0).click().perform ();  # 点击空白区域：坐标（0，0）
        # 获取浏览器窗口 截取整个网页图片
        autoit.win_activate ('鸿坤金服——社区金融超市 - Mozilla Firefox')
        print ('1111')
        autoit.send ('{LCTRL down}' + '{LSHIFT down}' + '{! down}')
        # autoit.send(’{LCTRL down}’ + ‘{LALT down}’ + ‘{a down}’)
        # driver.find_element_by_id(‘login’).send_keys(Keys.CONTROL + Keys.SHIFT + ‘!’)
        time.sleep (2)
        autoit.win_wait ('截取的图片另存为...')
        autoit.control_focus ("截取的图片另存为...", "1001")
        autoit.win_wait ("[Class:#32770]", 10)
        t = datetime.now ().strftime ("%Y%m%d%H%M%S")
        name = "pc黑名单用户登录查看首页" + t
        autoit.control_set_text ("截取的图片另存为...", "Edit1", name)
        autoit.control_click ("截取的图片另存为...", "Button1")

        #我的账号
        driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[6]/a").click()
        time.sleep(1)
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/pc黑名单用户我的账户1.png")
        # #向下滑动页面
        # shouye=driver.find_element_by_xpath("html/body/div[3]/div[2]/div/ul/li[1]/a")
        # driver.execute_script ("arguments[0].scrollIntoView();", shouye)  # 滚动到指定元素位置
        # time.sleep(1)
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/pc黑名单用户我的账户2.png")
        # # 右键 ctrl+s 保存网页
        # driver.find_element_by_xpath ("html/body/div[3]/div[2]/div/ul/li[1]/a").send_keys (
        #     Keys.CONTROL, 's')
        # t = datetime.now ().strftime ('%Y%m%d%H%M%S')
        # rule_name = '金服PC黑名单登录后我的账户页面' + t
        # # 调用exe保存网页
        # # rule_name便是你的动态文件名，可根据上下文获取
        # # os.system ('auto_lingcunwei.exe ' + 'D:\\Documents' + 'jinfu123456' + '.jar')
        # # os.system (r'"D:\\Documents\\auto_lingcunwei.exe"')
        # os.system ("D:\\Documents\\auto_lingcunwei.exe" + " " + rule_name)

        # 获取浏览器窗口 截取整个网页图片
        autoit.win_activate ('会员中心 - 鸿坤金服 - Mozilla Firefox')
        print ('1111')
        autoit.send ('{LCTRL down}' + '{LSHIFT down}' + '{! down}')
        # autoit.send(’{LCTRL down}’ + ‘{LALT down}’ + ‘{a down}’)
        # driver.find_element_by_id(‘login’).send_keys(Keys.CONTROL + Keys.SHIFT + ‘!’)
        time.sleep (2)
        autoit.win_wait ('截取的图片另存为...')
        autoit.control_focus ("截取的图片另存为...", "1001")
        autoit.win_wait ("[Class:#32770]", 10)
        t = datetime.now ().strftime ("%Y%m%d%H%M%S")
        name = "金服PC黑名单登录后我的账户页面" + t
        autoit.control_set_text ("截取的图片另存为...", "Edit1", name)
        autoit.control_click ("截取的图片另存为...", "Button1")
        # # 再点击一次shift键  释放长按shift 以免后续操作不方便
        # # autoit.send ('{LCTRL}' + '{LSHIFT}')
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

