#-*- coding:utf-8 -*-
import unittest
import time
from datetime  import datetime
import sys
import win32api
import win32con
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, ui
import autoit
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.log import logger
import os
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage
# from PIL import ImageGrab
from utils.config import Config
url = Config().get ('QTURL')
#Putforward   提现
class Test_Pc_Recharge(unittest.TestCase):
    def test_pcrecharge(self):
        # driver = webdriver.Chrome ()
        fp = webdriver.FirefoxProfile (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\hwtosi65.default")
        driver = webdriver.Firefox (fp)  # 启动带插件的firefox
        # driver=webdriver.Firefox() # 启动不带插件的firefox
        driver.maximize_window ()
        driver.get (url)
        # driver.get_cookies()
        driver.delete_all_cookies ()
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
        # 我的账号
        driver.find_element_by_xpath ("html/body/div[2]/div[2]/div/ul/li[9]/a").click ()  #我的账号
        time.sleep(1.5)
        driver.find_element_by_xpath(".//*[@id='right']/div/div[1]/div/div[2]/div[2]/a[1]").click()#点击充值
        time.sleep(1)
        driver.find_element_by_id("input_card_no").send_keys("6228481200290317812")
        # driver.get_screenshot_as_file ("D:/t金服_测试线上/report/shotcut/pc充值.png")
        # #点击空白处
        # action = ActionChains (driver)
        # action.move_by_offset(0, 0).click ().perform ()
        #点击展开更多
        driver.find_element_by_xpath(".//*[@id='PaymentFS']/div[2]/div[1]/div[2]/div[1]/div/img").click()
        amount=1
        driver.find_element_by_id("input_tranAmt").send_keys(amount)
        # # 获取浏览器窗口 截取整个网页图片 充值
        # autoit.win_activate ('会员中心 - 鸿坤金服 - Mozilla Firefox')
        # print ('1111')
        # autoit.send ('{LCTRL down}' + '{LSHIFT down}' + '{! down}')
        # # autoit.send(’{LCTRL down}’ + ‘{LALT down}’ + ‘{a down}’)
        # # driver.find_element_by_id(‘login’).send_keys(Keys.CONTROL + Keys.SHIFT + ‘!’)
        # time.sleep (2)
        # autoit.win_wait ('截取的图片另存为...')
        # autoit.control_focus ("截取的图片另存为...", "1001")
        # autoit.win_wait ("[Class:#32770]", 10)
        # t = datetime.now ().strftime ("%Y%m%d%H%M%S")
        # name = "金服pc充值页" + t
        # autoit.control_set_text ("截取的图片另存为...", "Edit1", name)
        # autoit.control_click ("截取的图片另存为...", "Button1")
        # # 再点击一次shift键  释放长按shift 以免后续操作不方便
        # autoit.send ('{LCTRL}' + '{LSHIFT}')
        #点击去充值
        driver.find_element_by_id("rechargeForm_btn").click()
        time.sleep(1)
        #跳转到收银台
        num2 = driver.window_handles  # 获取当前页句柄
        print (num2)
        driver.switch_to.window (num2[1])  # 在句柄2 上执行下述步骤
        time.sleep(5)
        print(driver.find_element_by_xpath ("html/body/div[2]/div[1]/div/div[1]/div[2]/span/i").text)  # 充值金额0.01
        # wait = ui.WebDriverWait (driver, 10)
        # wait.until (lambda driver: driver.find_element_by_xpath("html/body/div[2]/div[1]/div/div[1]/div[1]/div[1]"))
        ymje = driver.find_element_by_xpath ("html/body/div[2]/div[1]/div/div[1]/div[2]/span/i").text  # 充值金额0.01
        yhk=driver.find_element_by_xpath("html/body/div[2]/div[1]/div/div[2]/div[2]/div[1]").text   #银行卡
        ckr=driver.find_element_by_xpath("html/body/div[2]/div[1]/div/div[2]/div[3]/div[1]").text   #持卡人
        hkjf=driver.find_element_by_xpath("html/body/div[2]/div[1]/div/div[1]/div[1]/div[1]").text  #鸿坤金服
        self.assertEqual(amount,int(float(ymje)))
        self.assertEqual("银行卡",yhk)
        self.assertEqual("持卡人",ckr)
        self.assertEqual("鸿坤金服",hkjf)
        #
        # 获取浏览器窗口 截取整个网页图片
        # 收银台
        autoit.win_activate ('PC认证支付尊享版 - Mozilla Firefox')
        print ('1111')
        # autoit.send ('{LCTRL down}' + '{LSHIFT down}' + '{! down}') #新打开的窗口没有带上插件的快捷键
        # autoit.send ('{LCTRL down}' + '{LSHIFT down}' + '{76 down}') #使用网页截图功能 ctrl+shift+L
        # 快捷键ctrl+shift+L
        win32api.keybd_event (17, 0, 0, 0)  # ctrl
        win32api.keybd_event (16, 0, 0, 0)  # shift
        win32api.keybd_event(76,0,0,0) #L
        print('222')
        # autoit.send(’{LCTRL down}’ + ‘{LALT down}’ + ‘{a down}’)
        # driver.find_element_by_id(‘login’).send_keys(Keys.CONTROL + Keys.SHIFT + ‘!’)
        time.sleep (2)
        #ctrl + s保存截图
        win32api.keybd_event (17, 0, 0, 0)  # ctrl
        win32api.keybd_event (83, 0, 0, 0)  # S
        print('333')
        # autoit.win_wait ('截取的图片另存为...')
        # autoit.control_focus ("截取的图片另存为...", "1001")
        # autoit.win_wait ("[Class:#32770]", 10)
        # t = datetime.now ().strftime ("%Y%m%d%H%M%S")
        # name = "金服pc收银台页" + t
        # autoit.control_set_text ("截取的图片另存为...", "Edit1", name)
        # autoit.control_click ("截取的图片另存为...", "Button1")
        # # # 再点击一次shift键  释放长按shift 以免后续操作不方便
        # # win32api.keybd_event (17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键ctrl
        # # win32api.keybd_event (16, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键shift
        # # win32api.keybd_event (49, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键1 ！

        driver.close()
        win32api.keybd_event (17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键ctrl
        win32api.keybd_event (16, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键shift
        win32api.keybd_event (49, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键1 ！
        autoit.send ('{LCTRL up}')
        autoit.send ('{LSHIFT up}')
        autoit.send ('{! up}')
if __name__ == '__main__':
    unittest.main ()


