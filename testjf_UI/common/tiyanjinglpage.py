from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from testjf_UI.common.basepage import BasePage

class TiyanjinPage (BasePage):
    admin = (By.XPATH, ".//*[@id='login']")
    password = (By.XPATH, ".//*[@id='password']")
    # 验证码
    login_btn = (By.ID, "button")
    tyjgl = (By.XPATH, ".//*[@id='left']/div/ul/li[15]/div/span[1]")
    tyjff = (By.LINK_TEXT, "体验金发放")
    tel = (By.ID,"tel")
    sousuo = (By.LINK_TEXT, "查询")
    choose = (By.NAME, "checks")
    fftyj = (By.LINK_TEXT, "发送体验金")
    money=(By.ID,"simulAteMoney")
    qrff=(By.LINK_TEXT,"确认发放")

    def set_admin(self, admin):  # 输入用户名
        admintxt = self.driver.find_element (*TiyanjinPage.admin)
        admintxt.send_keys(admin)
    def set_password(self, password):  # 输入密码
        pwd = self.driver.find_element (*TiyanjinPage.password)
        pwd.send_keys(password)
    def click_login(self):  # 单击登录
        loginbtn = self.driver.find_element (*TiyanjinPage.login_btn)
        loginbtn.click ()

    def click_tyjgl(self):  # 单击体验金管理
        tyjglbtn = self.driver.find_element (*TiyanjinPage.tyjgl)
        tyjglbtn.click ()
    def click_tyjff(self):  # 单击体验金发放
        tyjffbtn = self.driver.find_element (*TiyanjinPage.tyjff)
        tyjffbtn.click ()
    def set_tel(self,tel):  # 输入用户手机号
        teltxt = self.driver.find_element (*TiyanjinPage.tel)
        teltxt.send_keys(tel)
    def click_sousuo(self):  # 点击搜索
        sousuobtn = self.driver.find_element (*TiyanjinPage.sousuo)
        sousuobtn.click ()
    def click_choose(self):  # 选择用户
        choosekbtn = self.driver.find_element (*TiyanjinPage.choose)
        choosekbtn.send_keys(Keys.SPACE)
    def click_fftyj(self):  # 点击发送体验金
        fstyjbtn = self.driver.find_element (*TiyanjinPage.fftyj)
        fstyjbtn.click ()
    def set_money(self,money):  # 输入金额
        moneytxt = self.driver.find_element (*TiyanjinPage.money)
        moneytxt.send_keys (money)
    def click_qrff(self):  # 确认发放
        qrffbtn = self.driver.find_element (*TiyanjinPage.qrff)
        qrffbtn.click ()
