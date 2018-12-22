import unittest

import pymysql

from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode
import requests

import json

class TestInvest(unittest.TestCase):
    connection = pymysql.connect (host='192.168.1.249', port=3307, user='dev_db_user', password='yrSuper001',
                                  db='finance_qa',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    # cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
    cursor.execute ("SELECT code from bidd_info where title='m金月月8901'")
    # 提交SQL
    connection.commit ()
    t = cursor.fetchall ()
    # a=t['tel']

    a= t[0]['code']

    def test_login(self):
        content = {'access_token': 'ed39725a-5f6f-4504-adb2-07f78b9adf04','login': '14510000053',
                   'passwd': 'Sc3O1RqsxkkPacfMvmiUKjyRDo1qMri+kgamx8SaZijqasveCgv+BT6IvNTsFItF7Jy//FwAHJKCI3IqKOA2INpBzJ/JKzsTAxKXufvhH28r5lBLpeWBcuyeVJEaiJ27fkFIAzAM0qBucOIvScLOaoXBmUTS3dVz9Jl+Fbq/p5M='}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                   'Accept-Encoding': 'gzip, deflate',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Referer': 'http://192.168.1.249:8602/financial/index.html',
                   'Content-Length': '215',
                   'Cookie': 'container_flag=container_flag; JSESSIONID=4C9658B8B1E2B04BBD1A5121BDA80EB3;',
                   'submitToken': '"SUBMIT_TOKEN:1f5832f3-3e02-4e8a-b264-fa5ce0eaf011";',
                   'ticket_admin': 'lNNabgYFTOyvXgCvOP1X9YB0B7bnzslM; submitToken_admin="SUBMIT_TOKEN:1f810b88-eb9f-4a88-ade9-50f0a5d64827"; ticket=2617gSHVCRVpSoyGybrt7DZQNEoszqPY',
                   'Connection': 'keep-alive'
                   }
        # http://192.168.1.249:8484/hk-api-services/userController/login
        r = requests.post ('http://192.168.1.249:8484/hk-api-services/userController/login', data=content,
                           headers=headers)  # 发送请求

        print (r.text)  # 获取响应报文
        print (r.status_code)
        print ("登录")
        c = r.cookies
        for key, value in c.items ():
            print (key, '==', value)
        s=c.values()
        print(c.values())


        # session = requests.session()
        # ss=session.get('http://192.168.1.249:9080/api/userController/login')
        # print(ss)


        # def test_invest(self):   --投标 141  170
        content1 = {'access_token': 'ed39725a-5f6f-4504-adb2-07f78b9adf04','bidId': TestInvest.a ,'investWay': '1101', 'money': '200',
                    'sessionId': s, 'sign': '42952b6522bbed5e51aac4e481c588c0', 'sign_type': 'MD5', 'source': '11'}

        # r1 = requests.post ('http://192.168.1.249:9080/api/investController/invest', data=content1,cookies=c)  # 发送请求
        r1 = requests.post ('http://192.168.1.249:8484/hk-api-services/investController/invest', data=content1)  # 发送请求

        # return r.json
        print (r1.text)  # 获取响应报文
        print (r1.status_code)
        print ("1234")
    # # 后台登录
    # def test_loginht(self):
    #     content = {'randomCode': '123', 'rememberMe': '0', 'login': '18812345678',
    #                'passwd': 'Xb4dT7muWJyqt0+TpHahsWrdxIe/BDKa9yxeFoD108q1yaCONHJdFgW7gr3fHmfuWZre8K8aDb4A5qtZWefu+M2QBEGZSRndZhSSOMeqGzkFsxspStSsf1Wv6P9Ppsb/MOKQYSpm2iiFdVTd4UV6CnmV+BCmPGw3URmtalNDvzs='}
    #
    #     r = requests.post ('http://192.168.1.249:8484/hk-management-services/managementLoginController/login',
    #                        data=content)  # 发送请求
    #
    #     print (r.text)  # 获取响应报文
    #     print (r.status_code)
    #     print ("123")
    #     c = r.cookies
    #
    #     # def test_invest(self):   --投标 141  170
    #     content1 = {'id': TestInvest.a, 'reason': '满标审核通过', 'state': '4'}
    #
    #     r1 = requests.post ('http://192.168.1.249:8484/hk-management-services/bidInfoController/auditBid', data=content1,
    #                         cookies=c)  # 发送请求
    #
    #     # return r.json
    #     print (r1.text)  # 获取响应报文
    #     print (r1.status_code)
    #     print ("审核")
    #
    #     # http://192.168.1.249:8501/management/loanController/makeLoans?bidInfoId=302
    #     # http://192.168.1.249:8484/hk-management-services/loanController/makeLoans?bidInfoId=713
    #     a1 = 'http://192.168.1.249:8484/hk-management-services/loanController/makeLoans?bidInfoId='
    #     a2 = str (TestInvest.a)
    #     add = a1 + a2
    #     r2 = requests.post (add, cookies=c)
    #     # return r.json
    #     print (r1.text)  # 获取响应报文
    #     print (r1.status_code)
    #     print ("放款")
    #

if __name__ == "__main__":
    unittest.main ()
