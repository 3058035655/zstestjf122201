import xlrd
from utils.config import DATA_PATH

excel = DATA_PATH + '/test.csv'
# data = xlrd.open_workbook(excel)
# table = data.sheet_by_index(0) #通过索引顺序获取,0表示第一张表
# data = [table.cell(i,ord('0')-ord('2')).value for i in range(1, 90)]
import csv

#读
with open(excel, "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
#     rows = [row for row in reader]
# print(rows)
    for col in reader:
        print(col)




#要提取其中某一列，可以用下面的代码：

#!/usr/bin/python3
# -*- conding:utf-8 -*-
# import csv
#
# #读取第二列的内容
# with open("test.csv", "r", encoding = "utf-8") as f:
# reader = csv.reader(f)
# column = [row[1] for row in reader]
#
# print(column)
#
# # 得到：['Name', 'mayi', 'jack', 'tom', 'rain']
# # 注意从csv读出的都是str类型。这种方法要事先知道列的序号，比如Name在第2列，而不能根据'Name'这个标题查询。这时可以采用第二种方法：