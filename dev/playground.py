import json
import os
import glob
import math
import decimal
from stats import getYint
import os
import glob

dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'
# order files by date
files = glob.glob(dataDir + "*.json")
files.sort(key=os.path.getmtime)
data = []
lenF = len(files)
i = 0
while i < lenF:
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


print(getYint(data, decimal.Decimal(31.0134543)))

