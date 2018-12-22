import csv

import time

from utils.config import DATA_PATH
# excel = DATA_PATH + '/test.csv'
# li=[]
# with open (excel, "r", encoding="utf-8") as f:
#     reader = csv.reader (f)
#     for col in reader:
#         # print (col[0])
#         li.append(col[0])
# print(li)
# startime=time.strftime("%Y%m%d%H%M%S")
# now=time.strftime("%Y%m%d%H%M%S")
# print(now)

startime = time.strftime ("%Y%m%d%H%M%S")
now = time.strftime ("%Y%m%d%H%M%S")
duratiion = input (u"输入持续运行时间:")
# while (startime + str (duratiion)) != now:
#     run (10, 1, int (duratiion))
#     now = time.strftime ("%Y%m%d%H%M%S")

print(type(duratiion))
print(type(startime))