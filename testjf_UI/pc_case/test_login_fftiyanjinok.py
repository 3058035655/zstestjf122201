#-*- coding:utf-8 -*-
import unittest
import time
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from testjf_UI.common.tiyanjinglpage import TiyanjinPage
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage

class Test_Newyyy (unittest.TestCase):
    excel = DATA_PATH + '/register.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        login_page = TiyanjinPage ()
        driver = login_page.driver
        # Step3: 输入用户名
        login_page.set_admin ("yradmin")
        # Step4: 输入密码
        login_page.set_password ("a12345")
        time.sleep (6)
        # Step5: 单击登录按钮
        login_page.click_login ()
        for d in datas:
            with self.subTest (data=d):
                # login_page = TiyanjinPage ()
                # driver=login_page.driver
                # # Step3: 输入用户名
                # login_page.set_admin ("yradmin")
                # # Step4: 输入密码
                # login_page.set_password ("a12345")
                # time.sleep (6)
                # # Step5: 单击登录按钮
                # login_page.click_login ()

                login_page.click_tyjgl()
                login_page.click_tyjff()
                time.sleep (1)
                driver.switch_to_frame("contentIframe")
                login_page.set_tel(int(d['title']))
                login_page.click_sousuo()
                login_page.click_choose()
                #   发放体验金
                login_page.click_fftyj()
                login_page.set_money("10000")    #金额
                login_page.click_qrff()
                driver.switch_to_default_content()
        driver.close()


if __name__ == '__main__':
    unittest.main ()

