import pymysql.cursors
# 连接MySQL数据库
connection = pymysql.connect(host='192.168.1.249', port=3307, user='dev_db_user', password='yrSuper001', db='p2p_product_hotcopy',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()
# 创建sql 语句，并执行
# sql = "SELECT TITLE FROM bidd_info ORDER BY id LIMIT 1"
sql="SELECT loan_code,receipt_atm,receipt_capital_atm,RECEIPT_INTEREST_ATM,receipt_plan_time,receipt_user_name from loan_receipt_plan  where loan_code='53631095-2a76-47ca-9b46-bc46088bca42'"
cursor.execute(sql)
# 提交SQL
connection.commit()
t=cursor.fetchall()
# a=t['tel']
a=t
# b=a[0]['TITLE']
print(t)   # [{'tel': '15912345678'}]
print(a)
# print(b)
