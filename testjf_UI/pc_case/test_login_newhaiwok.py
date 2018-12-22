#-*- coding:utf-8 -*-
import unittest
import time
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage

class Test_Newyyy (unittest.TestCase):
    excel = DATA_PATH + '/yueyueying.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page = LoginPage ()
                driver=login_page.driver
                # Step3: 输入用户名
                login_page.set_admin ("yradmin")
                # Step4: 输入密码
                login_page.set_password ("a12345")
                time.sleep (6)
                # Step5: 单击登录按钮
                login_page.click_login ()

                login_page.click_jkbgl()
                login_page.click_ckzjkb()
                time.sleep (1)
                driver.switch_to_frame("contentIframe")
                login_page.click_new()
                time.sleep (1)
                login_page.click_bidProduct()
                # 选择产品
                login_page.click_haiw()  #haiw
                # login_page.click_yyydq()  #月月赢到期
                login_page.click_loanuse()
                login_page.click_loanuseli()
                login_page.set_title(d['title'])
                login_page.set_loanBorrowershowname(d['title'])
                login_page.set_bidcode(d['title'])
                login_page.set_totalAmount("2000")
                login_page.set_termValue("6")
                login_page.set_biddlimit("365")
                login_page.set_interestRate("10")
                login_page.set_raiseRate("0")
                login_page.set_shouxufei("0")
                login_page.set_choose()
                WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.XPATH, "//html/body/div/div/div/div[2]/iframe")))
                a = driver.find_element_by_xpath ("//html/body/div/div/div/div[2]/iframe")
                driver.switch_to_frame (a)
                login_page.set_loanuser("祁志国")

                # login_page.set_loanuser("18301306330")
                login_page.click_search()
                time.sleep(3)
                login_page.click_searchok()
                time.sleep(1)
                driver.switch_to_default_content ()
                driver.switch_to_frame ("contentIframe")
                # login_page.click_type()
                # # 正常标、爆款标、推荐标
                # login_page.click_zcbiao()
                time.sleep(1)
                login_page.click_save()
                time.sleep(2)
                al = driver.switch_to_alert ()
                al.accept ()
                # 返回列表上架
                driver.switch_to_default_content ()
                login_page.click_ckzjkb()
                driver.switch_to_frame ("contentIframe")
                login_page.set_mingcheng(d['title'])
                login_page.click_sousuo()

                login_page.click_shangjia()
                time.sleep(1)
                driver.find_element_by_xpath ("//html/body/div/div/div/div[3]/input[1]").click ()
                driver.close()

if __name__ == '__main__':
    unittest.main ()

