import json
import re
import time
import unittest
import paramunittest
import requests
from jkutrl.basepage import BasePage
from jkutrl.common import get_xls

now = time.strftime("%Y_%m_%d %H:%M:%S")
LoanXmllist = get_xls("pcloginCase.xls", "LoanXmllist")
# print(accountRecharge)
b=BasePage()
url1=b.get_url()

@paramunittest.parametrized(*LoanXmllist)
class LoanXmllistTest(unittest.TestCase):
    def setParameters(self, case_name,login,password,totalnum,pagenum,current,startnum,productType,
                      preState,sbiddTermValue,ebiddTermValue,srate,erate,repaymentway,jackerooBidd,biddProperty,sortType,sort):
        self.case_name = str(case_name)
        self.login = str(int(login))
        self.password = str(password)
        self.totalnum=str(int(totalnum))
        self.pagenum=str(int(pagenum))
        self.current=str(int(current))
        self.startnum=str(int(startnum))
        self.productType=str(int(productType))
        self.preState=str(preState)
        self.sbiddTermValue=str(sbiddTermValue)
        self.ebiddTermValue=str(ebiddTermValue)
        self.srate=str(srate)
        self.erate=str(erate)
        self.repaymentway=str(repaymentway)
        self.jackerooBidd=str(jackerooBidd)
        self.biddProperty=str(biddProperty)
        self.sortType=str(sortType)
        self.sort=str(sort)
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
        content2 = {'totalnum': self.totalnum, 'pagenum': self.pagenum,
                    'current': self.current, 'startnum': self.startnum,
                    'productType': self.productType,'preState':self.preState,
                    'sbiddTermValue':self.sbiddTermValue,'ebiddTermValue':self.ebiddTermValue,
                    'srate':self.srate,'erate':self.erate,'repaymentway':self.repaymentway,
                    'jackerooBidd':self.jackerooBidd,'biddProperty':self.biddProperty,
                    'sortType':self.sortType,'sort':self.sort}
        #https://www.hongkunjinfu.com/loanBidFront.do?method=LoanBidlist
        url=url1+'/loanBidFront.do?method=loanXmList'
        #请求月月盈列表
        r2 = requests.post(url,verify=False,data=content2,cookies=c)  # 发送请求
        print ('status:', r2.status_code)
        # resStatus = re.findall (r'<resStatus>(.+?)</resStatus>', t)
        # print(resStatus[0])
        self.assertEqual(r2.status_code, 200)
if __name__ == "__main__":
    unittest.main(verbosity=2)
#https://www.hongkunjinfu.com/loanBidFront.do?method=loanXmList
