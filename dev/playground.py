import json
import datetime
import time
from datetime import timedelta
import os
import glob

dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'
print(dataDir)

files = glob.glob(dataDir + "*.json")
files.sort(key=os.path.getmtime) #class = list
print(files)

