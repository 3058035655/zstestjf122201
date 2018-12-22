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

from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import DATA_PATH, REPORT_PATH
from utils.config1 import Config
from utils.file_reader import ExcelReader
from utils.log import Logger, logger
from utils.mail import Email


class TestBaiDu(unittest.TestCase):
    # URL = Config().get('URL')
    # excel = DATA_PATH + '/baidu.xlsx'
    driver = selenium.webdriver.Chrome ()
    driver.get("https://www.baidu.com/")

    # http://192.168.1.249:8501/management/login.html


    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search'])
                time.sleep(2)
                # self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 ', description='修改html报告')
        runner.run(TestBaiDu('test_search'))
    e = Email(title='百度搜索测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='...',
              server='...',
              sender='...',
              password='...',
              path=report
              )
    e.send()