import threading
import unittest
from telnetlib import EC
import selenium
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

from utils.config import DATA_PATH


class TestBftz(unittest.TestCase):
    def test_bftz(name):
        driver = selenium.webdriver.Chrome ()
        driver.get ("http://192.168.1.249:9901/hkjf/loginAdmin.do?method=tologin")
        driver.find_element_by_xpath (".//*[@id='login']").send_keys ("yradmin")
        driver.find_element_by_xpath (".//*[@id='password']").send_keys ("a12345")
        time.sleep (5)
        driver.find_element_by_id ("button").submit ()
        driver.find_element_by_xpath(".//*[@id='left']/div/ul/li[7]/div/span[1]").click()
        driver.find_element_by_link_text("待放款的借款标").click()
        driver.find_element_by_link_text("放款").click()


    list=['13301307172','14510000051','14510000052','15510000051','15510000052','15510000053','16900000010','16900000011','13311553628','15500000001']
    # list=['13301307172','14510000051','14510000052''15510000051','15510000052']
    # list = ['13301307172', '14510000051', '14510000052', '15510000051', '15510000052','15510000053','16900000010','16900000011']
    threads = []
    files = range (len (list))
    # 创建线程
    for i in files:
        t = threading.Thread (target=test_bftz, args=(list[i],))
        threads.append (t)

    if __name__ == '__main__':
        # 启动线程
        for i in files:
            threads[i].start ()
    for i in files:
        threads[i].join ()
        print('end:%s' % time.ctime ())






