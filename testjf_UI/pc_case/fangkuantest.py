import unittest
import selenium
from telnetlib import EC
import xlrd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver, selenium
import time

from selenium.webdriver.support.wait import WebDriverWait

from utils.config import DATA_PATH
from utils.file_reader import ExcelReader
import pymysql.cursors
from locale import *


class TestPPy2s1 (unittest.TestCase):
    excel = DATA_PATH + '/investamount.xlsx'
    user = DATA_PATH + '/investuser1.xlsx'
    bidd = DATA_PATH + '/investbidd.xlsx'

    def test_ppy2s1(self):



                driver = webdriver.Chrome ()
                driver.get ("http://192.168.1.249:9901/hkjf/loginAdmin.do?method=tologin")
                driver.find_element_by_xpath (".//*[@id='login']").send_keys ("yradmin")
                driver.find_element_by_xpath (".//*[@id='password']").send_keys ("a12345")
                time.sleep (5)
                # 手动输入验证码
                # driver.find_element_by_xpath (".//*[@id='apLogin']/div[1]/ul/li[3]/p[3]/img").send_keys(text)
                driver.find_element_by_id ("button").submit ()
                # driver.find_element_by_name('verifyCode').clear()
                # driver.find_element_by_xpath (".//*[@id='apLogin']/div[1]/ul/li[3]/p[3]/img").send_keys(text)
                # driver.find_element_by_xpath (".//*[@id='button']").click()


                # # 财务管理-放款
                #
                # driver.find_element_by_xpath (".//*[@id='left']/div/ul/li[7]/div/span[1]").click ()
                # time.sleep (1)
                # driver.find_element_by_link_text ("待放款的借款标").click ()
                # driver.switch_to_frame ("contentIframe")
                # driver.find_element_by_name ("title").send_keys ("m月月盈2018030924")
                # time.sleep (1)
                # driver.find_element_by_link_text ("查询").click ()
                # driver.find_element_by_link_text ("放款").click ()
                # time.sleep (1)
                # driver.find_element_by_xpath ("//html/body/div/div/div/div[3]/input[1]").click ()
                # time.sleep (2)
                # al1 = driver.switch_to_alert ()
                # time.sleep (1)
                # al1.accept()
                # time.sleep (5)
                # driver.switch_to_frame ("contentIframe")
                # # 重新点击菜单 待放款的借款标
                # # driver.switch_to_default_content ()
                # # driver.find_element_by_xpath (".//*[@id='left']/div/ul/li[7]/div/span[1]").click ()
                # # time.sleep (4)
                # # driver.find_element_by_link_text ("待放款的借款标").click ()
                # # # driver.find_element_by_link_text ("待放款的借款标").click ()
                # # driver.switch_to_frame ("contentIframe")
                # driver.find_element_by_name ("title").send_keys ("m月月盈2018030901")
                # time.sleep (2)
                # driver.find_element_by_link_text ("查询").click ()
                # driver.find_element_by_link_text ("放款").click ()
                # time.sleep (2)
                # # a = driver.find_element_by_xpath ("//html/body/div/div/div/div[2]/iframe")
                # driver.find_element_by_xpath ("//html/body/div/div/div/div[3]/input[1]").click ()
                # time.sleep (3)
                # al1 = driver.switch_to_alert ()
                # al1.accept ()
                # time.sleep (2)
                # # 匹配管理
                # driver.switch_to_default_content ()
                # time.sleep (2)

                driver.find_element_by_xpath (".//*[@id='left']/div/ul/li[6]/div/span[1]").click ()
                time.sleep(2)
                driver.find_element_by_link_text ("一个散标匹配多个优选").click ()
                driver.switch_to_frame ("contentIframe")
                driver.find_element_by_name ("title").send_keys ("m散标2018030601")
                driver.find_element_by_link_text ("查询").click ()
                driver.find_element_by_link_text ("匹配").click ()
                driver.find_element_by_link_text ("选择").click ()
                time.sleep(2)
                # 选择优选
                a = driver.find_element_by_xpath ("//html/body/div/div/div/div[2]/iframe")
                driver.switch_to_frame (a)
                driver.find_element_by_name ("title").send_keys ("m月月匹配201803120")
                driver.find_element_by_link_text ("查询").click ()
                time.sleep(2)
                driver.find_element_by_id("types").click()
                time.sleep(1)
                driver.find_element_by_id ("btn_sub").click ()
                time.sleep (2)
                driver.switch_to_frame ("contentIframe")
                time.sleep (2)
                driver.find_element_by_id ("btn_sub").click ()


if __name__ == "__main__":
    unittest.main ()




