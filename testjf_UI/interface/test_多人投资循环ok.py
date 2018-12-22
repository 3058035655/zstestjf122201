#-*- coding:utf-8 -*-
import unittest
import time
import sys

import re
import requests
from testjf_UI.common.db import Db
from testjf_UI.common.loginpage import LoginPage
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import csv

def test_Login():
    excel = DATA_PATH + '/test.csv'
    with open(excel, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for col in reader:
            print(col)
            db = Db ()
            connection = db.connection
            cursor = db.cursor
            # cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
            cursor.execute ("SELECT code from bidd_info where title='m季季81602'")
            connection.commit ()
            t = cursor.fetchall ()
            # a=t['tel']
            code = t[0]['code']
            print ('标的code:', code)
            tel=col
            print('用户：',tel)

            # 用户登录
            content = {'login':tel,
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
            content_xq = {'code':code, 'tempType': '2'}
            rxq = requests.get ("http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail",
                                params=content_xq, cookies=c)
            txt = rxq.text
            r = re.findall (r'<input name="token"  type="hidden"  value="(.+?)"/>', txt)
            # print("token的值是：",r)
            print ('详情响应code:', rxq.status_code)
            # 用户投资
            contenttz = {'code':code, 'token': r, 'couponDetailCodeK': '', 'couponDetailCodeJ': '',
                         'confirmAmount': '1000', 'useAbleMoney': '1000'}
            rtz = requests.post ('http://192.168.1.249:9901/hkjf/investController.do?method=goodsOpenInvest',
                                 data=contenttz, cookies=c)  # 发送请求
            # print (r1.text)  # 获取响应报文
            print ('投资响应状态', rtz.status_code)

n=5
while n>0:
    test_Login ()
    n=n-1

