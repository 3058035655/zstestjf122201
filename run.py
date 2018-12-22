import unittest
# import win32api
# import win32con
from testjf_UI.pc_case.test_pcGeIndexPage import Test_PcIndexPage
from testjf_UI.pc_case.test_pc_loginok import Test_Pclogin
# from testjf_UI.pc_case.test_pc_putforward import Test_Pc_Putforward
# from testjf_UI.pc_case.test_pc_recharge import Test_Pc_Recharge
# from testjf_UI.pc_case.test_pcblacklist_sy import Test_PcBlacklistSy
# from testjf_UI.pc_case.test_pcinvest_bidd_detail import Test_PcInvet_bidd_detail
# from testjf_UI.pc_case.test_pcwhitelist_sy import Test_PcWhitelistSy
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH

if __name__=='__main__':
    suite=unittest.TestSuite()
    # 直接用addTest方法添加单个TestCase  test_pcLogin
    suite.addTest(Test_PcIndexPage("test_getindexpage"))  #打开pc首页
    suite.addTest(Test_Pclogin("test_pcLogin"))   #登录
    # suite.addTest (Test_PcWhitelistSy ("test_whitelistsy")) #白名单登录查看首页
    # suite.addTest(Test_PcBlacklistSy("test_blacklistsy"))  #黑名单登录查看首页
    # suite.addTest(Test_PcInvet_bidd_detail("test_pcinvet_bidd_detail")) #投资查看标的详情页
    # suite.addTest(Test_Pc_Recharge("test_pcrecharge"))  #打开充值页面
    # suite.addTest (Test_Pc_Putforward ("test_pc_putforward"))  #打开提现页面
    # runner = unittest.TextTestRunner (verbosity=2)
    # runner.run (suite)

    if __name__ == '__main__':
        report = REPORT_PATH + '\\report.html'
        print (report)
        with open (report, 'wb') as f:
            runner = HTMLTestRunner (f, verbosity=2, title='hkjf测试报告', description='修改html报告')
            runner.run (suite)
            e = Email (title='hkjf测试报告',
                       message='这是今天的测试报告，请查收！',
                       receiver='hongfeimou@hongkunjinfu.com',
                       # server='smtp.qq.com:465',
                       server='smtp.mxhichina.com:465',
                       sender='hongfeimou@hongkunjinfu.com',
                       password='.hongfei123',
                       path=report
                       )
            e.send ()
        print("hello123456")


