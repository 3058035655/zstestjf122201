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
from utils.file_reader import ExcelReader


class TestTouzinny(unittest.TestCase):
    excel = DATA_PATH + '/investamount.xlsx'
    user=DATA_PATH+'/investuser1.xlsx'
    bidd=DATA_PATH+'/investbidd.xlsx'
    def test_touzinny(self):
        datas = ExcelReader (self.excel).data
        tzusers=ExcelReader(self.user).data
        tzbidds=ExcelReader(self.bidd).data
        for d in datas:
            with self.subTest (data=d):

                for u in tzusers:
                    driver = webdriver.Chrome ()
                    driver.get ('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
                    WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
                    with self.subTest(tzuser=u):
                        driver.find_element_by_id ('login').send_keys (int(u['user']))
                        time.sleep(1)
                        e1 = driver.find_element_by_xpath (".//*[@id='txt2']")
                        action = ActionChains (driver)
                        action.move_to_element (e1).click ().send_keys ("2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc").perform ()

                        driver.find_element_by_xpath(".//*[@id='logindiv']/div/div[2]").submit()
                        for b in tzbidds:
                            with self.subTest (tzbidd=b):
                                # address=("http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail&code=ed791706-92f7-4435-b6f6-aa944ed87f4c")
                                ad1 = "http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail&code="
                                ad2 = b['bidd_code']
                                add = ad1 + ad2
                                driver.get(add)
                                time.sleep(1)
                                # driver.find_element_by_id ("projectCode").send_keys (d['title'])
                                driver.find_element_by_id("amount").send_keys(int(d['amount']))
                                driver.find_element_by_link_text("立即投资").click()
                                time.sleep(3)
                #sreach_window=driver.current_window_handle
                #driver.find_element_by_xpath(".//*[@id='PDF9hFVQpC']/div[1]/div[3]/input[1]").click()
                                driver.find_element_by_class_name("dialogBtn").click()
                                #input class="dialogBtn" type="button" value="确定"




if __name__ == "__main__":
    unittest.main ()




