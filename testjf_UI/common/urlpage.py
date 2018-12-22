import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Config

class GetURL (object):
    def get_qturl(self):
        qturl=Config().get('QTURL')
        return qturl
    def get_hturl(self):
        hturl=Config().get('URL')
        return hturl

