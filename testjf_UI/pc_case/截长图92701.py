# import org.sikuli.script.SikulixForJython
# from sikuli import *
# print ("Hello World!Jython")
# x=1
# print (x)
# any = Screen(0)
# any.click("1m.png")
#
# 不正规的方法
import sys
sys.path.append("C:\\Users\\Administrator\\AppData\\Roaming\\Sikulix\\SikulixLibs_201510051707")

from sikuli import *
from sikuli import Screen

print ("Hello World!Jython")
x=1
print (x)
any = Screen(0)
any.click("img\\1m.png")

