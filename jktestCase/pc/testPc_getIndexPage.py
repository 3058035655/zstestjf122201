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


class PcgetIndexPageTest(unittest.TestCase):
    def test_login(self):
        self.case_name='pcgetIndexPageTest'
        self._testMethodDoc = self.case_name  # 设置用例名称
        # https://www.hongkunjinfu.com/index.do?method=getIndexPage
        url=url1+'/index.do?method=getIndexPage'
        #请求首页
        r = requests.get (url,verify=False)  # 发送请求
        print ('status:', r.status_code)
        self.assertEqual (r.status_code, 200)
        # a=json.loads(t) #字符串转换为字典
        # print(a['state'])
        # self.assertEqual(t,self.expected)
        # resStatus = re.findall (r'<resStatus>(.+?)</resStatus>', t)
        # print(resStatus[0])
        # self.assertEqual(int(resStatus[0]), 1000)

if __name__ == "__main__":
    unittest.main(verbosity=2)
# https://www.hongkunjinfu.com/index.do?method=getIndexPage
