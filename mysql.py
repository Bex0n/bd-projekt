import pymysql

# mysql -u root -p
# haslo: root

class stockDatabase(object):

    def __init__(self):
        pass

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

    def getLatestDate(self, companyName):
        self.execute("SELECT * FROM STOCKS WHERE name = " + companyName)
        return self.fetch()
        

    
