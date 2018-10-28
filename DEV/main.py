from db import getMultiDays, dbCleanup
from unitTest import buySell
import datetime

start = datetime.datetime.today() # 2018-10-05 10:06:00
today = datetime.datetime.today().replace(second=0).replace(microsecond=0) # 2018-10-05 10:06:00
#Time periods in datetime format that you can perform actions on such as today - one_day
one_day = datetime.timedelta(days=1)
today = today - one_day - one_day - one_day - one_day

getMultiDays(13, 'SPY', today) # (days of data, symbol)
dbCleanup('SPY', 9) # (symbol, days to keep)

buySell(3) #days to test



end = datetime.datetime.today()
# print((end - start), 'seconds')