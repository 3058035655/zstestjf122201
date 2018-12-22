#-*- coding:utf-8 -*-
import re
import unittest
import time
import sys
import requests
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from testjf_UI.common.db import Db
from testjf_UI.common.tiyanjinglpage2 import TiyanjinPage
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')



class Test_Newyyy (unittest.TestCase):
    excel = DATA_PATH + '/体验金_体验标.xlsx'

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
        db = Db ()
        connection = db.connection
        cursor = db.cursor
        for d in datas:
            with self.subTest (data=d):
                # 获取用户code
                cursor.execute ("SELECT code from loginuser where tel=%s", (d['tel']))
                connection.commit ()
                t = cursor.fetchall ()
                # a=t['tel']
                usercode = t[0]['code']
                print ('用户code:', usercode)
                cursor.execute ("SELECT * from fn_sim_account where STATUS=0 and USER_CODE=%s", usercode)
                connection.commit ()
                t = cursor.fetchall ()
                l = len (t)
                if l == 0:
                    pass
                else:
                    # DELETE  from fn_sim_account where USER_CODE=
                    cursor.execute ("DELETE  from fn_sim_account where USER_CODE=%s", usercode)
                    connection.commit ()
                login_page.click_tyjgl()
                login_page.click_tyjff()
                time.sleep (1)
                driver.switch_to_frame("contentIframe")
                login_page.set_tel(int(d['tel']))
                login_page.click_sousuo()
                login_page.click_choose()
                #   发放体验金
                login_page.click_fftyj()
                login_page.set_money("10000")    #金额
                login_page.click_qrff()
                driver.switch_to_default_content()
                #新建体验标
                login_page.click_jkbgl ()
                login_page.click_ckzjkb ()
                time.sleep (1)
                driver.switch_to_frame ("contentIframe")
                login_page.click_new ()
                time.sleep (1)
                login_page.click_bidProduct ()
                # 选择产品
                login_page.click_tyb ()  # 体验标

                login_page.click_loanuse ()
                login_page.click_loanuseli ()
                login_page.set_title (d['bidd'])
                login_page.set_loanBorrowershowname (d['bidd'])
                login_page.set_bidcode (d['bidd'])
                login_page.set_totalAmount ("10000")
                login_page.set_termValue ("12")
                login_page.set_biddlimit ("365")
                login_page.set_interestRate ("10")
                login_page.set_raiseRate ("0")
                login_page.set_shouxufei ("0")
                login_page.click_type ()
                # 是否是新手标
                # driver.find_element_by_xpath (".//*[@id='prodetail']/div[1]/table/tbody/tr[22]/td/span[1]/div[1]/input").send_keys (Keys.SPACE)
                # 选择借款人
                login_page.set_choose ()
                WebDriverWait (driver, 10).until (
                    EC.presence_of_element_located ((By.XPATH, "//html/body/div/div/div/div[2]/iframe")))
                a = driver.find_element_by_xpath ("//html/body/div/div/div/div[2]/iframe")
                driver.switch_to_frame (a)
                login_page.set_loanuser ("张效伟")

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
                login_page.set_mingcheng (d['bidd'])
                login_page.click_sousuo2 ()

                login_page.click_shangjia ()
                time.sleep (1)
                driver.find_element_by_xpath ("//html/body/div/div/div/div[3]/input[1]").click ()

                #用户投资
                #  cursor.execute ("SELECT code FROM bidd_info where title=%s", (cell_value,))
                cursor.execute ("SELECT code from bidd_info where title=%s",(d['bidd']))
                connection.commit ()
                t = cursor.fetchall ()
                # a=t['tel']
                code = t[0]['code']
                print ('标的code:', code)
                tel = int (float (d['tel']))
                print ('用户：', tel)
                #SELECT * from fn_sim_account where USER_CODE=(SELECT code from loginuser where tel='13010000012')and STATUS=0;
                #获取用户code
                cursor.execute ("SELECT code from loginuser where tel=%s", (d['tel']))
                connection.commit ()
                t = cursor.fetchall ()
                # a=t['tel']
                usercode = t[0]['code']
                print ('用户code:', usercode)

                # 用户登录
                content = {'login': tel,
                           'password': '2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc',
                           'pwdLevel': '2', 'verify_code': '请输入计算结果', 'randCode': '请输入您的6位验证码',
                           'commendPhone': '请输入推荐码(推荐人手机号后8位)',
                           'loginregister': '请输入您的手机号', 'passwordresgister': '', 'token': '', 'modulus': '',
                           'exponent': '', 'newToken': '', 'phoneId': '', 'code': '',
                           'utype': '', 'csrftoken': '', 'pwdLevel': ''}
                r = requests.post ('http://192.168.1.249:9901/hkjf/login.do?method=indexlogin',
                                   data=content)  # 发送请求
                print ('登录响应状态', r.status_code)
                c = r.cookies
                # 请求标的详情
                content_xq = {'code': code, 'tempType': '2'}
                rxq = requests.get ("http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail",
                                    params=content_xq, cookies=c)
                txt = rxq.text
                r = re.findall (r'<input name="token"  type="hidden"  value="(.+?)"/>', txt)
                # print("token的值是：",r)
                print ('详情响应code:', rxq.status_code)
                # 用户投资
                contenttz = {'code': code, 'token': r, 'couponDetailCodeK': '', 'couponDetailCodeJ': '',
                             'confirmAmount': '10000', 'useAbleMoney': '10000'}
                rtz = requests.post ('http://192.168.1.249:9901/hkjf/investController.do?method=goodsOpenInvest',
                                     data=contenttz, cookies=c)  # 发送请求
                # print (r1.text)  # 获取响应报文
                print ('投资响应状态', rtz.status_code)
                # #后台满标审核
                driver.switch_to_default_content()
                driver.find_element_by_xpath(".//*[@id='left']/div/ul/li[5]/div/span[1]").click()
                driver.find_element_by_link_text("待审核的借款标").click()
                driver.switch_to_frame ("contentIframe")
                time.sleep(1)
                driver.find_element_by_name("title").send_keys(d['bidd'])
                driver.find_element_by_link_text("查询").click()
                time.sleep(1)
                driver.find_element_by_link_text("审核").click()
                driver.find_element_by_id("content").send_keys("ok")
                driver.find_element_by_link_text("通过").click()
                #放款
                driver.switch_to_default_content ()
                time.sleep(1)
                driver.find_element_by_xpath(".//*[@id='left']/div/ul/li[7]/div/span[1]").click()
                time.sleep(0.5)
                driver.find_element_by_link_text("待放款的借款标").click()
                driver.switch_to_frame("contentIframe")
                time.sleep (1)
                driver.find_element_by_name("title").send_keys(d['bidd'])
                driver.find_element_by_link_text("查询").click()
                time.sleep(1)
                driver.find_element_by_link_text("放款").click()
                driver.find_element_by_xpath ("//html/body/div/div/div/div[3]/input[1]").click ()
        driver.close()
if __name__ == '__main__':
    unittest.main ()

