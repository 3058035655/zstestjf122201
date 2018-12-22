# -*- coding:utf-8 -*-
import hashlib
from testjf_UI.interface.test3 import Mysign

m = hashlib.md5()  # 创建md5对象
m.update('abcdefg'.encode(encoding='UTF-8'))  # 生成加密串，其中password是要加密的字符串
# hashlib.md5('abcdefg'.encode(encoding='UTF-8')).hexdigest()
print(m.hexdigest())  # 打印经过md5加密的字符串


dict = {'access_token': '1b1d5757-9322-4d83-bb79-fed79f973dad',
                              'amount': '100',
                              'biddCode': 'biddcode',
                              'investType': '1',
                              'sessionId': 'sessionid',
                              'sign': 'sign',
                              'signType': 'MD5',
                              'source': '4',
                              'userCode': 'usercode'
                              }
a=Mysign.mysign(dict)
print(a)
# 加密
m = hashlib.md5 ()  # 创建md5对象
m.update (a.encode (encoding='UTF-8'))  # 生成加密串，其中password是要加密的字符串
# hashlib.md5('abcdefg'.encode(encoding='UTF-8')).hexdigest()
sign = m.hexdigest ()
print(sign)