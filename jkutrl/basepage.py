import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import Config
url = Config().get ('JKURL')

class BasePage (object):
    def get_url(self):
        return url

