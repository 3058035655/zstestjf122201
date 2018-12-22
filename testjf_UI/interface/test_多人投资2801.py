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

class Test_duoren_invest(unittest.TestCase):
    excel = DATA_PATH + '/register2.xlsx'
    def test_Login(self):
        # excel = DATA_PATH + '/register.xlsx'
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                # db = Db ()
                # connection = db.connection
                # cursor = db.cursor
                # # cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
                # cursor.execute ("SELECT code from bidd_info where title='m季季81602'")
                # connection.commit ()
                # t = cursor.fetchall ()
                # # a=t['tel']
                # code = t[0]['code']
                # print ('标的code:', code)
                tel=int(float(d['title']))
                print('用户：',tel)

                # 用户登录
                # content = {'login':tel,
                #            'password': '2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc',
                #            'pwdLevel': '2', 'verify_code': '请输入计算结果', 'randCode': '请输入您的6位验证码',
                #            'commendPhone': '请输入推荐码(推荐人手机号后8位)',
                #            'loginregister': '请输入您的手机号', 'passwordresgister': '', 'token': '', 'modulus': '',
                #            'exponent': '', 'newToken': '', 'phoneId': '', 'code': '',
                #            'utype': '', 'csrftoken': '', 'pwdLevel': ''}
                # r = requests.post ('http://192.168.1.249:9901/hkjf/login.do?method=indexlogin',
                #                    data=content)  # 发送请求
                # 注册
                content = {'token':'103a7b0f7778435319440ed61de1c327',
                           'newToken': '',
                           'answers': '',
                           'scores': '',
                           'nickName': 'jf',
                           'login': tel,
                           'verify_code': '1',
                           'phoneId': '1158439',
                           'code': '6A9CC1D1CFBC77552DF291E6DD140AB8',
                           'utype': '1',
                           'csrftoken': 'dca40c0e-358b-4453-b013-40e4cb6d5f1b',
                           'randCode': '018256',
                           'password': '2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc',
                           'pwdLevel': '2',
                           'commendPhone': '01307172',
                           }
                r = requests.post ('http://192.168.1.249:9901/hkjf/regist.do?method=userRegist',data=content)  # 发送请求
                # http://192.168.1.249:9901/hkjf/regist.do?method=userRegist
                print ('登录响应状态', r.status_code)
                c = r.cookies



if __name__ == '__main__':
    unittest.main ()

