#-*- coding:utf-8 -*-
import unittest
import time
import sys
sys.path.append('D:\\jftest1_CG\\test1')
from test1.common.loginpage import LoginPage

class Test_Login (unittest.TestCase):

    def test_Login(self):
        # # Step1: 打开登录页
        # BasePage()
        # Step2: 初始化登录Page

        login_page=LoginPage()

        # Step3: 输入用户名
        login_page.set_username ("18812345678")
        # Step4: 输入密码
        login_page.set_password ("a12345")
        # Step5: 单击登录按钮
        login_page.click_login ()
        time.sleep(1)
        # login_page.driver.close()
        login_page.click_jkbgl()
        login_page.click_ckzjkb()
        time.sleep (1)
        login_page.click_new()
        time.sleep (1)
        login_page.click_bidProduct()
        # 选择产品
        login_page.click_Product()
        login_page.click_loanuse()
        login_page.click_loanuseli()
        login_page.set_title("m月月72402")
        login_page.set_bidcode("m月月72402")
        login_page.set_totalAmount("1000000")
        login_page.set_termValue("12")
        login_page.set_interestRate("10")
        login_page.set_raiseRate("0")
        login_page.set_shouxufei("0")
        login_page.click_choose()
        time.sleep(2)
        login_page.set_loanuser("18301306330")
        login_page.click_search()
        login_page.click_searchok()
        time.sleep(1)
        login_page.click_type()
        # 正常标、爆款标、推荐标
        login_page.click_choosetype()
        login_page.click_save()
        time.sleep(1)
        login_page.click_ok()
        time.sleep (1)
        login_page.click_ckzjkb ()
        time.sleep (1)
        login_page.set_mingcheng("m月月72402")
        login_page.click_sousuo()
        time.sleep(1)
        login_page.click_shangjia()
        time.sleep(1)
        login_page.click_shangjiaok()
        time.sleep(1)
        login_page.driver.close()

if __name__ == '__main__':
    unittest.main ()

