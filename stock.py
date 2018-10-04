import requests
import json
import datetime
import time

apikey = 'MLQIDKUU3X5BCPGD'
symbol = 'SPY'
interval = '1min'

#gets stock data in json format
def callStockAPI():
    URL = "https://www.alphavantage.co/query"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'function': 'TIME_SERIES_INTRADAY', 'symbol': symbol, 'interval': interval, 'apikey': apikey}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    # extracting data in json format
    j = r.json()
    #data = r.json()
    return(j)

r = callStockAPI()
#print(r)

one_day = datetime.timedelta(days=1)
one_minute = datetime.timedelta(minutes=1)
today = datetime.datetime.today().replace(second=0).replace(microsecond=0) 


startTime = '2010-01-01 00:00:00'

i = int(round(time.time() * 1000))
print(i)

# def convertDatetimeToMil(dt):
#     i = int(round(time.time() * 1000))
#     print(i)

# convertDatetimeToMil(startTime)


#getsthe slope between 2 points
# def calculateSlope(p1, p2):
#     m = (p2[1] - p1[1]) / (p2[0] - p1[0])
#     print(m)

# p1 = [1,2]
# p2 = [5,7]
# calculateSlope(p1, p2)