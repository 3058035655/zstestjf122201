#-*- coding:utf-8 -*-
import unittest
import time
import sys

from testjf_UI.common.zsjiaxiquanpage import ZsJiaxiquan
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from selenium.webdriver.support.ui import Select
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage

class Test_Zsjiaxiquan (unittest.TestCase):
    excel = DATA_PATH + '/register.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page = ZsJiaxiquan ()
                driver = login_page.driver
                # Step3: 输入用户名
                login_page.set_admin ("yradmin")
                # Step4: 输入密码
                login_page.set_password ("a12345")
                time.sleep (6)
                # Step5: 单击登录按钮
                login_page.click_login ()
                # time.sleep(1)
                login_page.click_zzfw()
                time.sleep(0.5)
                login_page.click_zskq ()
                time.sleep (0.5)
                driver.switch_to_frame ("contentIframe")
                login_page.set_tel (int (d['title']))
                login_page.click_sousuo ()
                login_page.click_choose ()
                time.sleep (0.5)
                login_page.click_ffqk()

                login_page.click_type()
                # jxq=driver.find_element(Select (driver.find_element_by_id ("productType")).select_by_value('0') ).click()
                # driver.find_element_by_id ("productType").find_elements_by_tag_name ("option")[1].click (); #根据父亲节点找 加息券
                # driver.find_element_by_id ("productType").find_elements_by_tag_name ("option")[2].click ();  # 投资红包
                driver.find_element_by_id ("productType").find_elements_by_tag_name ("option")[3].click ();  # 提现券
                # driver.find_element_by_id ("productType").find_elements_by_tag_name ("option")[4].click ();  # 好友券
                login_page.click_sousuo () #点击查询
                login_page.click_choose () #勾选加息券
                login_page.click_pfkq()
                login_page.set_reason("派发卡券原因123")
                login_page.click_tongyi()
                time.sleep(0.5)
                login_page.click_ok()
                login_page.driver.close()

if __name__ == '__main__':
    unittest.main ()

