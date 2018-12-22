import unittest
#相对路径
from utils import HTMLTestRunner
from utils.config import TESTJF_APP_PATH, APP_REPORT


# testcase_path = ".\\testcase"
from utils.mail import Email

testcase_path=TESTJF_APP_PATH
appreport_path = APP_REPORT+"\\appium_report.html"
print(appreport_path)
def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test_*.py")
    for test_suite in discover:
        # print(test_suite)
        for test_case in test_suite:
            uit.addTest(test_case)
            return uit
suite = creat_suite()
fp = open(appreport_path,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试结果",description="appium测试结果")
runner.run(suite)
fp.close()
e = Email (title='appium测试报告',
               message='这是今天的android测试报告，请查收！',
               receiver='hongfeimou@hongkunjinfu.com',
               # server='smtp.qq.com:465',
               server='smtp.mxhichina.com:465',
               sender='hongfeimou@hongkunjinfu.com',
               password='.hongfei123',
               path=appreport_path
               )
e.send ()