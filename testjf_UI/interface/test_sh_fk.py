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

    cursor = connection.cursor ()
    # cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
    cursor.execute ("SELECT id from bid_info where name='m年年5203'")
    # 提交SQL
    connection.commit ()
    t = cursor.fetchall ()
    # a=t['tel']

    a= t[0]['id']

    def test_loginht(self):
        content = {'randomCode': '123','rememberMe': '0','login': '18812345678','passwd': 'nuxMWr+r6pPgNFohH7Id/dJXOPPVv9QfSi5Jwk83LTfQqzAp/jWiwFsw0yy45mnxSDv3tPFqjkbmuwPUrQKzyHN+tjYAiUZigBEphPZvyHEhytSoBY3ft1JaNbaOdqws4kc2m1t4t4qumsa1BofMsYZ2JKsXsUXBFipsXd+/K1A='}


        r=requests.post('http://192.168.1.249:8501/management/managementLoginController/login',data=content)  # 发送请求

        print (r.text)  # 获取响应报文
        print (r.status_code)
        print("123")
        c=r.cookies


    # def test_invest(self):   --投标 141  170
        content1={'id':TestInvest.a,'reason':'满标审核通过','state':'4'}

        r1=requests.post('http://192.168.1.249:8501/management/bidInfoController/auditBid',data=content1,cookies=c)  # 发送请求

        # return r.json
        print (r1.text)  # 获取响应报文
        print (r1.status_code)
        print("审核")

# http://192.168.1.249:8501/management/loanController/makeLoans?bidInfoId=302
#         r2 = requests.post ('http://192.168.1.249:8501/management/loanController/makeLoans?bidInfoId=TestInvest.a',cookies=c)  # 发送请求
        a1='http://192.168.1.249:8501/management/loanController/makeLoans?bidInfoId='
        a2=str(TestInvest.a)
        add=a1+a2
        r2 = requests.post (add,cookies=c)
        # return r.json
        print (r1.text)  # 获取响应报文
        print (r1.status_code)
        print ("放款")
if __name__ == "__main__":
    unittest.main ()
