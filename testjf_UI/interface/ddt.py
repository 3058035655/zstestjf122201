from selenium import webdriver
import  unittest,time

from  ddt import  ddt,unpack,data
# 测试数据


users =[{'username':'root','userpw':'123'},{'username':'roo1t','userpw':'123f'}]

@ddt
class LoginCase(unittest.TestCase):

    def setUp(self):
        self.fox = webdriver.Firefox()
        self.baseUrl = "http://localhost:8080/CookiesDemo/login.jsp"

    @data(*users)
    def testa(self,u):
        """正确用户和密码登录用例"""
        self.fox.get(self.baseUrl)
        login(self.fox,u['username'],u['userpw'])
        self.assertEqual(self.fox.title,u"登录","正确用户名和密码登录不成功")

    @data((2,3),(3,1))
    @unpack
    def testb(self,a,b):
        print(a,b)

    def tearDown(self):
        self.fox.quit()

if __name__ == '__main__':
    unittest.main()