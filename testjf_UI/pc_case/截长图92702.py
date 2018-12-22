import jpype
from selenium import webdriver
import time
# #启动带插件的firefox
# fp=webdriver.FirefoxProfile(r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\hwtosi65.default")
# driver=webdriver.Firefox(fp)
# driver.get("https://www.hongkunjinfu.com/")
# time.sleep(2)
# driver.close()

# #导入jpype
# from jpype import *
# #启动java虚拟机，加载第三方类库
# # startJVM(r'C:\Program Files\Java\jre6\bin\client\jvm.dll','-ea',r'-Djava.class.path=c:\Program Files\Sikuli X\sikuli-script.jar')
# startJVM(r'C:\Program Files\Java\jre1.8.0_65\bin\server\jvm.dll','-ea',r'-Djava.class.path=D:\Documents\Downloads\sikulix.jar')
# #关闭java虚拟机shutdownJVM()

# from jpype import *
# startJVM(r'C:\Program Files\Java\jre1.8.0_65\bin\server\jvm.dll','-ea', r'-Djava.class.path=D:\Documents\Downloads\sikulixapi.jar')
# shutdownJVM()
# App = JClass('org.sikuli.script.App')
# Screen = JClass('org.sikuli.script.Screen')
# screen = Screen()
#

# from jpype import *
# startJVM(getDefaultJVMPath())
# java.lang.System.out.println("hello world")
# shutdownJVM()
#
# vmPath = jpype.getDefaultJVMPath()
# jpype.startJVM(vmPath,"-Djava.class.path=D:\Documents\Downloads\sikulixapi.jar:")



import jpype
jvmPath = jpype.getDefaultJVMPath()
jpype.startJVM(jvmPath)
jpype.java.lang.System.out.println( " hello world!" )
jpype.shutdownJVM()
