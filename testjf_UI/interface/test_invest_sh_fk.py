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
    cursor.execute ("SELECT id from bid_info where name='季等额92001'")
    # 提交SQL
    connection.commit ()
    t = cursor.fetchall ()
    # a=t['tel']

    a= t[0]['id']

    def test_login(self):
        content = {'login': '15510000011',
                   'passwd': 'j0kOOiDj+LWhp6rCAxJP5umWe75wQjo/0lQqZnvIQRflkvsaEYOgAC7noCFUk4DIFGUZBXK/IRKZcNHYVGOoQi1loX193tGTRIBj5/L+nrwv1ua72pNx6dD2GXiCGxAKR51PZGUygEKYD+EzS+b0RcKym7EHr/VtEOktfwCX0f8='}
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
        r = requests.post ('http://192.168.1.249:8602/financial/indexController/fasterLogin.do', data=content,
                           headers=headers)  # 发送请求

        print (r.text)  # 获取响应报文
        print (r.status_code)
        print ("123")
        c = r.cookies

        # def test_invest(self):   --投标 141  170
        content1 = {'bidId': TestInvest.a ,'money': '10000', 'investRedPacketId': '-999', 'investRaiseInterestId': '-999'}

        r1 = requests.post ('http://192.168.1.249:8602/financial/bidInfoController/invest.do', data=content1,
                            cookies=c)  # 发送请求

        # return r.json
        print (r1.text)  # 获取响应报文
        print (r1.status_code)
        print ("1234")

    def test_loginht(self):
        content = {'randomCode': '123', 'rememberMe': '0', 'login': '18812345678',
                   'passwd': 'nuxMWr+r6pPgNFohH7Id/dJXOPPVv9QfSi5Jwk83LTfQqzAp/jWiwFsw0yy45mnxSDv3tPFqjkbmuwPUrQKzyHN+tjYAiUZigBEphPZvyHEhytSoBY3ft1JaNbaOdqws4kc2m1t4t4qumsa1BofMsYZ2JKsXsUXBFipsXd+/K1A='}

        r = requests.post ('http://192.168.1.249:8501/management/managementLoginController/login',
                           data=content)  # 发送请求

        print (r.text)  # 获取响应报文
        print (r.status_code)
        print ("123")
        c = r.cookies

        # def test_invest(self):   --投标 141  170
        content1 = {'id': TestInvest.a, 'reason': '满标审核通过', 'state': '4'}

        r1 = requests.post ('http://192.168.1.249:8501/management/bidInfoController/auditBid', data=content1,
                            cookies=c)  # 发送请求

        # return r.json
        print (r1.text)  # 获取响应报文
        print (r1.status_code)
        print ("审核")

        # http://192.168.1.249:8501/management/loanController/makeLoans?bidInfoId=302

        a1 = 'http://192.168.1.249:8501/management/loanController/makeLoans?bidInfoId='
        a2 = str (TestInvest.a)
        add = a1 + a2
        r2 = requests.post (add, cookies=c)
        # return r.json
        print (r1.text)  # 获取响应报文
        print (r1.status_code)
        print ("放款")


if __name__ == "__main__":
    unittest.main ()
