import pymysql
from readConfig import ReadConfig
# from jkutrl.config import Config
from utils.config import Config

host = Config().get ('HOST')
port=Config().get('PORT')
user=Config().get('user')
password=Config().get('password')
db=Config().get('db')
charset=Config().get('charset')

class Db(object):
    global connection
    connection = pymysql.connect (host=host, port=port, user=user, password=password, db=db, charset=charset,
                                         cursorclass=pymysql.cursors.DictCursor)
    def get_cursor(self):
        cursor = connection.cursor ()
        return cursor
    def get_connection(self):
            return connection
