import json
import re
import time
import unittest
import paramunittest
import requests
from jkutrl.basepage import BasePage
from jkutrl.common import get_xls

now = time.strftime("%Y_%m_%d %H:%M:%S")
userinmoney = get_xls("pcChongzhiCase.xls", "userinmoney")
# print(accountRecharge)
b=BasePage()
url1=b.get_url()
@paramunittest.parametrized(*userinmoney)
class userinmoneyTest(unittest.TestCase):
    def setParameters(self, case_name,login,password,input_tranAmt,card_no,bank_code,payType,tranAmt):
        self.case_name = str(case_name)
        self.login = str(int(login))
        self.password = str(password)
        self.input_tranAmt=str(input_tranAmt)
        self.card_no=str(int(card_no))
        self.bank_code=str(int(bank_code))
        self.payType=str(payType)
        self.tranAmt=str(tranAmt)
    def test_login(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        # 用户登录
        content = {'login': self.login,'password': self.password}
        #https://www.hongkunjinfu.com/login.do?method=indexlogin
        url=url1+'/login.do?method=indexlogin'
        r = requests.post (url,verify=False,data=content)  # 发送请求
        print ('status:', r.status_code)
        t=r.text
        c=r.cookies
        # https: // www.hongkunjinfu.com / safeCenterFinanceFront.do?method = touserinmoney
        content2 = {'input_tranAmt': self.input_tranAmt, 'card_no': self.card_no
            , 'bank_code': self.bank_code
            , 'payType': self.payType
            , 'tranAmt': self.tranAmt
            , 'card_no': self.card_no}
        url2=url1+'/safeCenterFinanceFront.do?method=touserinmoney'
        r2 = requests.post(url2,verify=False,data=content2,cookies=c)  # 发送请求
        print ('status:', r2.status_code)
        # resStatus = re.findall (r'<resStatus>(.+?)</resStatus>', t)
        # print(resStatus[0])
        self.assertEqual(r2.status_code, 200)
if __name__ == "__main__":
    unittest.main(verbosity=2)
# https://www.hongkunjinfu.com/safeCenterFinanceFront.do?method=touserinmoney
# https://www.hongkunjinfu.com/safeCenterFinanceFront.do?method=userinmoney