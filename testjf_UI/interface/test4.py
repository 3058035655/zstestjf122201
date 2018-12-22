import hashlib
a=' https://www.hongkunjinfu.com/investControllerFront.do?method=detail&code=abb7c0e3-99e8-42c8-9d14-b8d379bfa52a&tempType=2'
m = hashlib.md5 ()  # 创建md5对象
m.update (a.encode (encoding='UTF-8'))  # 生成加密串，其中password是要加密的字符串
# hashlib.md5('abcdefg'.encode(encoding='UTF-8')).hexdigest()
sign = m.hexdigest ()
print (sign)
#c773064e07605528fee1fec42b72b700  6ebff37372d5445b62158045477a5b5a
#a3db772dd35d1235b7290589a324c259    成功的