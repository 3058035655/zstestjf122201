#-*- coding:utf-8 -*-
import datetime
import unittest
import time
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from testjf_UI.common.fredpackgepage import PfRedpackage
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage

class Test_Pf_pclqredpackage (unittest.TestCase):
    excel = DATA_PATH + '/register_sm.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page = PfRedpackage ()
                driver = login_page.driver
                # Step3: 输入用户名
                login_page.set_admin ("yradmin")
                # Step4: 输入密码
                login_page.set_password ("a12345")
                time.sleep (10)
                # Step5: 单击登录按钮
                login_page.click_login ()
                # time.sleep(1)
                login_page.click_hbgl ()
                time.sleep (0.5)
                login_page.click_pfhb ()
                time.sleep (0.5)
                driver.switch_to_frame ("contentIframe")
                login_page.set_tel (int (d['login']))
                login_page.click_sousuo()
                login_page.click_choose()
                login_page.click_pfhbl()
                time.sleep(0.5)
                login_page.set_value("10000")
                a = datetime.datetime.now ()
                b = str(a + datetime.timedelta(days=365))
                login_page.set_enddate(b)    #2018-07-28 14:52:04
                login_page.set_packetSendReason("测试")
                login_page.click_queding()
                time.sleep(1)
                #红包审核
                driver.switch_to_default_content ()
                login_page.click_cwgl()
                time.sleep(0.5)
                login_page.click_hbsh()
                time.sleep(0.5)
                driver.switch_to_frame ("contentIframe")
                login_page.set_dhuser(int(d['login']))
                login_page.click_sousuo()
                time.sleep(0.5)
                hbbm = driver.find_element_by_xpath ("html/body/div/div[2]/div[2]/div/table/tbody/tr/td[3]").text  # 红包编码
                print (hbbm)
                login_page.click_quanxuan()
                time.sleep(0.5)
                login_page.click_plsh ()
                time.sleep(0.5)
                login_page.set_shreason("派发红包审核通过")
                login_page.click_tongyi()

                # 登录前台领取红包
                driver.get ('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
                WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
                driver.find_element_by_id ('login').send_keys (int (d['login']))
                time.sleep (1)
                e1 = driver.find_element_by_xpath (".//*[@id='txt2']")
                action = ActionChains (driver)
                # action.move_to_element (e1).click ().send_keys (
                #     "2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc").perform ()
                # driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").submit()  #submit的结果是1
                #http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage
                action.move_to_element (e1).click ().send_keys("a12345").perform ()
                driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").click ()
                driver.find_element_by_link_text("我的账号").click()
                driver.find_element_by_xpath("html/body/div[4]/div/div[2]/div[2]/ul/li[7]/div/span[1]").click()
                driver.find_element_by_link_text("红包兑换").click()
                time.sleep(0.5)
                driver.find_element_by_id("redpageKey").send_keys(hbbm)#红包编码
                driver.find_element_by_link_text("兑换").click()
                time.sleep(0.5)
                driver.close()


if __name__ == '__main__':
    unittest.main ()

