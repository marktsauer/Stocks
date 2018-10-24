import requests
import json
import datetime
import time
from datetime import timedelta
import os

dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/'

#Time periods in datetime format that you can perform actions on such as today - one_day
startTime = datetime.datetime(2000,1,1) #type- datetime.datetime format- 2000-01-01 00:00:00 #use as base time to calculate against all other time
one_day = datetime.timedelta(days=1)
one_minute = datetime.timedelta(minutes=1)
today = datetime.datetime.today().replace(second=0).replace(microsecond=0) # 2018-10-05 10:06:00
smday = 390 #minutes in the stock market day

#converts datetime format to short date: 20181005
def shortDate(longDate):
    shortDate = longDate.strftime('%Y%m%d') 
    return(shortDate)


#calls API

#need to call this instead
    # https://api.iextrading.com/1.0/stock/SPY/quote

def callIEXStock(date, symbol):
    URL = "https://api.iextrading.com/1.0/stock/" + symbol + "/chart/date/" + date
    # defining a params dict for the parameters to be sent to the API
    #PARAMS = {'symbols' : 'SPY'}
    # sending get request and saving the response as response object
    r = requests.get(url=URL)#, params=PARAMS)
    # extracting data in json format
    data = json.loads(r.text)
    #data = r.json()
    listData = []
    for r in data:
        try:
            jsonStructure = {
                'date': r['date'],
                'minute' : r['minute'],
                'close'   : r['close']
            }
            listData.append(jsonStructure)
        except KeyError: pass
    return(listData)




#Puts a days worth of stock data in a document
def maintainDB(date, symbol, dayCount): #takes 20181005 format
    j = callIEXStock(date, symbol)
    dbPath = dataDir + symbol + "/"
    if not os.path.exists(dbPath):
        os.makedirs(dbPath)
    
    ext = ".json"
    f = dbPath+date+ext
    keyCount = dayCount * smday
    count = len(j)
    i = 0
    data = []
    if os.path.exists(f):
        filetime = datetime.datetime.fromtimestamp(os.path.getctime(f))
    else:
        filetime = today.date()
    # only creates file if it does not exist/ or if its todays file / or if the file was last updated before today
    if (not os.path.exists(f)) or (date == shortDate(today)) or (filetime.date() == today.date()):
        while i < count:
            #get data from API - type str
            d = j[i]['date']            # 20181005
            t = j[i]['minute'] + ':00'  # 09:30:00
            p = j[i]['close']            # 289.685
            #print(d,t,p)  # 20181005 09:30:00 289.685

            #add hiphens to date format
            newDate = datetime.datetime.strptime(d,'%Y%m%d').strftime('%Y-%m-%d')

            #convert API date and time to format that can be calculated in minutes
            #add new formatted date with time
            sDate = newDate + ' ' + t
            APIdateTime = datetime.datetime.strptime(sDate,"%Y-%m-%d %H:%M:%S") # type: datetime.datetime format: 2018-10-05 09:30:00

            #calculate APIdateTime in minutes
            tDelta = (APIdateTime - startTime).total_seconds() / 60# 592997400.0
            
            key = keyCount + i
            #create new object with preferred format to put in database
            jsonStructure = {
                'key'     : str(key),
                'dateTime': str(APIdateTime),
                'minutes' : str(tDelta),
                'price'   : str(p)
            }
            data.append(jsonStructure)
            i += 1
        with open(f, 'w', newline='\n') as outfile:
            json.dump(data, outfile)




def getMultiDays(days, symbol):
    i = days # to increment through days
    p = days # to set a base day to increment i off of
    a = days # to skip weekends
    while i >= 0:
        p = p - a
        one_day = datetime.timedelta(days=i)
        date = datetime.datetime.today().replace(second=0).replace(microsecond=0) - one_day
        d = shortDate(date)
        weekno = (date).weekday()
        if weekno < 5:
            maintainDB(d, symbol, p)
            a = a - 1
        p = days
        i = i - 1
        

    

getMultiDays(9, 'SPY')
#build in a way to delete days older than x days
