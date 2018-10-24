import requests
import json
import datetime
import time
from datetime import timedelta
import os
import glob
import math
# from db import getMultiDays
# from stats import slr
import decimal

symbol = 'SPY'
print(symbol)
dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'

#refresh data from db
# getMultiDays(9, symbol)

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
# currentDBPrice = (data[-1]['x'])
# print(currentDBPrice)

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



# # get what the stock should be based on 
# slrPrice = decimal.Decimal(slr(decimal.Decimal(currentDBPrice)))
# print(slrPrice)

# # get what the stock price currently is
# realTimePrice = decimal.Decimal((getRealTimePrice(symbol)[0]['iexRealtimePrice']))
# print(realTimePrice)

# calculate percent deviation from slr line
def getPercentDif(slrPrice, realTimePrice):
    percentChange = ((realTimePrice - slrPrice) / realTimePrice) * 100
    return(percentChange)

# print(getPercentDif(slrPrice, realTimePrice))

#get sum of x
def Ex(tot):
    Ex = 0
    for i in range(tot):
        Ex = decimal.Decimal(Ex) + decimal.Decimal((data[i]['x']))
# print(Ex) # 247

#get sum of y
def Ey(tot):
    Ey = 0
    for i in range(tot):
        Ey = decimal.Decimal(Ey) + decimal.Decimal((data[i]['y']))
# print(Ey) # 486

#get mean of x
def Mx(Ex):
    Mx = Ex(tot) / tot
    return(Mx)
# print(Mx) # 15.6

#get mean of x
def My(Ey):
    My = Ey(tot) / tot
    return(My)
# print(My) # 79.7

#get sum of x*y in all rows
Exy = 0
for i in range(tot):
    xy = decimal.Decimal((data[i]['x'])) * decimal.Decimal((data[i]['y']))
    Exy = Exy + xy
# print(Exy) # 20485

#get x squared in all rows
Ex2 = 0
for i in range(tot):
    x2 = decimal.Decimal((data[i]['x'])) * decimal.Decimal((data[i]['x']))
    Ex2 = Ex2 + x2
# print(Ex2) # 11409

#get y squared in all rows
Ey2 = 0
for i in range(tot):
    y2 = decimal.Decimal((data[i]['y'])) * decimal.Decimal((data[i]['y']))
    Ey2 = Ey2 + y2
# print(Ey2) # 40022

#get (x - Mx)2
xMx2 = 0
for i in range(tot):
    xmx = (decimal.Decimal((data[i]['x'])) - Mx) * (decimal.Decimal((data[i]['x'])) - Mx)
    xMx2 = xMx2 + xmx
# print(xMx2) # 42.40

#get (y - My)2
yMy2 = 0
for i in range(tot):
    ymy = (decimal.Decimal((data[i]['y'])) - My) * (decimal.Decimal((data[i]['y'])) - My)
    yMy2 = yMy2 + ymy
# print(yMy2) # 1206.10

#get pearson coorelation coefficient
def r():
    #find r from variables above
    rt = (tot * Exy) - (Ex * Ey)
    rb = decimal.Decimal(math.sqrt(((tot * Ex2) - (Ex * Ex)) * ((tot * Ey2) - (Ey * Ey))))
    r = rt / rb
    return(r) # 0.5298089018901743628197856966

#find slope
def b():
    Sx = math.sqrt(xMx2 / (tot - 1))
    Sy = math.sqrt(yMy2 / (tot - 1))
    b = r() * decimal.Decimal((Sy / Sx))
    return(b)

#find y intercept
def a():
    a = My - (b() * Mx)
    return(a)


#simple linear regression formula # this will give you a point in the y-axis(price) given a point on the x-axis(time)
def slr(x):
    y = a() + (b() * x)
    return(y)

#deviation buy sell limits
s3 = 3.0
s2 = 2.0
s1 = 1.0
b1 = -1.0
b2 = -2.0
b3 = -3.0

# order files by date
files = glob.glob(dataDir + "*.json")
files.sort(key=os.path.getmtime)
#get all but todays file
data = []
lenF = len(files)
i = 0
while i < lenF - 1:
    with open(files[i]) as f:
        j = json.load(f)
        jlen = len(j)
    for p in range(jlen):
        jsonStructure = {
                # 'x' : j[p]['minutes'],
                'x' : j[p]['key'],
                'y'   : j[p]['price']
            }
        data.append(jsonStructure)
    i += 1

#to iterate through one day testing after every minute
while i < lenF:
    with open(files[i]) as f:
        j = json.load(f)
        jlen = len(j)
        p = 0
        while p < jlen:
            jsonStructure = {
                # 'x' : j[p]['minutes'],
                'x' : j[p]['key'],
                'y'   : j[p]['price']
            }
            data.append(jsonStructure)
            p += 1

            tot = len(data)

            #put calculaions, buys and sells in here 
            bankAccountBalance = 25000
            currentDBtime = (data[-1]['x'])
            currentDBPrice = (data[-1]['y'])
            # get slr price
            slrPrice = decimal.Decimal(slr(decimal.Decimal(currentDBtime)))

            # get what the stock price currently is
            realTimePrice = decimal.Decimal(currentDBPrice)

            percentDif = getPercentDif(slrPrice, realTimePrice)
            print(slrPrice, realTimePrice, percentDif)

               
    i += 1

# print(data)
print(len(data))


