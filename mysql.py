import pymysql
from datadownloader import *
from csvparser import *
from nameconverter import *

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

    def add(self, name, line):
        self.execute("SELECT COUNT(*) FROM stocks WHERE name = '" + name + "' AND DATE = '" + line[0] + "'")
        output = self.fetch()
        if (output[0][0] > 0):
            return
        sql = "INSERT INTO stocks (name, date, open, high, low, close, adjclose, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name, line[0], line[1], line[2], line[3], line[4], line[5], line[6])
        self.cursor.execute(sql, val)
        self.conn.commit()

    def getLastDate(self, companyName):
        self.execute("SELECT max(date) FROM stocks WHERE name = '" + companyName + "' ORDER BY date")
        data = self.fetch()
        return str(data[0][0])
    
    def updateLastMonth(self, companyName):
        downloadLastMonth(convertName(companyName))
        data = parseData(convertName(companyName))
        for position in data:
            self.add(companyName, position) 