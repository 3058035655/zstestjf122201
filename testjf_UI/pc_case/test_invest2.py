import threading
import unittest
from telnetlib import EC

import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

from utils.config import DATA_PATH


class TestBftz(unittest.TestCase):
    def test_bftz(name):
        content={'login':name,'passwd':'j0kOOiDj+LWhp6rCAxJP5umWe75wQjo/0lQqZnvIQRflkvsaEYOgAC7noCFUk4DIFGUZBXK/IRKZcNHYVGOoQi1loX193tGTRIBj5/L+nrwv1ua72pNx6dD2GXiCGxAKR51PZGUygEKYD+EzS+b0RcKym7EHr/VtEOktfwCX0f8='}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'Accept':'application/json, text/javascript, */*; q=0.01',
                   'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
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
        r=requests.post('http://192.168.1.249:8602/financial/indexController/fasterLogin.do',data=content,headers=headers)  # 发送请求

        print (r.text)  # 获取响应报文
        print (r.status_code)
        print("123")
        c=r.cookies


    # def test_invest(self):   --投标 141  170
        content1={'bidId':'203','money':'100','investRedPacketId':'-999','investRaiseInterestId':'-999'}

        r1=requests.post('http://192.168.1.249:8602/financial/bidInfoController/invest.do',data=content1,cookies=c)  # 发送请求

        # return r.json
        print (r1.text)  # 获取响应报文
        print (r1.status_code)
        print("1234")

    list=['15510000011','15510000012']
    # list=['13301307172','14510000051','14510000052''15510000051','15510000052']
    # list = ['13301307172', '14510000051', '14510000052', '15510000051', '15510000052','15510000053','16900000010','16900000011']
    threads = []
    files = range (len (list))
    # 创建线程
    for i in files:
        t = threading.Thread (target=test_bftz, args=(list[i],))
        threads.append (t)

    if __name__ == '__main__':
        # 启动线程
        for i in files:
            threads[i].start ()
    for i in files:
        threads[i].join ()
        print('end:%s' % time.ctime ())






