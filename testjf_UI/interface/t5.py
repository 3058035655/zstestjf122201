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

# dict= sorted(dict.items(), key=lambda d:d[0], reverse = False) # reverse=True为降序。


list = sorted (dict.items ())
print(type(list))
list = sorted (dict.items ())
s = ''
for item in list:
    # dict[item[0]] = item[1]
    print(type(item[0]))
    a = item[0] + '=' + item[1] + '&'
    print (type (a))
    s = s + a
s = s[:-1]
print (s)