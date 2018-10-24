import json
import os
import glob
import math
import decimal

dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'

# order files by date
files = glob.glob(dataDir + "*.json")
files.sort(key=os.path.getmtime)

#collect all data in one list
# data = []
# for i in files:
#     with open(i) as f:
#         j = json.load(f)
#         jlen = len(j)
#     for p in range(jlen):
#         jsonStructure = {
#                 # 'x' : j[p]['minutes'],
#                 'x' : j[p]['key'],
#                 'y'   : j[p]['price']
#             }
#         data.append(jsonStructure)
        
        
# stage data
data = []

def getData(data):
    return(data)

def tot(data):
    tot = len(getData(data))
    return(tot)

#get sum of x
def Ex(tot, data):
    Ex = 0
    for i in range(tot):
        Ex = decimal.Decimal(Ex) + decimal.Decimal((data[i]['x']))
# print(Ex) # 247

#get sum of y
def Ey(tot, data):
    Ey = 0
    for i in range(tot):
        Ey = decimal.Decimal(Ey) + decimal.Decimal((data[i]['y']))
# print(Ey) # 486

#get mean of x
def Mx(tot, Ex):
    Mx = Ex(tot) / tot
    return(Mx)
# print(Mx) # 15.6

#get mean of x
def My(Ey):
    My = Ey(tot) / tot
    return(My)
# print(My) # 79.7

#get sum of x*y in all rows
Exy = 0
for i in range(tot):
    xy = decimal.Decimal((data[i]['x'])) * decimal.Decimal((data[i]['y']))
    Exy = Exy + xy
# print(Exy) # 20485

#get x squared in all rows
Ex2 = 0
for i in range(tot):
    x2 = decimal.Decimal((data[i]['x'])) * decimal.Decimal((data[i]['x']))
    Ex2 = Ex2 + x2
# print(Ex2) # 11409

#get y squared in all rows
Ey2 = 0
for i in range(tot):
    y2 = decimal.Decimal((data[i]['y'])) * decimal.Decimal((data[i]['y']))
    Ey2 = Ey2 + y2
# print(Ey2) # 40022

#get (x - Mx)2
xMx2 = 0
for i in range(tot):
    xmx = (decimal.Decimal((data[i]['x'])) - Mx) * (decimal.Decimal((data[i]['x'])) - Mx)
    xMx2 = xMx2 + xmx
# print(xMx2) # 42.40

#get (y - My)2
yMy2 = 0
for i in range(tot):
    ymy = (decimal.Decimal((data[i]['y'])) - My) * (decimal.Decimal((data[i]['y'])) - My)
    yMy2 = yMy2 + ymy
# print(yMy2) # 1206.10

#get pearson coorelation coefficient
def r():
    #find r from variables above
    rt = (tot * Exy) - (Ex * Ey)
    rb = decimal.Decimal(math.sqrt(((tot * Ex2) - (Ex * Ex)) * ((tot * Ey2) - (Ey * Ey))))
    r = rt / rb
    return(r) # 0.5298089018901743628197856966

#find slope
def b():
    Sx = math.sqrt(xMx2 / (tot - 1))
    Sy = math.sqrt(yMy2 / (tot - 1))
    b = r() * decimal.Decimal((Sy / Sx))
    return(b)

#find y intercept
def a():
    a = My - (b() * Mx)
    return(a)


#simple linear regression formula # this will give you a point in the y-axis(price) given a point on the x-axis(time)
def slr(x):
    y = a() + (b() * x)
    return(y)

# slr(11872)



