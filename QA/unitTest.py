import json
import os
import glob
import math
from stats import getYint
import decimal

dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'

# order files by date
files = glob.glob(dataDir + "*.json")
files.sort(key=os.path.getmtime)


def getPercentDif(getYint, currentDBPrice):
    percentChange = ((currentDBPrice - getYint) / currentDBPrice) * 100
    return(percentChange)

# collect all data in one list
#get all but todays file
data = []
lenF = len(files)
i = 0
while i < lenF - 1:
    with open(files[i]) as f:
        j = json.load(f)
        jlen = len(j)
    for p in range(jlen):
        jsonStructure = {
                # 'x' : j[p]['minutes'],
                'x' : j[p]['key'],
                'y'   : j[p]['price']
            }
        data.append(jsonStructure)
    i += 1


#to iterate through one day testing after every minute
while i < lenF:
    with open(files[i]) as f:
        j = json.load(f)
        jlen = len(j)
        p = 0
        while p < jlen:
            jsonStructure = {
                # 'x' : j[p]['minutes'],
                'x' : j[p]['key'],
                'y'   : j[p]['price']
            }
            data.append(jsonStructure)
            p += 1

            tot = len(data)

            #put calculaions, buys and sells in here 
            currentDBtime = (data[-1]['x'])
            currentDBPrice = decimal.Decimal(data[-1]['y'])
            # get y-intercept price
            yInt = 0
            yInt = getYint(data, currentDBtime) #replace with new API call getting real time price
            percentDif = getPercentDif(yInt, currentDBPrice)
            print(yInt, currentDBPrice, percentDif)
            
    i += 1


# print(getYint(data, '32'))



# print(getYint(data, 41))