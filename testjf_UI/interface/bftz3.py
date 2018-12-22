import threading
import unittest
from telnetlib import EC

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
        driver=webdriver.Chrome()
        driver.get('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))


        driver.find_element_by_id ('login').send_keys (name)
        time.sleep(1)
        e1 = driver.find_element_by_xpath (".//*[@id='txt2']")
        action = ActionChains (driver)
        action.move_to_element (e1).click ().send_keys ("2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc").perform ()

        driver.find_element_by_xpath(".//*[@id='logindiv']/div/div[2]").submit()
        time.sleep(1)
        driver.get("http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail&code=477a34ea-b344-49fa-8dc2-b256b7502079")
        time.sleep(2)
        #投资金额
        driver.find_element_by_id("amount").send_keys("100")
        # driver.find_element_by_xpath(".//*[@id='clientInvestForm']/div[4]/a").click()
        driver.find_element_by_link_text("立即投资").click()
        time.sleep(1)
        #sreach_window=driver.current_window_handle
        #driver.find_element_by_xpath(".//*[@id='PDF9hFVQpC']/div[1]/div[3]/input[1]").click()
        driver.find_element_by_class_name("dialogBtn").click()
        #input class="dialogBtn" type="button" value="确定"
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






