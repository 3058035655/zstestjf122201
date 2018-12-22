import urllib.request
file=urllib.request.urlopen("https://www.hongkunjinfu.com/")
data=file.read()
dataline=file.readline()
fhandle=open("./1.html","wb")
fhandle.write(data)
fhandle.close()