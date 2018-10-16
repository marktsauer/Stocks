import json
import datetime
import time
from datetime import timedelta
import os
import glob

dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'

# order file by date
files = glob.glob(dataDir + "*.json")
files.sort(key=os.path.getmtime)

data = []

for i in files:
    with open(i) as f:
        j = json.load(f)
        jlen = len(j)
        # print(jlen)
    for p in range(jlen):
        # print(p)
        jsonStructure = {
                # 'dateTime' : j[p]['dateTime'],
                'x' : j[p]['seconds'],
                'y'   : j[p]['price']
            }
        data.append(jsonStructure)
print(type(data))

# for i in data:
