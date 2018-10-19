import requests
import json
import datetime
import time
from datetime import timedelta
import os
today = datetime.datetime.today().replace(second=0).replace(microsecond=0) # 2018-10-05 10:06:00

one_day = datetime.timedelta(days=1)
weekno = (datetime.datetime.today() - one_day).weekday()
print(datetime.datetime.today() - one_day)

i = 0
while i < 7:
    one_day = datetime.timedelta(days=i)
    weekno = (today - one_day).weekday()
    print(weekno)
    i += 1