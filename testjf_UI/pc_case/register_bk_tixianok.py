import unittest
from telnetlib import EC

import pymysql
import xlrd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from db import Db
from utils.config import DATA_PATH
from utils.file_reader import ExcelReader
from testjf_UI.common.urlpage import GetURL
qturl=GetURL().get_qturl()


class Test_smyh(unittest.TestCase):
    tel = DATA_PATH + '/register_sm.xlsx'
    def test_Login(self):
        tels = ExcelReader (self.tel).data

        for d in tels:
            with self.subTest (data=d):
                regtel=int(d['login'])
                print(regtel)
                cursor=Db().get_cursor()
                connection = Db.get_connection (self)
                # cursor.execute ("SELECT id from bid_info where  name=%s", (bidname,))
                cursor.execute("SELECT code from loginuser where LOGIN=%s",(regtel,))  #查询code

                connection.commit ()
                t1 = cursor.fetchall ()
                code=t1[0]['code']
                print (code)
                cursor.execute ("SELECT ENTITY_STATUS from fn_account where user_code=%s", (code,)) #查询银行卡状态
                connection.commit ()
                t2 = cursor.fetchall ()
                print(t2)
                status = t2[0]['ENTITY_STATUS']

                # 判断是否已经绑卡   0未绑卡
                if status == 0:
                    print ('hello null')
                    cursor.execute ("update fn_account set bank_code=null,bank_account=null,entity_no=null,entity_status=0,entity_name=null,entity_bank=null,entity_dept=null,entity_province=null,entity_city=null,entity_addr=null where user_code=%s",
                        (code,))

                    # SELECT * FROM personinfo WHERE LOGIN_NAME='牟泓霏'
                    # UPDATE personinfo set login_name='',login_card='' where login_name='牟泓霏'
                    connection.commit ()
                    driver = webdriver.Chrome ()
                    driver.get(qturl)
                    WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
                    driver.find_element_by_id ('login').send_keys (regtel)
                    time.sleep (1)
                    e1 = driver.find_element_by_xpath (".//*[@id='txt2']")
                    action = ActionChains (driver)
                    action.move_to_element (e1).click ().send_keys ('a12345').perform ()
                    driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").click ()
                    driver.find_element_by_link_text ("我的账号").click ()
                    time.sleep(0.5)
                    driver.find_element_by_link_text ("提现").click ()
                    time.sleep (3)
                    driver.find_element_by_id("entityNo").send_keys("6228481200290317812")
                    driver.find_element_by_id("province").click()
                    driver.find_element_by_xpath(".//*[@id='province']/option[2]").click()
                    driver.find_element_by_id("city").click()
                    driver.find_element_by_xpath(".//*[@id='city']/option[1]").click()
                    driver.find_element_by_id("bank_entity_addr").send_keys("某支行")
                    driver.find_element_by_id("btn_sub").click()
                    driver.find_element_by_link_text("提现").click()
                    time.sleep(1)
                    driver.find_element_by_id ("tranAmt").send_keys ("0.01")
                    driver.find_element_by_id ("btn_sub").click ()
                    driver.close()
                #已经绑卡 status=1
                else:
                    print ('not null')

                    driver=webdriver.Chrome()
                    driver.get ('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
                    WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
                    driver.find_element_by_id ('login').send_keys (regtel)
                    time.sleep (1)
                    e1 = driver.find_element_by_xpath (".//*[@id='txt2']")
                    action = ActionChains (driver)
                    action.move_to_element (e1).click ().send_keys ('a12345').perform ()
                    driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").click()
                    driver.find_element_by_link_text("我的账号").click()
                    driver.find_element_by_link_text("提现").click()
                    time.sleep(1)
                    # driver.find_element_by_id("entityNo").send_keys("6228481200290317812")
                    # driver.find_element_by_id("province").click()
                    # driver.find_element_by_xpath(".//*[@id='province']/option[2]").click()
                    # driver.find_element_by_id("city").click()
                    # driver.find_element_by_xpath(".//*[@id='city']/option[1]").click()
                    # driver.find_element_by_id("bank_entity_addr").send_keys("某支行")
                    # driver.find_element_by_id("btn_sub").click()
                    # driver.find_element_by_link_text("提现").click()
                    driver.find_element_by_id("tranAmt").send_keys("0.01")
                    driver.find_element_by_id("btn_sub").click()





if __name__ == "__main__":
    unittest.main ()




