from selenium.webdriver.common.by import By
from testjf_UI.common.basepage import BasePage

class PfRedpackage (BasePage):
    admin = (By.XPATH, ".//*[@id='login']")
    password = (By.XPATH, ".//*[@id='password']")
    # 验证码
    login_btn = (By.ID, "button")
    hbgl = (By.XPATH, ".//*[@id='left']/div/ul/li[14]/div/span[1]")
    pfhb = (By.LINK_TEXT, "派发红包")
    tel = (By.ID, "tel")
    sousuo = (By.LINK_TEXT, "查询")
    choose = (By.NAME, "checks")
    pfhbl = (By.LINK_TEXT, "派发红包")
    value = (By.ID, "redpageValue")
    packetEndDate = (By.ID, "limitDate")
    packetSendReason = (By.ID, "sendReason")
    queding=(By.LINK_TEXT,"确定")

    # 财务管理
    cwgl=(By.XPATH,".//*[@id='left']/div/ul/li[5]/div/span[1]")
    hbsh=(By.LINK_TEXT,"红包审核")
    dhuser=(By.ID,"exchangeTel")
    quanxuan = (By.ID, "types")
    plsh=(By.LINK_TEXT,"批量审核")
    shreason=(By.ID,"checkReason")
    tongyi=(By.XPATH,"//html/body/div/div/div/div[3]/input[1]")


    def set_admin(self, login):  # 输入用户名
        name = self.driver.find_element (*PfRedpackage.admin)
        name.send_keys(login)

    def set_password(self, password):  # 输入密码
        pwd = self.driver.find_element (*PfRedpackage.password)
        pwd.send_keys(password)

    def click_login(self):  # 单击登录
        loginbtn = self.driver.find_element (*PfRedpackage.login_btn)
        loginbtn.click ()
    def click_hbgl(self):  # 点击红包管理
        hbglbtn = self.driver.find_element (*PfRedpackage.hbgl)
        hbglbtn.click ()
    def click_pfhb(self):  # 点击派发红包
        pfhbbtn = self.driver.find_element (*PfRedpackage.pfhb)
        pfhbbtn.click ()
    def set_tel(self, tel):  # 输入用户
        teltxt = self.driver.find_element (*PfRedpackage.tel)
        teltxt.send_keys (tel)
    def click_sousuo(self):  # 点击搜索
        sousuobtn = self.driver.find_element (*PfRedpackage.sousuo)
        sousuobtn.click ()
    def click_choose(self):  # 选择用户
        choosebtn = self.driver.find_element (*PfRedpackage.choose)
        choosebtn.click ()
    def click_pfhbl(self):  #点击派发红包了
        pfhblbtn=self.driver.find_element(*PfRedpackage.pfhbl)
        pfhblbtn.click()
    def set_value(self, value):  # 输入金额
        valuetxt = self.driver.find_element (*PfRedpackage.value)
        valuetxt.send_keys(value)
    def set_enddate(self, packetEndDate):  # 输入过期日期
        enddatetxt = self.driver.find_element(*PfRedpackage.packetEndDate)
        enddatetxt.send_keys(packetEndDate)
    def set_packetSendReason(self, packetSendReason):  # 输入派发原因
        packetSendReasontxt = self.driver.find_element (*PfRedpackage.packetSendReason)
        packetSendReasontxt.send_keys(packetSendReason)
    def click_queding(self):  # 点击派发
        quedingbtn = self.driver.find_element (*PfRedpackage.queding)
        quedingbtn.click ()
    def click_cwgl(self):  # 财务管理
        cwglbtn = self.driver.find_element (*PfRedpackage.cwgl)
        cwglbtn.click ()
    def click_hbsh(self):  # 红包审核
        hbshbtn = self.driver.find_element (*PfRedpackage.hbsh)
        hbshbtn.click ()
    def set_dhuser(self, dhuser):  # 输入兑换红包用户
        dhusertxt = self.driver.find_element (*PfRedpackage.dhuser)
        dhusertxt.send_keys(dhuser)

    def click_quanxuan(self):  # 全选
        quanxuanbtn = self.driver.find_element (*PfRedpackage.quanxuan)
        quanxuanbtn.click ()
    def click_plsh(self):  # 批量审核
        plshbtn = self.driver.find_element (*PfRedpackage.plsh)
        plshbtn.click ()
    def set_shreason(self, shreason):  # 原因
        shreasontxt = self.driver.find_element (*PfRedpackage.shreason)
        shreasontxt.send_keys(shreason)
    def click_tongyi(self):  # 同意
        shokbtn = self.driver.find_element (*PfRedpackage.tongyi)
        shokbtn.click ()
