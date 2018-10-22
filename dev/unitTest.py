import requests
import json
import datetime
import time
from datetime import timedelta
import os
# from stats import slr

bankAccountBalance = 25000


# print(slr(4267))

#get current price

def getCurrentIEXStock(symbol):
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

(getCurrentIEXStock("SPY"))

