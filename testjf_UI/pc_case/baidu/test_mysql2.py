import unittest
import selenium
from telnetlib import EC
import xlrd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver, selenium
import time

from selenium.webdriver.support.wait import WebDriverWait

from utils.config import DATA_PATH
from utils.file_reader import ExcelReader
import pymysql.cursors
from locale import *


class TestLoanRcceiptplan2(unittest.TestCase):
    excel = DATA_PATH + '/investamount.xlsx'
    user = DATA_PATH + '/investuser1.xlsx'
    bidd = DATA_PATH + '/investbidd.xlsx'
    def test_loanreceiptplan2(self):
        connection = pymysql.connect (host='192.168.1.249', port=3307, user='dev_db_user', password='yrSuper001',
                                      db='p2p_product_hotcopy',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        fname = DATA_PATH + '/yueyueying.xlsx'
        fname2 = DATA_PATH + '/sanbiao.xlsx'
        bk = xlrd.open_workbook (fname)
        bk2 = xlrd.open_workbook (fname2)
        shxrange = range (bk.nsheets)
        shxrange2 = range (bk2.nsheets)
        try:
            sh = bk.sheet_by_name ("Sheet1")
            sh2 = bk2.sheet_by_name ("Sheet1")
        except:
            print
            "no sheet in %s named Sheet1" % fname
            "no sheet in %s named Sheet1" % fname2
        # 获取第一行第一列数据
        cell_value = sh.cell_value (1, 0)
        cell_value2 = sh.cell_value (2, 0)
        print (cell_value)
        print (cell_value2)
        # 通过cursor创建游标
        cursor = connection.cursor ()
        # sql = "SELECT code FROM bidd_info where title='%s'",(cell_value)   # 加str确认与%s匹配
        #
        # # 创建sql 语句，并执行
        # # sql = "SELECT code FROM bidd_info ORDER BY id LIMIT 1"
        # cursor.execute (sql)
        cursor.execute ("SELECT code FROM bidd_info where title=%s", (cell_value,))
        # 提交SQL
        connection.commit ()
        t = cursor.fetchall ()
        # a=t['tel']
        biddtitle = t
        biddcode1 = biddtitle[0]['code']
        # [{'tel': '15912345678'}]
        print (biddtitle)
        print (biddcode1)
        cursor.execute ("SELECT code FROM bidd_info where title=%s", (cell_value2,))
        # 提交SQL
        connection.commit ()
        t = cursor.fetchall ()
        # a=t['tel']
        biddtitle = t
        biddcode2 = biddtitle[0]['code']
        # [{'tel': '15912345678'}]
        print (biddtitle)
        print (biddcode2)
        biddcodes=[biddcode1,biddcode2]
        print(biddcodes[0])
        print(biddcodes[1])
if __name__ == "__main__":
    unittest.main ()