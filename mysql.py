import pymysql

class stockDatabase(object):

    def __init__(self):
        self.chuj = 1

    def connect(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root', 
            password = 'root',
            db='finance',
        )
        self.cursor = self.conn.cursor()
    
    def disconnect(self):
        self.conn.close()

    def execute(self, command):
        self.cursor.execute(command)
    
    def fetch(self):
        return self.cursor.fetchall()

    
