import requests
import json
import datetime
import time
from datetime import timedelta
import os
import glob
from db import getMultiDays
from stats import slr
import decimal

symbol = 'SPY'
print(symbol)
dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'
bankAccountBalance = 25000

#refresh data from db
getMultiDays(9, symbol)

# order files by date
files = glob.glob(dataDir + "*.json")
files.sort(key=os.path.getmtime)

#collect all data in one list
data = []
for i in files:
    with open(i) as f:
        j = json.load(f)
        jlen = len(j)
    for p in range(jlen):
        jsonStructure = {
                # 'x' : j[p]['minutes'],
                'x' : j[p]['key'],
                'y'   : j[p]['price']
            }
        data.append(jsonStructure)

#get last x-axis item in db
currentDBPrice = (data[-1]['x'])

#get real time IEX price from quote API (more acurate)
def getRealTimePrice(symbol):
    URL = "https://api.iextrading.com/1.0/stock/" + symbol + "/quote"
    # defining a params dict for the parameters to be sent to the API
    #PARAMS = {'symbols' : 'SPY'}
    # sending get request and saving the response as response object
    r = requests.get(url=URL)#, params=PARAMS)
    # extracting data in json format
    data = json.loads(r.text)
    #data = r.json()
    listData = []
    try:
        jsonStructure = {
            'latestTime': data['latestTime'],
            'iexRealtimePrice' : data['iexRealtimePrice']
        }
        listData.append(jsonStructure)
    except KeyError: pass
    return(listData)



# get what the stock should be based on 
slrPrice = decimal.Decimal(slr(decimal.Decimal(currentDBPrice)))
print(slrPrice)

# get what the stock price currently is
realTimePrice = decimal.Decimal((getRealTimePrice(symbol)[0]['iexRealtimePrice']))
print(realTimePrice)

# calculate percent deviation from slr line
def getPercentDif(slrPrice, realTimePrice):
    percentChange = ((realTimePrice - slrPrice) / realTimePrice) * 100
    return(percentChange)

print(getPercentDif(slrPrice, realTimePrice))


#deviation buy sell limits
s3 = 3.0
s2 = 2.0
s1 = 1.0
b1 = -1.0
b2 = -2.0
b3 = -3.0



