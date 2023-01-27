import pymysql
from datadownloader import *
from csvparser import *
from nameconverter import *
from datetime import date

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
        sqlremove = "DELETE FROM stocks WHERE name = '" + name + "' AND DATE = '" + line[0] + "'"
        self.execute(sqlremove)
        self.conn.commit()
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

    def getMin(self, companyName):
        sql = "SELECT low, date FROM stocks WHERE name = '" + companyName + "' AND date > '" + str(date.today() - relativedelta(months=1)) + "' GROUP BY low, date ORDER BY low"
        self.execute(sql)
        data = self.fetch()
        if (len(data) == 0 or data[0][0] == None):
            return '-'
        return str(data[0][0]) + " on " + str(data[0][1])

    def getMax(self, companyName):
        sql = "SELECT high, date FROM stocks WHERE name = '" + companyName + "' AND date > '" + str(date.today() - relativedelta(months=1)) + "' GROUP BY high, date ORDER BY high DESC"
        self.execute(sql)
        data = self.fetch()
        if (len(data) == 0 or data[0][0] == None):
            return '-'
        return str(data[0][0]) + " on " + str(data[0][1])

    def getAvg(self, companyName):
        sql = "SELECT AVG((open + close) / 2) FROM stocks WHERE name = '" + companyName + "' AND date > '" + str(date.today() - relativedelta(months=1)) + "'"
        self.execute(sql)
        data = self.fetch()
        if (len(data) == 0 or data[0][0] == None):
            return '-'
        return str(round(data[0][0], 2))

    def getMedian(self, companyName):
        sql = "SELECT (open + close) / 2 FROM stocks WHERE name = '" + companyName + "' AND date > '" + str(date.today() - relativedelta(months=1)) + "' ORDER BY date"
        self.execute(sql)
        data = self.fetch()
        size = len(data)
        if (len(data) == 0 or data[0][0] == None):
            return '-'
        if (size % 2 == 0 and size > 0):
            return str(round((data[int(size / 2)][0] + data[int(size / 2 - 1)][0]) / 2, 2))
        if (size % 2 == 1):
            return str(round(data[int(size / 2)][0], 2))
        return 0

    def getVolume(self, companyName):
        sql = "SELECT SUM(volume) FROM stocks WHERE name = '" + companyName + "' AND date > '" + str(date.today() - relativedelta(months=1)) + "'"
        self.execute(sql)
        data = self.fetch()
        if (len(data) == 0 or data[0][0] == None):
            return '-'
        return str(data[0][0])

    def getDailyVolume(self, companyName):
        sql = "SELECT AVG(volume) FROM stocks WHERE name = '" + companyName + "' AND date > '" + str(date.today() - relativedelta(months=1)) + "'"
        self.execute(sql)
        data = self.fetch()
        if (len(data) == 0 or data[0][0] == None):
            return '-'
        return str(int(data[0][0]))

    def getHighestVolume(self, companyName):
        sql = "SELECT volume, date FROM stocks WHERE name = '" + companyName + "' AND date > '" + str(date.today() - relativedelta(months=1)) +"' GROUP BY volume, date ORDER BY MAX(volume) DESC"
        self.execute(sql)
        data = self.fetch()
        if (len(data) == 0 or data[0][0] == None):
            return '-'
        return str(data[0][0]) + " on " + str(data[0][1])

    def getLowestVolume(self, companyName):
        sql = "SELECT volume, date FROM stocks WHERE name = '" + companyName + "' AND date > '" + str(date.today() - relativedelta(months=1)) + "' AND date != '" + str(date.today()) + "' GROUP BY volume, date ORDER BY volume"
        self.execute(sql)
        data = self.fetch()
        if (len(data) == 0 or data[0][0] == None):
            return '-'
        return str(data[0][0]) + " on " + str(data[0][1])

