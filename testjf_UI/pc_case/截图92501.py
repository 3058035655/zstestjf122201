# var page = require('webpage').create();
# page.open('http://lib.csdn.net/experts/detail?type=11', function(status){
#     console.log('Status:' + status);
#     if(status === "success") {
#         page.render('example.png');
#     }
#     phantom.exit();
# });
#-*- coding:utf-8 -*-
import unittest
import time
import sys
import urllib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.log import logger
import os
from urllib.request import urlopen
from urllib.request import urlretrieve
import re
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage

from utils.config import Config
url = Config().get ('QTURL')
print(url)


class Test_Pclogin(unittest.TestCase):
    def test_pcLogin(self):
        #driver = webdriver.Chrome ()
        driver=webdriver.Firefox()
        # driver._is_remote = False  #POST /session/b7e401ca-5c0d-4cf2-ac9f-26b29baf3df7/actions did not match a known command 报错
        driver.maximize_window ()
        driver.get(url)
        # action = ActionChains (driver)
        # action.move_to_element (e1).click ().send_keys ('a12345').perform ()
        ActionChains (driver).send_keys (Keys.CONTROL + Keys.SHIFT + 'I').perform ()
        time.sleep(10)
        driver.close()

if __name__ == '__main__':
    unittest.main ()

