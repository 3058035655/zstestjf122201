import json
import re
import time
import unittest
import paramunittest
import requests
from jkutrl.basepage import BasePage
from jkutrl.common import get_xls

now = time.strftime("%Y_%m_%d %H:%M:%S")
queryCardbinBf = get_xls("pcChongzhiCase.xls", "queryCardbinBf")
# print(accountRecharge)
b=BasePage()
url1=b.get_url()
@paramunittest.parametrized(*queryCardbinBf)
class queryCardbinBfTest(unittest.TestCase):
    def setParameters(self, case_name,login,password,card_no):
        self.case_name = str(case_name)
        self.login = str(int(login))
        self.password = str(password)
        self.card_no=str(int(card_no))
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
        # https://www.hongkunjinfu.com/financeController.do?method=queryCardbinBf&operate=query_card_bin&card_no=6228481200290317812
        url2=url1+'/financeController.do?method=queryCardbinBf&operate=query_card_bin&card_no='+self.card_no
        r2 = requests.get(url2,verify=False,cookies=c)  # 发送请求
        print ('status:', r2.status_code)
        # resStatus = re.findall (r'<resStatus>(.+?)</resStatus>', t)
        # print(resStatus[0])
        self.assertEqual(r2.status_code, 200)
if __name__ == "__main__":
    unittest.main(verbosity=2)
# https://www.hongkunjinfu.com/financeController.do?method=queryCardbinBf&operate=query_card_bin&card_no=6228481200290317812