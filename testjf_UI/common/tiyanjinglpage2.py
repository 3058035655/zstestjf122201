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
    #建标
    jkbgl = (By.XPATH, ".//*[@id='left']/div/ul/li[5]/div/span[1]")
    ckzjkb = (By.XPATH, ".//*[@id='left']/div/ul/li[5]/ul/li[1]/a")
    new = (By.LINK_TEXT, "添加")
    bidProduct = (By.ID, "select1_input")

    yyyay = (By.ID, "li1_input_4303c3e0-c85f-11e4-90b2-d89d67270c78_2")  # 月月盈-按月付息
    jjyay = (By.ID, "li1_input_68794eb3-c85f-11e4-90b2-d89d67270c78_3")  # 季季按月付息
    nnyay = (By.ID, "li1_input_89bbee85-c85f-11e4-90b2-d89d67270c78_4")  # 年年按月付息--

    yyydq = (By.ID, "li1_input_242618f5-0f78-11e7-8183-141877633774_2")  # 月月盈-到期一次还本付息
    jjydq = (By.ID, "li1_input_995f0b89-0f78-11e7-8183-141877633774_3")  # 季季-到期一次还本付息
    nnydq = (By.ID, "li1_input_c03159c5-0f78-11e7-8183-141877633774_4")  # 年年-到期一次还本付息
    tyb = (By.ID, "li1_input_b0006936-39e8-11e5-9ecc-1051721c3a3e_5")  # 体验标
    sanbiao = (By.ID, "li1_input_ef1f4fbb-c860-11e4-90b2-d89d67270c78_0")  # 常规借款产品
    grjk = (By.ID, "li1_input_934981df-2ac6-11e5-9ecc-1051721c3a3e_0")  # 个人借款
    xinshoubiao = (By.ID, "li1_input_69ba5f73-c866-11e4-90b2-d89d67270c78_0")  # 新手标
    haiw = (By.ID, "li1_input_3cf5c735-a078-11e8-8cdc-141877633774_10")  # 海外 产品

    loanuse = (By.ID, "select2_input")
    loanuseli = (By.ID, "li2_input_1")
    title = (By.ID, "loanTitle")
    loanBorrowershowname = (By.ID, "loanBorrowershowname")
    bidcode = (By.ID, "projectCode")

    totalAmount = (By.ID, "amount")
    termValue = (By.ID, "termvalue")
    biddlimit = (By.ID, "biddlimit")
    interestRate = (By.ID, "rate")
    raiseRate = (By.ID, "raiseRate")
    commissionRate = (By.ID, "loanrate")
    serviceRate = (By.ID, "loanServiceRate")
    # 逾期罚款
    # 选择借款人
    type = (By.ID, "select4_input")  # 标的属性
    zcbiao = (By.XPATH, ".//*[@id='bidForm']/div/div/div[27]/select/option[2]")  # 正常标  爆款标 推荐标
    bkbiao = (By.ID, "li4_input_2")
    tuijianbiao = (By.ID, "li4_input_3")
    choose2 = (By.XPATH, ".//*[@id='prodetail']/div[1]/table/tbody/tr[40]/td/input[2]")
    sanbiao_choose = (By.XPATH, ".//*[@id='prodetail']/div[1]/table/tbody/tr[44]/td/input[2]")
    loanuser = (By.XPATH, ".//*[@id='loginName']")
    search = (By.LINK_TEXT, "查询")
    chooseok = (By.LINK_TEXT, "选择")

    save = (By.LINK_TEXT, "保存")
    ok = (By.ID, "alertOkBtn")
    # 返回上架
    mingcheng = (By.NAME, "title")
    sousuo2 = (By.LINK_TEXT, "查询")
    shangjia = (By.LINK_TEXT, "上架")
    shangjiaok = (By.ID, "confirmOkBtn")
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
    #建标的方法
    def click_jkbgl(self):  # 单击借款标管理
        jkbglbtn = self.driver.find_element (*TiyanjinPage.jkbgl)
        jkbglbtn.click ()
    def click_ckzjkb(self):  # 单击筹款中的借款标
        ckzjkbbtn = self.driver.find_element (*TiyanjinPage.ckzjkb)
        ckzjkbbtn.click ()
    def click_new(self):  # 单击添加
        newbtn = self.driver.find_element (*TiyanjinPage.new)
        newbtn.click ()
    def click_bidProduct(self):  # 点击借款产品
        bidproductbtn = self.driver.find_element (*TiyanjinPage.bidProduct)
        bidproductbtn.click ()
    def click_yyyay(self):  # 选择月月赢按月付息
        yyyaybtn = self.driver.find_element (*TiyanjinPage.yyyay)
        yyyaybtn.click ()
    def click_jjyay(self):  # 选择季季赢按月付息
        jjyaybtn = self.driver.find_element (*TiyanjinPage.jjyay)
        jjyaybtn.click ()
    def click_nnyay(self):  # 选择年年盈赢按月付息
        nnyaybtn = self.driver.find_element (*TiyanjinPage.nnyay)
        nnyaybtn.click ()
    def click_yyydq(self):  # 选择月月赢到期
        yyydqbtn = self.driver.find_element (*TiyanjinPage.yyydq)
        yyydqbtn.click ()
    def click_jjydq(self):  # 选择季季赢到期
        jjydqbtn = self.driver.find_element (*TiyanjinPage.jjydq)
        jjydqbtn.click ()
    def click_nnydq(self):  # 选择年年赢到期
        nnydqbtn = self.driver.find_element (*TiyanjinPage.nnydq)
        nnydqbtn.click ()
    def click_tyb(self):  # 选择体验标
        tybbtn = self.driver.find_element (*TiyanjinPage.tyb)
        tybbtn.click ()

    def click_haiw(self):  # 选择海外
        tybbtn1 = self.driver.find_element (*TiyanjinPage.haiw)
        tybbtn1.click ()
    def click_sanbiao(self):  # 选择常规借款产品
        sanbiaobtn = self.driver.find_element (*TiyanjinPage.sanbiao)
        sanbiaobtn.click ()
    def click_xinshoubiao(self):  # 选择新手标
        xinshoubiaobtn = self.driver.find_element (*TiyanjinPage.xinshoubiao)
        xinshoubiaobtn.click ()
    def click_loanuse(self):  # 点击借款用途
        loanuse = self.driver.find_element (*TiyanjinPage.loanuse)
        loanuse.click ()
    def click_loanuseli(self):  # 选择借款用途
        loanuseli = self.driver.find_element (*TiyanjinPage.loanuseli)
        loanuseli.click ()
    def set_title(self, title):  # 输入标的名称
        bidtitle = self.driver.find_element (*TiyanjinPage.title)
        bidtitle.send_keys(title)
    def set_loanBorrowershowname(self, loanBorrowershowname):  # 输入标的名称
        loanBorrowershownametxt = self.driver.find_element (*TiyanjinPage.loanBorrowershowname)
        loanBorrowershownametxt.send_keys(loanBorrowershowname)

    def set_bidcode(self, bidcode):  # 输入标的code
        bidcodee = self.driver.find_element (*TiyanjinPage.bidcode)
        bidcodee.send_keys(bidcode)
    def set_totalAmount(self, totalAmount):  # 输入金额
        totalamount = self.driver.find_element (*TiyanjinPage.totalAmount)
        totalamount.send_keys(totalAmount)
    def set_termValue(self, termValue):  # 输入几个月
        termvalue = self.driver.find_element (*TiyanjinPage.termValue)
        termvalue.send_keys (termValue)
    def set_biddlimit(self, biddlimit):  # 满标期限
        biddlimittxt = self.driver.find_element (*TiyanjinPage.biddlimit)
        biddlimittxt.send_keys (biddlimit)
    def set_interestRate(self, interestRate):  # 输入年利率
        interestrate = self.driver.find_element (*TiyanjinPage.interestRate)
        interestrate.send_keys (interestRate)
    def set_raiseRate(self, raiseRate):  # 输入已加息利率
        raiseate = self.driver.find_element (*TiyanjinPage.raiseRate)
        raiseate.send_keys (raiseRate)
    def set_shouxufei(self, commissionRate):  # 输入手续费
        shouxufei = self.driver.find_element (*TiyanjinPage.commissionRate)
        shouxufei.send_keys (commissionRate)
    def set_serviceRate(self, serviceRate):  # 输入服务费
        servicerate = self.driver.find_element (*TiyanjinPage.serviceRate)
        servicerate.send_keys (serviceRate)

    def set_choose(self):  # 请选择借款人
        choosebtn = self.driver.find_element (*TiyanjinPage.choose2)
        choosebtn.send_keys (Keys.SPACE)
    def set_sanbiaochoose(self):  # 散标--请选择借款人
        sanbiaochoosebtn = self.driver.find_element (*TiyanjinPage.sanbiao_choose)
        sanbiaochoosebtn.send_keys (Keys.SPACE)
    def set_loanuser(self, loanuser):  # 输入借款人
        loanuserr = self.driver.find_element (*TiyanjinPage.loanuser)
        loanuserr.send_keys(loanuser)
    def click_search(self):  # 搜索借款人
        searchbtn = self.driver.find_element (*TiyanjinPage.search)
        searchbtn.click ()
    def click_searchok(self):  # 确认选择借款人
        searchokbtn = self.driver.find_element (*TiyanjinPage.chooseok)
        searchokbtn.click ()
    def click_type(self):  # 点击标的类型
        bidtype = self.driver.find_element (*TiyanjinPage.type)
        bidtype.click ()
    def click_zcbiao(self):  # 正常标
        zcbiaobtn = self.driver.find_element (*TiyanjinPage.zcbiao)
        zcbiaobtn.click ()
    def click_bkbiao(self):  # 爆款标
        bkbiaobtn = self.driver.find_element (*TiyanjinPage.bkbiao)
        bkbiaobtn.click ()
    def click_tuijianbiao(self):  # 推荐标
        tuijianbiaobtn = self.driver.find_element (*TiyanjinPage.tuijianbiao)
        tuijianbiaobtn.click ()
    def click_save(self):  # 保存
        savebtn = self.driver.find_element (*TiyanjinPage.save)
        savebtn.click ()
    def click_ok(self):  # 弹出框点击确认
        okbtn = self.driver.find_element (*TiyanjinPage.ok)
        okbtn.click ()
    def set_mingcheng(self, mingcheng):  # 输入标的名称
        mingchengtxt = self.driver.find_element (*TiyanjinPage.mingcheng)
        mingchengtxt.send_keys(mingcheng)
    def click_sousuo2(self):  # 点击搜索
        sousuobtn = self.driver.find_element (*TiyanjinPage.sousuo2)
        sousuobtn.click ()
    def click_shangjia(self):  # 点击上架
        shangjiabtn = self.driver.find_element (*TiyanjinPage.shangjia)
        shangjiabtn.click ()
    def click_shangjiaok(self):  # 点击上架
        shangjiaokbtn = self.driver.find_element (*TiyanjinPage.shangjiaok)
        shangjiaokbtn.click ()
