#-*- coding:utf-8 -*-

import time
import sys
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')



excel = DATA_PATH + '/register.xlsx'
print('excel 的 类型是：',type(excel))
datas = ExcelReader (excel).data
print('datas的类型是：',type(datas))
for d in datas:
    with subTest (data=d):
       # print(int(d['title']))
        print(d)



