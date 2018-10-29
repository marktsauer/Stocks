from db import getMultiDays, dbCleanup
from unitTest import buySell
import datetime
import os
import glob

# start = datetime.datetime.today() # 2018-10-05 10:06:00


today = datetime.datetime.today().replace(second=0).replace(microsecond=0) # 2018-10-05 10:06:00
#Time periods in datetime format that you can perform actions on such as today - one_day
one_day = datetime.timedelta(days=1)
dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/'



symbol = 'SPY'
daysToTest = 30
bankBalance = 10000
shares = 50
while daysToTest > 0:
    startday = (today - (one_day * daysToTest))
    getMultiDays(9, 'SPY', startday) # (days of data, symbol, day to start populating db)
    dbCleanup('SPY', 5) # (symbol, keep only x amount of files)
    dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/' + symbol +'/'
    files = glob.glob(dataDir + "*.json")
    files.sort(key=os.path.getmtime)
    lastFile = files[-1]
    path, filename = os.path.split(lastFile)
    totalMoney, bankBalance, shareValue, shares, currentDBPrice = buySell(1, bankBalance, shares, symbol)
    print(filename, 'Total Assets:',totalMoney, 'Bank Balance:',bankBalance, 'Share Value:',shareValue, 'Shares:', shares, 'Current Share Price:', currentDBPrice)
    daysToTest = daysToTest - 1



# end = datetime.datetime.today()
# print((end - start), 'seconds')