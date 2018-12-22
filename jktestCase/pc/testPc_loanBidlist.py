import json
import re
import time
import unittest
import paramunittest
import requests
from jkutrl.basepage import BasePage
from jkutrl.common import get_xls

now = time.strftime("%Y_%m_%d %H:%M:%S")
LoanBidlist = get_xls("pcloginCase.xls", "LoanBidlist")
# print(accountRecharge)
b=BasePage()
url1=b.get_url()

@paramunittest.parametrized(*LoanBidlist)
class LoanBidlistTest(unittest.TestCase):
    def setParameters(self, case_name,login,password):
        self.case_name = str(case_name)
        self.login = str(int(login))
        self.password = str(password)
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
        #https://www.hongkunjinfu.com/loanBidFront.do?method=LoanBidlist
        url=url1+'/loanBidFront.do?method=LoanBidlist'
        r2 = requests.get(url,verify=False,cookies=c)  # 发送请求
        print ('status:', r2.status_code)
        # resStatus = re.findall (r'<resStatus>(.+?)</resStatus>', t)
        # print(resStatus[0])
        self.assertEqual(r2.status_code, 200)
if __name__ == "__main__":
    unittest.main(verbosity=2)
#https://www.hongkunjinfu.com/loanBidFront.do?method=loanXmList