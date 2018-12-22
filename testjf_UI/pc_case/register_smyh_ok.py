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
                driver=webdriver.Chrome()
                zcurl=qturl+'/regist.do?method=toRegist'
                driver.get(zcurl)
                driver.find_element_by_id("nickName").send_keys("hkjf")
                driver.find_element_by_id("login").send_keys(regtel)
                # 手动输入问题
                time.sleep (5)
                # driver.find_element_by_id("verify_code").send_keys('1')
                driver.find_element_by_id("sendSmsBtn").click()
                time.sleep(0.5)
                time.sleep(3)
                connection=Db().get_connection()
                cursor = Db().get_cursor()
                # cursor.execute ("SELECT id from bid_info where  name=%s", (bidname,))
                #SELECT * from sys_tel_message where tel='15912345678'
                cursor.execute ("SELECT * from sys_tel_message where tel=%s order by id desc limit 1",(regtel,))
                connection.commit ()
                t = cursor.fetchall ()
                yzm = t[0]['MESSAGE_NOTE']
                print(yzm)
                cursor.execute ("SELECT * FROM personinfo WHERE LOGIN_NAME=%s", (d['name'],))
                # SELECT * FROM personinfo WHERE LOGIN_NAME='牟泓霏'
                # UPDATE personinfo set login_name='',login_card='' where login_name='牟泓霏'
                connection.commit()
                t1=cursor.fetchall()
                print(t1)
                print()
                l = len (t1)
                # print (l)

                # 输入密码
                txt2 = driver.find_element_by_id ("txt2")
                action_a = ActionChains (driver)
                action_a.move_to_element (txt2).click ().send_keys ('a12345').send_keys (Keys.RETURN).perform ()
                # 推荐码
                # driver.find_element_by_id("commendPhone").send_keys("01307172")

                # 定位焦点方法
                elem = driver.find_element_by_id ("randCode")
                action_a0 = ActionChains (driver)
                action_a0.move_to_element (elem).click ().send_keys (yzm).send_keys (Keys.RETURN).perform ()

                driver.find_element_by_id("btn_sub").submit()

                #判断身份证，姓名是否已经被使用
                if l == 0:
                    print ('hello null')
                    driver.find_element_by_id ("loginName").send_keys (d['name'])  # 姓名
                    driver.find_element_by_id ("idCard").send_keys (d['idcard'])  # 身份证
                    driver.find_element_by_id ("email").send_keys ("123@126.com")  # 邮箱
                    driver.find_element_by_id ("btn_sub").click ()
                else:
                    print ('not null')
                    cursor.execute ("UPDATE personinfo set login_name='',login_card='' where login_name=%s", (d['name'],))
                    # SELECT * FROM personinfo WHERE LOGIN_NAME='牟泓霏'
                    # UPDATE personinfo set login_name='',login_card='' where login_name='牟泓霏'
                    connection.commit ()
                    # t1 = cursor.fetchall ()
                    # print (t1)
                    driver.find_element_by_id("loginName").send_keys(d['name'])   #姓名
                    driver.find_element_by_id("idCard").send_keys(d['idcard'])    #身份证
                    driver.find_element_by_id("email").send_keys("123@126.com")    #邮箱
                    driver.find_element_by_id("btn_sub").click()
                # time.sleep()
                # driver.find_element_by_link_text("跳过该环节>>").click()
                driver.close()


if __name__ == "__main__":
    unittest.main ()




