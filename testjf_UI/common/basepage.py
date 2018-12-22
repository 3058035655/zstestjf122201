import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import Config

url = Config().get ('URL')
class BasePage (object):
    def __init__(self):
        self.driver = selenium.webdriver.Chrome()
        # self.base_url = "http://192.168.1.249:8484/hk-management-services/index.html"  #测试环境
        # 预发布环境
        # self.base_url="http://39.105.87.46:8501/hk-management-services/login.html?_v=20180525targetUrlAfterLogin=http://39.105.87.46:8501/hk-management-services/index.html"
        self.base_url = url
        self.driver.get(self.base_url)

