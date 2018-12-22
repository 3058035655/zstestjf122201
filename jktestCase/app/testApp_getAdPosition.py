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
getAdPosition=get_xls("apploginCase.xls","getAdPosition")
b=BasePage()
url1=b.get_url()

@paramunittest.parametrized(*getAdPosition)
class AppgetAdPositionTest(unittest.TestCase):
    def setParameters(self, case_name,access_token,type,function):
        self.case_name = str(case_name)
        self.access_token = str (access_token)
        self.type=str(int(type))
        self.function=str(int(function))

    def test_login(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        # 用户登录
        content = {'access_token':self.access_token,
                   'type':self.type,
                   'function':self.function}
        #https://www.hongkunjinfu.com/login.do?method=indexlogin
        url=url1+'/hkjfapp/banner/getAdPosition'
        r = requests.get (url,verify=False,data=content)  # 发送请求
        print ('status:', r.status_code)
        t=r.text
        print(t)
        #正则匹配返回结果是否包含excepted字段的值
        # resStatus = re.findall (t, self.expected)
        # a=json.loads(t) #字符串转换为字典
        # print(a['state'])
        # print(resStatus[0])
        # self.assertEqual(int(resStatus[0]), 1000)

if __name__ == "__main__":
    unittest.main(verbosity=2)