from db import getMultiDays, dbCleanup
from unitTest import unitTest

getMultiDays(9, 'SPY') # (days of data, symbol)
dbCleanup('SPY') # (symbol)

unitTest(3) #days to test


