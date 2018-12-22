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
applogin_test=get_xls("apploginCase.xls","applogin_test")
b=BasePage()
url1=b.get_url()

@paramunittest.parametrized(*applogin_test)
class AppLoginTest(unittest.TestCase):
    def setParameters(self, case_name,access_token,mobileUDID, login, password,appVersion,mobileModel,mobileVersion	,mobileIp,mobileMAC,passLength,expected):
        self.case_name = str(case_name)
        self.access_token = str (access_token)
        self.mobileUDID = str (mobileUDID)
        self.login = str(int(login))
        self.password = str(password)
        self.appVersion=str(appVersion)
        self.mobileModel=str(mobileModel)
        self.mobileVersion=str(int(mobileVersion))
        self.mobileIp=str(mobileIp)
        self.mobileMAC=str(mobileMAC)
        self.passLength=str(int(passLength))
        self.expected=str(expected)

        # def setUp(self):
        #     self.baseUrl = "http://www.mi.com"
        #     self.driver = webdriver.Chrome()
        #     self.driver.implicitly_wait(10)  # 静默等待10s
    def test_login(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        # 用户登录
        content = {'login': self.login,'password': self.password,
                   'access_token':self.access_token,
                   'mobileUDID':self.mobileUDID,
                   'appVersion':self.appVersion,
                   'mobileModel':self.mobileModel,
                   'mobileVersion':self.mobileVersion	,
                   'mobileIp':self.mobileIp,
                   'mobileMAC':self.mobileMAC,
                   'passLength':self.passLength}
        #https://www.hongkunjinfu.com/login.do?method=indexlogin
        url=url1+'/hkjfapp/user/doLogin'
        r = requests.post (url,verify=False,data=content)  # 发送请求
        # print ('status:', r.status_code)
        t=r.text
        print(t)
        #正则匹配返回结果是否包含excepted字段的值
        resStatus = re.findall (t, self.expected)
        # a=json.loads(t) #字符串转换为字典
        # print(a['state'])
        # print(resStatus[0])
        # self.assertEqual(int(resStatus[0]), 1000)

if __name__ == "__main__":
    unittest.main(verbosity=2)