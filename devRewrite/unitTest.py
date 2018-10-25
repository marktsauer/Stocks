import json
import os
import glob
import math
import decimal
from stats import getYint

dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'

# order files by date
files = glob.glob(dataDir + "*.json")
files.sort(key=os.path.getmtime)

# collect all data in one list
data = []
fLen = len(files)
i = 0

while i > fLen:
    


for i in files:
    with open(i) as f:
        j = json.load(f)
        jlen = len(j)
    for p in range(jlen):
        jsonStructure = {
                # 'x' : j[p]['minutes'],
                'x' : j[p]['key'],
                'y'   : j[p]['price']
            }
        data.append(jsonStructure)


print(getYint(data, 41))