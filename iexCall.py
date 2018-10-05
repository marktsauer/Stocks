import requests
import json
import datetime
import time

#Time periods in datetime format that you can perform actions on such as today - one_day
startTime = datetime.datetime(2000,1,1) #use as base time to calculate against all other time

one_day = datetime.timedelta(days=1)
one_minute = datetime.timedelta(minutes=1)
today = datetime.datetime.today().replace(second=0).replace(microsecond=0) #i.e. 2018-10-05 10:06:00


#converts to format short date (i.e. 20181005)
def shortDate(longDate):
    shortDate = longDate.strftime('%Y%m%d') 
    return(shortDate)

days = 21
date = shortDate(today)
symbol = 'SPY'

def callIEXStock(symbol, date):
    URL = "https://api.iextrading.com/1.0/stock/" + symbol + "/chart/date/" + date
    # defining a params dict for the parameters to be sent to the API
    #PARAMS = {'symbols' : 'SPY'}
    # sending get request and saving the response as response object
    r = requests.get(url=URL)#, params=PARAMS)
    # extracting data in json format
    #data = json.loads(r.text)
    data = r.json()
    return(data)

j = callIEXStock(symbol, date)
#print(j)

#get data from API
d = j[0]['date']            #20181005
t = j[0]['minute'] + ':00'  #09:30:00
p = j[0]['open']            #289.685
print(d,t,p)

newDate = datetime.datetime.strptime(str(d), '%Y%m%d').strftime('%Y-%m-%d')
print(newDate)
#print(startTime)
 

apiDate = datetime.datetime.strptime(d,'%Y%m%d') - one_day


# l = (len(j))
# print(l)
# i = 0
# while i < l:
#     print(j[i]['date'] , j[i]['minute'] , j[i]['open'])
#     i += 1
