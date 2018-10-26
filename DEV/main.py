from db import getMultiDays, dbCleanup
from unitTest import buySell

getMultiDays(9, 'SPY') # (days of data, symbol)
dbCleanup('SPY') # (symbol)

buySell(3) #days to test


