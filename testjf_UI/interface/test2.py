# URL = "http://192.168.1.249:9921/hkjfapp/invest/invest"
# dicts = {'access_token': '1b1d5757-9322-4d83-bb79-fed79f973dad',
#                               'amount': '100',
#                               'biddCode': 'biddcode',
#                               'investType': '1',
#                               'sessionId': 'sessionid',
#                               'sign': 'sign',
#                               'signType': 'MD5',
#                               'source': '4',
#                               'userCode': 'usercode'}
# dicts = sorted (dicts.items ())  #key按照字母排序
# def parse_url(data):
#     # data2 = sorted (data.items ())  #key按照字母排序
#     item=data.items()
#     urls="?"
#     for i in item:
#         (key,value)=i
#         temp_str = key+"="+value
#         urls = urls + temp_str+"&"
#     urls = urls[:len(urls)-1]
#     return urls
# print (URL + parse_url(dicts))
from testjf_UI.interface.test3 import Mysign
URL1 = "http://192.168.1.249:9921/hkjfapp/invest/invest?"
dict = {'access_token': '1b1d5757-9322-4d83-bb79-fed79f973dad', 'amount': '100', 'biddCode': 'biddcode','investType': '1','sessionId': 'sessionid','sign': 'sign', 'signType': 'MD5', 'source': '4', 'userCode': 'usercode'}

a=Mysign.mysign(dict)
add=URL1+a
print(add)