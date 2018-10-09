import os
import json
import datetime
import time
#need to make sure db path exists first
#just create /data at root

startTime = datetime.datetime(2000,1,1) #type- datetime.datetime format- 2000-01-01 00:00:00 #use as base time to calculate against all other time
one_day = datetime.timedelta(days=1)
one_minute = datetime.timedelta(minutes=1)
today = datetime.datetime.today().replace(second=0).replace(microsecond=0) # 2018-10-05 10:06:00


d = "/Users/marksauer/Documents/GitHub/Stocks/data/"
f = "test.json"
print(os.path.isdir(d))
print(os.path.exists(d+f))
print(d+f)

def maintainDB():
    print(today)


maintainDB()