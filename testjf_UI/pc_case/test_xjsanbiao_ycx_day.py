# coding=utf-8
import selenium
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


class TestNewyyy(unittest.TestCase):
    excel = DATA_PATH + '/sanbiao_ycx_day.xlsx'
    def test_newyyy(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest(data=d):
                driver=selenium.webdriver.Chrome()
                driver.get("http://192.168.1.249:8501/management/login.html")
                driver.find_element_by_id("login").send_keys("18812345678")
                driver.find_element_by_id("password").send_keys("a12345")
                driver.find_element_by_id("submit").click()
                time.sleep (1)
                driver.find_element_by_xpath (".//*[@id='side-menu']/li[2]/a/span[1]").click ()
                driver.find_element_by_xpath (".//*[@id='side-menu']/li[2]/ul[1]/li/a/span").click ()
                time.sleep (1)
                driver.find_element_by_link_text("添加").click()
                time.sleep(1)
                driver.find_element_by_name("bidProductId").click()
                # 选择产品  散标 一次性
                driver.find_element_by_xpath(".//*[@id='bidForm']/div/div/div[1]/select/option[10]").click()
                driver.find_element_by_name ("loanUse").click ()
                driver.find_element_by_xpath(".//*[@id='bidForm']/div/div/div[2]/select/option[2]").click()
                driver.find_element_by_name("title").send_keys(d['title'])
                driver.find_element_by_name("bidCode").send_keys(d['title'])
                # 金额
                driver.find_element_by_name("totalAmount").send_keys("10000")
                # 几个月
                driver.find_element_by_name("termValue").send_keys("12")

                # 年利率
                driver.find_element_by_name("interestRate").send_keys("10")
                driver.find_element_by_name("raiseRate").send_keys("0")
                driver.find_element_by_name("commissionRate").send_keys("1")
                driver.find_element_by_name("serviceRate").send_keys("1")
                # 是否允许提前还本
                driver.find_element_by_name("advanceRepayState").click()
                # 按月
                # driver.find_element_by_xpath(".//*[@id='repayCapArea']/span/div[1]/input[2]").click()
                driver.find_element_by_id("returnCapDays").send_keys("0")
                # 选择借款人
                driver.find_element_by_link_text("请选择").click()
                time.sleep(1)

                driver.find_element_by_name("login").send_keys("15302602360")
                driver.find_element_by_id("searchForm-searchBtn").click()
                driver.find_element_by_link_text("选择").click()
                time.sleep (1)
                driver.find_element_by_name("type").click()
                time.sleep (1)
                # 正常标  爆款标 推荐标
                driver.find_element_by_xpath (".//*[@id='bidForm']/div/div/div[27]/select/option[2]").click ()
                time.sleep(1)
                # driver.find_element_by_xpath (".//*[@id='bidForm']/div/div/div[26]/select/option[3]").click ()
                # driver.find_element_by_xpath(".//*[@id='bidForm']/div/div/div[26]/select/option[4]").click()
                driver.find_element_by_xpath(".//*[@id='matchTypeSpan']/div/input[2]").click()
                driver.find_element_by_id ("startDate").click ()
                # time.sleep(1)
                frame = driver.find_element_by_xpath ("html/body/div[4]/iframe")

                driver.switch_to_frame (frame)
                driver.find_element_by_xpath (".//*[@id='dpTodayInput']").click ()

                # time.sleep(1)
                driver.switch_to_default_content ()
                # time.sleep(1)
                driver.find_element_by_id ("endDate").click ()
                # time.sleep(1)
                driver.switch_to_frame (frame)

                # time.sleep(1)
                driver.find_element_by_xpath (".//*[@id='dpTitle']/div[6]/a").click ()
                driver.find_element_by_xpath (".//*[@id='dpTitle']/div[6]/a").click ()
                driver.find_element_by_xpath ("html/body/div[1]/div[3]/table/tbody/tr[4]/td[3]").click ()
                # driver.find_element_by_xpath ("html/body/div[1]/div[3]/table/tbody/tr[4]/td[3]").click ()
                # time.sleep(1)
                driver.switch_to_default_content ()
                # time.sleep (1)
                driver.find_element_by_xpath (".//*[@id='bidForm']/div/div/div[28]/button[1]").click ()
                time.sleep(1)


                # # 手动输入验证码
                # # driver.find_element_by_xpath (".//*[@id='apLogin']/div[1]/ul/li[3]/p[3]/img").send_keys(text)
                # driver.find_element_by_id("button").submit()
                # # driver.find_element_by_name('verifyCode').clear()
                # #driver.find_element_by_xpath (".//*[@id='apLogin']/div[1]/ul/li[3]/p[3]/img").send_keys(text)
                # #driver.find_element_by_xpath (".//*[@id='button']").click()
                # driver.find_element_by_xpath(".//*[@id='left']/div/ul/li[5]/div/span[1]").click()
                # driver.find_element_by_link_text("筹款中的借款标").click()
                #
                # time.sleep(1)
                # handles=driver.current_window_handle
                # print(handles)
                # driver.switch_to_frame("contentIframe")
                # driver.find_element_by_link_text("添加").click()
                #
                # time.sleep(5)
                # driver.find_element_by_id("select1_input").click()
                # #月月赢 按月付息 到期还本
                # driver.find_element_by_id("li1_input_4303c3e0-c85f-11e4-90b2-d89d67270c78_2").click()
                # driver.find_element_by_id("select2_input").click()
                # driver.find_element_by_id("li2_input_1").click()
                # # title="m爆款标201822802"
                #
                #
                # driver.find_element_by_id("loanTitle").send_keys(d['title'])
                # driver.find_element_by_id("loanBorrowershowname").send_keys(d['title'])
                # driver.find_element_by_id("projectCode").send_keys(d['title'])
                # driver.find_element_by_id("amount").send_keys("10000")
                # driver.find_element_by_id("termvalue").send_keys("1")
                # driver.find_element_by_id("biddlimit").send_keys("365")
                # driver.find_element_by_id("rate").send_keys("8")
                # driver.find_element_by_id("raiseRate").send_keys("0")
                # driver.find_element_by_id("loanrate").send_keys("0")
                # driver.find_element_by_id("loanServiceRate").send_keys("0")
                # driver.find_element_by_id("select4_input").click()
                # # 标的属性
                # # driver.find_element_by_id("li4_input_2").click()
                #
                # #选择借款人
                # driver.find_element_by_xpath(".//*[@id='prodetail']/div[1]/table/tbody/tr[40]/td/input[2]").send_keys(Keys.SPACE)
                # # time.sleep(5)
                # WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.XPATH, "//html/body/div/div/div/div[2]/iframe")))
                # # a=driver.find_elements_by_xpath(".//*[@id='d86zjCDbir']/div[1]/div[2]/iframe")
                # # a=driver.find_element_by_xpath("//html/body/div[2]/div[1]/div[1]/div[2]")
                # a=driver.find_element_by_xpath("//html/body/div/div/div/div[2]/iframe")
                # driver.switch_to_frame(a)
                # # driver.switch_to_frame(a)
                # #dr.find_element_by_xpath(".//*[@id='d86zjCDbir']/div[1]/div[2]/iframe")
                # # driver.find_element_by_xpath("//form[@id='queryForm']/ul/li/span/input").send_keys("123")
                # driver.find_element_by_xpath(".//*[@id='loginName']").send_keys("transfer")
                # driver.find_element_by_link_text("查询").click()
                # time.sleep(3)
                # driver.find_element_by_link_text("选择").click()
                # time.sleep(1)
                # driver.switch_to_default_content()
                # driver.switch_to_frame("contentIframe")
                # driver.find_element_by_link_text("保存").submit()
                # time.sleep(5)
                # al=driver.switch_to_alert()
                # al.accept()
                # # # 返回列表上架
                # # driver.switch_to_default_content()
                # # driver.find_element_by_link_text("筹款中的借款标").click()
                # # driver.switch_to_frame("contentIframe")
                # # driver.find_element_by_name("title").send_keys(d['title'])
                # # driver.find_element_by_link_text("查询").click()
                # # driver.find_element_by_link_text("上架").click()
                # # time.sleep(1)
                # # # i=driver.find_element_by_class_name("___boxDialog").find_elements_by_tag_name("input")
                # #
                # # # driver.find_element(i[0]).click()
                # # # a=driver.find_element_by_xpath("//html/body/div/div/div/div[2]/iframe") ???
                # #
                # # driver.find_element_by_xpath("//html/body/div/div/div/div[3]/input[1]").click()
                # #
                # # # .//*[@id='r56OIMlaYm']/div[1]/div[3]/input[1]
                # #
                # # #a=driver.switch_to.active_element.send_keys("transfer")

if __name__ == "__main__":
    unittest.main ()

