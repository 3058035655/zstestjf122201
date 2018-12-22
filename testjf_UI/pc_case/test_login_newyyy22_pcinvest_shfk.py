#-*- coding:utf-8 -*-
import unittest
import time
import sys
from selenium.webdriver.support import expected_conditions as EC

import requests
import xlrd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from testjf_UI.common import db
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage

class Test_Newyyy22 (unittest.TestCase):
    excel = DATA_PATH + '/yueyueying.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                # login_page = LoginPage ()
                # driver = login_page.driver
                # # Step3: 输入用户名
                # login_page.set_admin ("yradmin")
                # # Step4: 输入密码
                # login_page.set_password ("a12345")
                # time.sleep (6)
                # # Step5: 单击登录按钮
                # login_page.click_login ()
                #
                # login_page.click_jkbgl ()
                # login_page.click_ckzjkb ()
                # time.sleep (1)
                # driver.switch_to_frame ("contentIframe")
                # login_page.click_new ()
                # time.sleep (1)
                # login_page.click_bidProduct ()
                # # 选择产品
                # login_page.click_yyyay()  # 月月赢按月
                # # login_page.click_nnydq ()  # 年年赢到期
                # login_page.click_loanuse ()
                # login_page.click_loanuseli ()
                # login_page.set_title (d['title'])
                # login_page.set_loanBorrowershowname (d['title'])
                # login_page.set_bidcode (d['title'])
                # login_page.set_totalAmount ("10000")
                # login_page.set_termValue ("3")
                # login_page.set_biddlimit ("365")
                # login_page.set_interestRate ("10")
                # login_page.set_raiseRate ("0")
                # login_page.set_shouxufei ("0")
                # login_page.set_choose ()
                # WebDriverWait (driver, 10).until (
                #     EC.presence_of_element_located ((By.XPATH, "//html/body/div/div/div/div[2]/iframe")))
                # a = driver.find_element_by_xpath ("//html/body/div/div/div/div[2]/iframe")
                # driver.switch_to_frame (a)
                # login_page.set_loanuser ("transfer")
                #
                # # login_page.set_loanuser("18301306330")
                # login_page.click_search ()
                # time.sleep (3)
                # login_page.click_searchok ()
                # time.sleep (1)
                # driver.switch_to_default_content ()
                # driver.switch_to_frame ("contentIframe")
                # # login_page.click_type()
                # # # 正常标、爆款标、推荐标
                # # login_page.click_zcbiao()
                # time.sleep (1)
                # login_page.click_save ()
                # time.sleep (2)
                # al = driver.switch_to_alert ()
                # al.accept ()
                # # 返回列表上架
                # driver.switch_to_default_content ()
                # login_page.click_ckzjkb ()
                # driver.switch_to_frame ("contentIframe")
                # login_page.set_mingcheng (d['title'])
                # login_page.click_sousuo ()
                #
                # login_page.click_shangjia ()
                # time.sleep (1)
                # driver.find_element_by_xpath ("//html/body/div/div/div/div[3]/input[1]").click ()
                # driver.close ()

                con = db.Db ()
                connection = con.connection
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
                cursor = con.cursor
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
                content = {'login': '13301307172',
                           'password': '2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc',
                           'pwdLevel':'2', 'verify_code':'请输入计算结果', 'randCode':'请输入您的6位验证码', 'commendPhone': '请输入推荐码(推荐人手机号后8位)', 'loginregister': '请输入您的手机号',
                           'passwordresgister': '', 'token': '', 'modulus': '', 'exponent': '', 'newToken':'', 'phoneId':'', 'code':'', 'utype': '', 'csrftoken': '', 'pwdLevel': ''
                           }
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                           'Accept': 'application/json, text/javascript, */*; q=0.01',
                           'Accept-Language': 'zh-CN,zh;q=0.8',
                           'Accept-Encoding': 'gzip, deflate',
                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                           'X-Requested-With': 'XMLHttpRequest',
                           'Referer': 'http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage',
                           'Content-Length': '790',
                           'Cookie': 'JSESSIONID=28A99DF26761AE4A207F7994150A75B8;',
                           'submitToken': '"c4761b51-96b6-4c67-a20b-264c5a29060c";',
                           'ticket': 'qS6lHfYKgE2kSDA7PY8rRA9e6hvQCzs4',
                           'Connection': 'keep-alive'
                           }
                # r = requests.post ('http://192.168.1.249:9901/hkjf/login.do?method=indexlogin',data=content, headers=headers)  # 发送请求
                r = requests.post ('http://192.168.1.249:9901/hkjf/login.do?method=indexlogin',data=content)  # 发送请求

                print (r.text)  # 获取响应报文
                print (r.status_code)
                print ("登录")
                c = r.cookies
                print("c:",c)

                ##--投标 141  170
                # content_tz= {'code': a, 'token': '', 'couponDetailCodeK': '','couponDetailCodeJ':'','confirmAmount':'2000',
                #             'useAbleMoney': ''}
                #
                # # r1 = requests.post ('http://192.168.1.249:8584/hk-financial-services/bidInfoController/invest.do',data=content1,cookies=c)  # 发送请求
                # r_tz=requests.post('http://192.168.1.249:9901/hkjf/investController.do?method=goodsOpenInvest',data=content_tz,cookies=c)
                # # return r.json
                # # print (r_tz.text)  # 获取响应报文
                # print (r_tz.status_code)
                # print ("投资")

                # # 后台登录
                #
                #
                # conten2 = {'randomCode': '123', 'rememberMe': '0', 'login': '88812345678',
                #            'passwd': 'H/SOSDPHotw0L2qVobGWQkipJ7HWEkabs5Q63qU8PW8NvPy5HYNwMZuu2bG03VxixQczvSQRaWlEDror33LOflH7DJUPRiwD/1iYB1w1qsBN0z/1KwargVhtGw/SMDUd9yTotjfG4NbiGH9yiiba8t1hHVVVCCJbv6PvEn1bBYs='}
                #
                # r2 = requests.post ('http://192.168.1.249:8584/hk-management-services/managementLoginController/login',
                #                     data=conten2)  # 发送请求
                #
                # print (r2.text)  # 获取响应报文
                # print (r2.status_code)
                # print ("123")
                # c2 = r2.cookies
                #
                # # def test_invest(self):   --投标 141  170
                # content3 = {'id': a, 'reason': '满标审核通过', 'state': '4'}
                # # http://192.168.1.249:8584/hk-management-services/bidInfoController/auditBid
                # r3 = requests.post ('http://192.168.1.249:8584/hk-management-services/bidInfoController/auditBid',
                #                     data=content3,
                #                     cookies=c2)  # 发送请求
                #
                # # return r.json
                # print (r3.text)  # 获取响应报文
                # print (r3.status_code)
                # print ("审核")
                #
                # # http://192.168.1.249:8501/management/loanController/makeLoans?bidInfoId=302
                # # http://192.168.1.249:8584/hk-management-services/bidInfoController/auditBid
                # a1 = 'http://192.168.1.249:8584/hk-management-services/loanController/makeLoans?bidInfoId='
                # a2 = str (a)
                # add = a1 + a2
                # r4 = requests.post (add, cookies=c2)
                # # return r.json
                # print (r4.text)  # 获取响应报文
                # print (r4.status_code)
                # print ("放款")



if __name__ == '__main__':
    unittest.main ()

