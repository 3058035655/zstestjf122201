# coding=utf-8
import time

import selenium
from selenium.webdriver.common.by import By
from wxPython import wx

driver=driver=selenium.webdriver.Chrome()

driver.get("http://192.168.1.249:8602/financial/index.html")
time.sleep(10)
# C:\Users\Administrator\AppData\Roaming\Python\Python27\site-packages
# C:\Users\Administrator\AppData\Roaming\Python\Scripts
# python3.4 已经卸载了

VarifyApp = wx.App ()
VarifyApp.Frame = wx.Frame (None, -1, title="varify Message Box")
VarifyApp.Frame.Show ()
VarifyApp.MainLoop ()