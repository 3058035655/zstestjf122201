import pymysql
import readConfig as readConfig
from jkutrl.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()


class MyDB:
    global host, username, password, port, database, config
    host = localReadConfig.get_db("host")
    user = localReadConfig.get_db("user")
    password = localReadConfig.get_db("password")
    port = localReadConfig.get_db("port")
    db = localReadConfig.get_db("db")
    config = {
        'host': str(host),
        'user': user,
        'passwd': password,
        'port': int(port),
        'db': db}

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self, sql, params):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDB()
        # executing sql
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        """
        get all jkresult after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        """
        get one jkresult after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        return value

    def closeDB(self):
        """
        close database
        :return:
        """
        self.db.close()
        print("Database closed!")

