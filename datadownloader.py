from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import requests

def dataPath(company):
    return "data/" + company + ".data"

def download(date1, date2, company):
    url = 'https://query1.finance.yahoo.com/v7/finance/download/' + company + '?period1=' + str(int(dt.timestamp(date1))) + '&period2=' + str(int(dt.timestamp(date2))) + '&interval=1d&events=history&includeAdjustedClose=true'
    response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    open(dataPath(company), "wb").write(response.content)

def downloadLastMonth(company):
    download(dt.now() - relativedelta(months=1), dt.now(), company)

downloadLastMonth("NVDA")