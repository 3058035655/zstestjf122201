#-*- coding:utf-8 -*-
import unittest
import time
import sys

import requests
import xlrd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from db import Db
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage

class Test_Newyyy_pctz_shfk (unittest.TestCase):
    excel = DATA_PATH + '/yueyueying.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page = LoginPage ()
                driver = login_page.driver
                amount=10000
                # Step3: 输入用户名
                login_page.set_admin ("yradmin")
                # Step4: 输入密码
                login_page.set_password ("a12345")
                time.sleep (6)
                # Step5: 单击登录按钮
                login_page.click_login ()

                login_page.click_jkbgl ()
                login_page.click_ckzjkb ()
                time.sleep (1)
                driver.switch_to_frame ("contentIframe")
                login_page.click_new ()
                time.sleep (1)
                login_page.click_bidProduct ()
                # 选择产品
                login_page.click_yyyay()  # 月月赢按月
                # login_page.click_nnydq ()  # 年年赢到期
                login_page.click_loanuse ()
                login_page.click_loanuseli ()
                login_page.set_title (d['title'])
                login_page.set_loanBorrowershowname (d['title'])
                login_page.set_bidcode (d['title'])
                login_page.set_totalAmount (amount)
                login_page.set_termValue ("3")
                login_page.set_biddlimit ("365")
                login_page.set_interestRate ("10")
                login_page.set_raiseRate ("0")
                login_page.set_shouxufei ("0")
                login_page.set_choose ()
                WebDriverWait (driver, 10).until (
                    EC.presence_of_element_located ((By.XPATH, "//html/body/div/div/div/div[2]/iframe")))
                a = driver.find_element_by_xpath ("//html/body/div/div/div/div[2]/iframe")
                driver.switch_to_frame (a)
                login_page.set_loanuser ("transfer")

                # login_page.set_loanuser("18301306330")
                login_page.click_search ()
                time.sleep (3)
                login_page.click_searchok ()
                time.sleep (1)
                driver.switch_to_default_content ()
                driver.switch_to_frame ("contentIframe")
                # login_page.click_type()
                # # 正常标、爆款标、推荐标
                # login_page.click_zcbiao()
                time.sleep (1)
                login_page.click_save ()
                time.sleep (2)
                al = driver.switch_to_alert ()
                al.accept ()
                # 返回列表上架
                driver.switch_to_default_content ()
                login_page.click_ckzjkb ()
                driver.switch_to_frame ("contentIframe")
                login_page.set_mingcheng (d['title'])
                login_page.click_sousuo ()

                login_page.click_shangjia ()
                time.sleep (1)
                driver.find_element_by_xpath ("//html/body/div/div/div/div[3]/input[1]").click ()
                # driver.close ()
                connection = Db ().get_connection()
                cursor = Db().get_cursor()
                fname = DATA_PATH + '/yueyueying.xlsx'
                bk = xlrd.open_workbook (fname)
                try:
                    sh = bk.sheet_by_name ("Sheet1")
                except:
                    print
                    "no sheet in %s named Sheet1" % fname

                # 获取第一行第一列数据
                cell_value = sh.cell_value (1, 0)
                print ("表格", cell_value)
                # 通过cursor创建游标

                cursor.execute ("SELECT * from bidd_info where title=%s", (d['title'],))
                # 提交SQL
                connection.commit ()
                t = cursor.fetchall ()
                print(t)
                bidname = t[0]['TITLE']
                print (bidname)
                cursor = con.cursor
                cursor.execute ("SELECT code from bidd_info where  title=%s", (bidname,))
                # 提交SQL
                connection.commit ()
                t = cursor.fetchall ()
                # a=t['tel']
                a = t[0]['code']

                #登录前台投资
                driver.get ('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
                WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
                driver.find_element_by_id ('login').send_keys ('13301307172')
                time.sleep (1)
                e1 = driver.find_element_by_xpath (".//*[@id='txt2']")
                action = ActionChains (driver)
                action.move_to_element (e1).click ().send_keys (
                    "2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc").perform ()

                driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").submit ()

                # address=("http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail&code=ed791706-92f7-4435-b6f6-aa944ed87f4c")
                ad1 = "http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail&code="
                ad2 = a
                add = ad1 + ad2
                driver.get (add)
                time.sleep (1)
                # driver.find_element_by_id ("projectCode").send_keys (d['title'])
                driver.find_element_by_id ("amount").send_keys (amount)   #投资金额
                driver.find_element_by_link_text ("立即投资").click ()
                time.sleep (3)
                driver.find_element_by_class_name ("dialogBtn").click ()

                # 后台登录
                driver.get("http://192.168.1.249:9901/hkjf/loginAdmin.do?method=tologin")
                login_page.set_admin ("yradmin")
                # Step4: 输入密码
                login_page.set_password ("a12345")
                time.sleep (6)
                # Step5: 单击登录按钮
                login_page.click_login ()
                login_page.click_jkbgl ()
                time.sleep(0.5)
                #审核标的
                driver.find_element_by_link_text("待审核的借款标").click()
                driver.switch_to_frame ("contentIframe")
                time.sleep(0.5)
                driver.find_element_by_name("title").send_keys(d['title'])
                driver.find_element_by_link_text("查询").click()
                driver.find_element_by_link_text("审核").click()
                driver.find_element_by_id("content").send_keys("满标审核通过！")
                driver.find_element_by_link_text("通过").click()
                driver.switch_to_default_content ()
                #放款
                driver.find_element_by_xpath(".//*[@id='left']/div/ul/li[7]/div/span[1]").click()
                time.sleep(0.5)
                driver.find_element_by_link_text("待放款的借款标").click()
                driver.switch_to_frame ("contentIframe")
                time.sleep(0.5)
                driver.find_element_by_name("title").send_keys(d['title'])
                driver.find_element_by_link_text('查询').click()
                driver.find_element_by_link_text("放款").click()
                time.sleep(0.8)
                driver.find_element_by_xpath("//html/body/div/div/div/div[3]/input[1]").click()
                driver.close()




if __name__ == '__main__':
    unittest.main ()

