import json
import re
import time
import unittest
import paramunittest
import requests
from jkutrl.basepage import BasePage
from jkutrl.common import get_xls

# proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
pcloginCase=get_xls("pcloginCase.xls","pclogin_test")
b=BasePage()
url1=b.get_url()

@paramunittest.parametrized(*pcloginCase)
class PcLoginTest(unittest.TestCase):
    def setParameters(self, case_name, login, password,expected):
        self.case_name = str(case_name)
        self.login = str(int(login))
        self.password = str(password)
        self.expected=str(expected)
        # def setUp(self):
        #     self.baseUrl = "http://www.mi.com"
        #     self.driver = webdriver.Chrome()
        #     self.driver.implicitly_wait(10)  # 静默等待10s
    def test_login(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        # 用户登录
        content = {'login': self.login,'password': self.password}
        #https://www.hongkunjinfu.com/login.do?method=indexlogin
        url=url1+'/login.do?method=indexlogin'
        r = requests.post (url,verify=False,data=content)  # 发送请求
        print ('status:', r.status_code)
        t=r.text
        print(t)
        # a=json.loads(t) #字符串转换为字典
        # print(a['state'])
        self.assertEqual(t,self.expected)
        # resStatus = re.findall (r'<resStatus>(.+?)</resStatus>', t)
        # print(resStatus[0])
        # self.assertEqual(int(resStatus[0]), 1000)

if __name__ == "__main__":
    unittest.main(verbosity=2)