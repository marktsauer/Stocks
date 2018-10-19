import json
import datetime
import time
from datetime import timedelta
import os
import glob

dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'

#Time periods in datetime format that you can perform actions on such as today - one_day
startTime = datetime.datetime(2000,1,1) #type- datetime.datetime format- 2000-01-01 00:00:00 #use as base time to calculate against all other time
one_day = datetime.timedelta(days=1)
one_minute = datetime.timedelta(minutes=1)
today = datetime.datetime.today().replace(second=0).replace(microsecond=0) # 2018-10-05 10:06:00

#converts datetime format to short date: 20181005
def shortDate(longDate):
    shortDate = longDate.strftime('%Y%m%d') 
    return(shortDate)

# order files by date
files = glob.glob(dataDir + "*.json")
files.sort(key=os.path.getmtime)
print(files)
for i in files:
        print(os.path.getmtime(i))

# print(dattime.datetime(time.time()))

today = datetime.datetime.now().date()
today = datetime.datetime.today().replace(second=0).replace(microsecond=0) # 2018-10-05 10:06:00

print(today.date())

for file in os.listdir(dataDir):
    filetime = datetime.datetime.fromtimestamp(os.path.getctime(dataDir + file))
    print(filetime)
    if filetime.date() == today.date():
        print('true')