from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from testjf_UI.common.basepage import BasePage
from testjf_UI.common.loginpage import LoginPage


class ZsJiaxiquan (BasePage):
    admin = (By.XPATH, ".//*[@id='login']")
    password = (By.XPATH, ".//*[@id='password']")
    # 验证码
    login_btn = (By.ID, "button")
    zzfw = (By.XPATH, ".//*[@id='left']/div/ul/li[24]/div/span[1]")
    zskq = (By.LINK_TEXT, "赠送卡券")
    tel = (By.ID, "tel")
    sousuo = (By.LINK_TEXT, "查询")
    choose = (By.NAME, "checks")
    ffqk=(By.LINK_TEXT,"发放券卡")
    type = (By.ID, "productType")
    # # 通过value进行选择
    # Select (driver.find_element_by_id ("prodType")).select_by_value ("01")
    # # 通过选项文字进行选择
    # Select (driver.find_element_by_id ("prodType")).select_by_visible_text ("信贷产品")
    # jxq=Select (driver.find_element_by_id ("productType")).select_by_visible_text ("加息券")
    # driver.find_element_by_id ("productType").find_elements_by_tag_name ("option")[1].click ();  # 根据父亲节点找

    pfkq=(By.LINK_TEXT,"派发卡券")
    reason = (By.ID, "_sendReason")
    tongyi=(By.XPATH,".//*[@id='returnBox']/div/div/input")

    ok=(By.XPATH,"//html/body/div/div/div/div[3]/input[1]")

    def set_admin(self, login):  # 输入用户名
        name = self.driver.find_element (*ZsJiaxiquan.admin)
        name.send_keys(login)

    def set_password(self, password):  # 输入密码
        pwd = self.driver.find_element (*ZsJiaxiquan.password)
        pwd.send_keys(password)

    def click_login(self):  # 单击登录
        loginbtn = self.driver.find_element (*ZsJiaxiquan.login_btn)
        loginbtn.click ()
    def click_zzfw(self):  # 点击增值服务
        zzfwbtn = self.driver.find_element (*ZsJiaxiquan.zzfw)
        zzfwbtn.click ()
    def click_zskq(self):  # 点击赠送卡券
        zskqbtn = self.driver.find_element (*ZsJiaxiquan.zskq)
        zskqbtn.click ()
    def set_tel(self,tel):  # 输入用户手机号
        teltxt = self.driver.find_element (*ZsJiaxiquan.tel)
        teltxt.send_keys(tel)
    def click_sousuo(self):  # 点击搜索
        sousuobtn = self.driver.find_element (*ZsJiaxiquan.sousuo)
        sousuobtn.click ()
    def click_choose(self):  # 选择用户
        choosekbtn = self.driver.find_element (*ZsJiaxiquan.choose)
        choosekbtn.send_keys(Keys.SPACE)
    def click_ffqk(self):   #点击发放券卡
        ffqkbtn=self.driver.find_element(*ZsJiaxiquan.ffqk)
        ffqkbtn.click()
    def click_type(self):
        typebtn=self.driver.find_element(*ZsJiaxiquan.type)
        typebtn.click()

    def click_pfkq(self):
        pfkqbtn=self.driver.find_element(*ZsJiaxiquan.pfkq)
        pfkqbtn.click()
    def set_reason(self,reason):
        reasontxt=self.driver.find_element(*ZsJiaxiquan.reason)
        reasontxt.send_keys(reason)
    def click_tongyi(self):
        tongyibtn=self.driver.find_element(*ZsJiaxiquan.tongyi)
        tongyibtn.click()
    def click_ok(self):
        okalert=self.driver.find_element(*ZsJiaxiquan.ok)
        okalert.click()



