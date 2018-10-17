import json
# import datetime
# import time
import os
import glob
import math
import decimal

dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'

# order files by date
files = glob.glob(dataDir + "*.json")
files.sort(key=os.path.getmtime)

#collect all data in one list
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

tot = len(data)


# #get sum of x
Ex = 0
for i in range(tot):
    Ex = decimal.Decimal(Ex) + decimal.Decimal((data[i]['x']))
print(Ex)

# #get sum of y
Ey = 0
for i in range(tot):
    Ey = decimal.Decimal(Ey) + decimal.Decimal((data[i]['y']))
print(Ey)

