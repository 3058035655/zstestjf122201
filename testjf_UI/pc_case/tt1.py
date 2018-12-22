URL = "http://192.168.1.249:9921/hkjfapp/invest/invest"

os_type = {"os_type": "win_xp"}
content_tz = {'access_token': '1b1d5757-9322-4d83-bb79-fed79f973dad',
                              'amount': '100',
                              'biddCode': 'biddcode',
                              'investType': '1',
                              'sessionId': 'sessionid',
                              'sign': 'sign',
                              'signType': 'MD5',
                              'source': '4',
                              'userCode': 'usercode'
                              }
# rtz = requests.post ("http://192.168.1.249:9921/hkjfapp/invest/invest",params=content_tz, cookies=c)

def parse_url(data={}):
    # sorted (data.items (), key=lambda d: d[0], reverse=False)
    # data2=sorted(data.items())
    item = data.items ()
    print(item)
    urls = "?"
    for i in item:
        (key, value) = i
        temp_str = key + "=" + value
        urls = urls + temp_str + "&"
    urls = urls[:len (urls) - 1]
    return urls

print (URL + parse_url (content_tz))
# print (URL + parse_url (os_type))
