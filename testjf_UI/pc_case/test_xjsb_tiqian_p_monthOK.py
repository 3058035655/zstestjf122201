# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import unittest, time, re

from utils.config import DATA_PATH
from utils.file_reader import ExcelReader


class TestNewsanbiaomonth(unittest.TestCase):
    excel = DATA_PATH + '/sanbiao_month.xlsx'
    def test_newsanbiaomonth(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                driver=webdriver.Chrome()
                driver.get("http://192.168.1.249:9901/hkjf/loginAdmin.do?method=tologin")
                driver.find_element_by_xpath (".//*[@id='login']").send_keys ("yradmin")
                driver.find_element_by_xpath (".//*[@id='password']").send_keys ("a12345")
                time.sleep (5)
                # 手动输入验证码
                # driver.find_element_by_xpath (".//*[@id='apLogin']/div[1]/ul/li[3]/p[3]/img").send_keys(text)
                driver.find_element_by_id("button").submit()
                # driver.find_element_by_name('verifyCode').clear()
                #driver.find_element_by_xpath (".//*[@id='apLogin']/div[1]/ul/li[3]/p[3]/img").send_keys(text)
                #driver.find_element_by_xpath (".//*[@id='button']").click()
                driver.find_element_by_xpath(".//*[@id='left']/div/ul/li[5]/div/span[1]").click()
                driver.find_element_by_link_text("筹款中的借款标").click()

                time.sleep(1)
                handles=driver.current_window_handle
                print(handles)
                driver.switch_to_frame("contentIframe")
                driver.find_element_by_link_text("添加").click()

                time.sleep(5)
                driver.find_element_by_id("select1_input").click()
                #月月赢 按月付息 到期还本
                driver.find_element_by_id("li1_input_934981df-2ac6-11e5-9ecc-1051721c3a3e_0").click()
                driver.find_element_by_id("select2_input").click()
                driver.find_element_by_id("li2_input_1").click()
                # title="m爆款标201822802"


                driver.find_element_by_id("loanTitle").send_keys(d['title'])
                driver.find_element_by_id("loanBorrowershowname").send_keys(d['title'])
                driver.find_element_by_id("projectCode").send_keys(d['title'])
                driver.find_element_by_id("amount").send_keys("10000")
                driver.find_element_by_id("termvalue").send_keys("1")
                driver.find_element_by_id("biddlimit").send_keys("365")
                driver.find_element_by_id("rate").send_keys("10")
                driver.find_element_by_id("raiseRate").send_keys("0")
                driver.find_element_by_id("loanrate").send_keys("0")
                driver.find_element_by_id("loanServiceRate").send_keys("0")
                driver.find_element_by_id("select4_input").click()
                # 标的属性
                # driver.find_element_by_id("li4_input_2").click()
                # 是否提前还款
                driver.find_element_by_name("isAdvReturnCap").send_keys(Keys.SPACE)
                # driver.find_element_by_id("returnCapDays").send_keys("0")
                #选择借款人
                # .//*[@id='prodetail']/div[1]/table/tbody/tr[22]/td/span[1]/div[1]/input
                # .//*[@id='prodetail']/div[1]/table/tbody/tr[32]
                # .//*[@id='prodetail']/div[1]/table/tbody/tr[44]/td/input[2]
                driver.find_element_by_xpath(".//*[@id='prodetail']/div[1]/table/tbody/tr[44]/td/input[2]").send_keys(Keys.SPACE)

                # time.sleep(5)
                WebDriverWait (driver, 15).until (EC.presence_of_element_located ((By.XPATH, "//html/body/div/div/div/div[2]/iframe")))
                # a=driver.find_elements_by_xpath(".//*[@id='d86zjCDbir']/div[1]/div[2]/iframe")
                # a=driver.find_element_by_xpath("//html/body/div[2]/div[1]/div[1]/div[2]")
                a=driver.find_element_by_xpath("//html/body/div/div/div/div[2]/iframe")
                driver.switch_to_frame(a)
                # driver.switch_to_frame(a)
                #dr.find_element_by_xpath(".//*[@id='d86zjCDbir']/div[1]/div[2]/iframe")
                # driver.find_element_by_xpath("//form[@id='queryForm']/ul/li/span/input").send_keys("123")T
                driver.find_element_by_xpath(".//*[@id='loginName']").send_keys("颜祖佑")
                driver.find_element_by_link_text("查询").click()
                time.sleep(3)
                driver.find_element_by_link_text("选择").click()
                time.sleep(1)
                driver.switch_to_default_content()
                driver.switch_to_frame("contentIframe")
                driver.find_element_by_link_text("保存").submit()
                time.sleep(2)
                al=driver.switch_to_alert()
                al.accept()
                # 返回列表上架
                driver.switch_to_default_content()
                driver.find_element_by_link_text("筹款中的借款标").click()
                driver.switch_to_frame("contentIframe")
                driver.find_element_by_name("title").send_keys(d['title'])
                driver.find_element_by_link_text("查询").click()

                # driver.find_element_by_link_text("上架").click()
                # time.sleep(1)
                # #     # i=driver.find_element_by_class_name("___boxDialog").find_elements_by_tag_name("input")
                # #
                # #     # driver.find_element(i[0]).click()
                # #     # a=driver.find_element_by_xpath("//html/body/div/div/div/div[2]/iframe") ???
                # #
                # driver.find_element_by_xpath("//html/body/div/div/div/div[3]/input[1]").click()



if __name__ == "__main__":
    unittest.main ()

