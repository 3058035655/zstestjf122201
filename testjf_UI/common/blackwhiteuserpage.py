from selenium.webdriver.common.by import By
from testjf_UI.common.basepage import BasePage

class BlackWhitepage (BasePage):
    admin = (By.XPATH, ".//*[@id='login']")
    password = (By.XPATH, ".//*[@id='password']")
    # 验证码
    login_btn = (By.ID, "button")
    xtgl = (By.XPATH, ".//*[@id='left']/div/ul/li[17]/div/span[1]")
    yhgngl = (By.LINK_TEXT, "用户功能权限管理")
    tianjia = (By.LINK_TEXT, "添加")
    tel = (By.ID, "tel")
    gntype = (By.ID, "type")
    save=(By.LINK_TEXT,"保存")  #保存


    def set_admin(self, login):  # 输入用户名
        name = self.driver.find_element (*BlackWhitepage.admin)
        name.send_keys(login)

    def set_password(self, password):  # 输入密码
        pwd = self.driver.find_element (*BlackWhitepage.password)
        pwd.send_keys(password)

    def click_login(self):  # 单击登录
        loginbtn = self.driver.find_element (*BlackWhitepage.login_btn)
        loginbtn.click ()
    def click_xtgl(self):  # 点击系统管理
        xtglbtn = self.driver.find_element (*BlackWhitepage.xtgl)
        xtglbtn.click ()
    def click_yhgnmd(self):  # 点击用户功能权限管理
        yhgnmdbtn = self.driver.find_element (*BlackWhitepage.yhgngl)
        yhgnmdbtn.click ()
    def click_tianjia(self):  # 点击添加
        tianjiabtn = self.driver.find_element (*BlackWhitepage.tianjia)
        tianjiabtn.click ()
    def set_tel(self,tel):  # 输入用户
        teltxt = self.driver.find_element (*BlackWhitepage.tel)
        teltxt.send_keys(tel)
    def click_gntype(self):  # 点击功能类型
        gntypebtn = self.driver.find_element (*BlackWhitepage.gntype)
        gntypebtn.click()
    def click_save(self):  # 点击保存
        savebtn = self.driver.find_element (*BlackWhitepage.save)
        savebtn.click()

