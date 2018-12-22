import unittest
from telnetlib import EC

import pymysql
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

from utils.config import DATA_PATH
from utils.file_reader import ExcelReader



connection = pymysql.connect (host='192.168.1.249', port=3307, user='dev_db_user', password='yrSuper001',
                              db='p2p_product_hotcopy',
                              charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor ()
cursor.execute ("SELECT message_note from sys_tel_message where tel='13301307172'" )
# 提交SQL
connection.commit ()
t = cursor.fetchall ()
# a=t['tel']

yzm = t[0]['message_note']
# [{'tel': '15912345678'}]
print(yzm)
print (t)

