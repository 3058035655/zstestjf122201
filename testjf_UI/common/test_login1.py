import unittest
import selenium
import time
from appium.webdriver import webdriver
from testjf_UI.common.basepage import BasePage
from testjf_UI.common.loginpage import LoginPage

class Test_Login (unittest.TestCase):
    def test_Login(self):
        # # Step1: 打开登录页
        # BasePage()

        # Step2: 初始化登录Page
        login_page=LoginPage()

        # Step3: 输入用户名
        login_page.set_username ("yradmin")

        # Step4: 输入密码
        login_page.set_password ("a12345")

        # Step5: 单击登录按钮
        login_page.click_login ()
        login_page.driver.maximize_window()
        time.sleep(43200)
        login_page.driver.close()


if __name__ == '__main__':
    unittest.main ()

