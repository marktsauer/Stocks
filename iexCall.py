import requests
import json
import datetime
import time
from datetime import timedelta
import os

#Time periods in datetime format that you can perform actions on such as today - one_day
startTime = datetime.datetime(2000,1,1) #type- datetime.datetime format- 2000-01-01 00:00:00 #use as base time to calculate against all other time
one_day = datetime.timedelta(days=1)
one_minute = datetime.timedelta(minutes=1)
today = datetime.datetime.today().replace(second=0).replace(microsecond=0) # 2018-10-05 10:06:00

#converts datetime format to short date: 20181005
def shortDate(longDate):
    shortDate = longDate.strftime('%Y%m%d') 
    return(shortDate)


days = 90
date = shortDate(today)
symbol = 'SPY'

#calls API
def callIEXStock(date, symbol):
    URL = "https://api.iextrading.com/1.0/stock/" + symbol + "/chart/date/" + date
    # defining a params dict for the parameters to be sent to the API
    #PARAMS = {'symbols' : 'SPY'}
    # sending get request and saving the response as response object
    r = requests.get(url=URL)#, params=PARAMS)
    # extracting data in json format
    #data = json.loads(r.text)
    data = r.json()
    return(data)

j = callIEXStock(date, symbol)


#Database maintainance

def maintainDB():
    dbPath = "/Users/marksauer/Documents/GitHub/Stocks/data/"
    ext = ".json"
    f = open(dbPath+date+ext,"a+")
    count = len(j)
    i = 0
    while i < count:
        #get data from API - type str
        d = j[i]['date']            # 20181005
        t = j[i]['minute'] + ':00'  # 09:30:00
        p = j[i]['open']            # 289.685
        #print(d,t,p)  # 20181005 09:30:00 289.685

        #add hiphens to date
        newDate = datetime.datetime.strptime(d,'%Y%m%d').strftime('%Y-%m-%d')

        #convert API date and time to format that can be calculated in minutes
        #add new formatted date with time
        sDate = newDate + ' ' + t
        APIdateTime = datetime.datetime.strptime(sDate,"%Y-%m-%d %H:%M:%S") # type: datetime.datetime format: 2018-10-05 09:30:00

        #calculate APIdateTime in minutes
        tDelta = (APIdateTime - startTime).total_seconds() # 6852 days, 9:30:00

        f.write(str(APIdateTime) + ',' + str(tDelta) + ',' + str(p) + '\n')
        i += 1
    f.close()

maintainDB()
