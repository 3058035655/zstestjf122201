#-*- coding:utf-8 -*-
import unittest
import time
import sys
import re
import requests

from db import Db
from testjf_UI.common.loginpage import LoginPage
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Test_duoren_invest(unittest.TestCase):
    excel = DATA_PATH + '/register.xlsx'
    def test_Login(self):
        # excel = DATA_PATH + '/register.xlsx'
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                db = Db ()
                connection = db.connection
                cursor = db.cursor
                # cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
                cursor.execute ("SELECT code from bidd_info where title='月月9438'")
                connection.commit ()
                t = cursor.fetchall ()
                # a=t['tel']
                code = t[0]['code']
                print ('标的code:', code)
                tel=int(float(d['title']))
                print('用户：',tel)

                # 用户登录
                content = {'login':tel,
                           'password': '8b08c0bd2c536072a4bed2ddebcc4f01a73549106e04d12659aed56cf938d6b72f3a53149b488e4a309f2fe9851d8d3ad60a429cbe4e82dd16cfb1206dc7c7752ddf861a79374247777d76d3188061738b196fddd53e3f0ae1044c525fa9f35de6cfa0ce69dd2f2e30e4211acfd8a4d806d9c22bb5130aa68eceda6cc78c9630',
                           'pwdLevel': '2', 'verify_code': '请输入计算结果', 'randCode': '请输入您的6位验证码',
                           'commendPhone': '请输入推荐码(推荐人手机号后8位)',
                           'loginregister': '请输入您的手机号', 'passwordresgister': '', 'token': '', 'modulus': '',
                           'exponent': '', 'newToken': '', 'phoneId': '', 'code': '',
                           'utype': '', 'csrftoken': '', 'pwdLevel': ''}
                r = requests.post ('http://192.168.1.249:9901/hkjf/login.do?method=indexlogin',
                                   data=content)  # 发送请求
                print ('登录响应状态', r.status_code)
                print(r.text)
                c = r.cookies
                # 请求标的详情
                content_xq = {'code':code, 'tempType': '2'}
                rxq = requests.get ("http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail",
                                    params=content_xq, cookies=c)
                txt = rxq.text
                r = re.findall (r'<input name="token"  type="hidden"  value="(.+?)"/>', txt)
                # print("token的值是：",r)
                print ('详情响应code:', rxq.status_code)
                # 用户投资
                contenttz = {'code':code, 'token': r, 'couponDetailCodeK': '', 'couponDetailCodeJ': '',
                             'confirmAmount': '1000', 'useAbleMoney': ''}
                rtz = requests.post ('http://192.168.1.249:9901/hkjf/investController.do?method=goodsOpenInvest',
                                     data=contenttz, cookies=c)  # 发送请求
                print ('投资响应状态', rtz.status_code)

if __name__ == '__main__':
    unittest.main ()

