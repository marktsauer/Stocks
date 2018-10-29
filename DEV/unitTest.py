import json
import os
import glob
import math
from stats import getYint, getPercentDif
import decimal


# dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/SPY/'


# get all but todays data
def buySell(daysToTest, bankBalance, shares, symbol):
    dataDir = os.path.dirname(os.path.realpath(__file__)) + '/data/' + symbol +'/'
    files = glob.glob(dataDir + "*.json")
    files.sort(key=os.path.getmtime)
    data = []
    lenF = len(files)
    i = 0
    while i < lenF - daysToTest:
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


    currentDBPrice = decimal.Decimal(data[-1]['y'])
    percentCounter = 0
    shareValue = shares * currentDBPrice
    totalMoney = bankBalance + shareValue




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

                #put calculaions, buys and sells in here 
                currentDBtime = (data[-1]['x'])
                currentDBPrice = decimal.Decimal(data[-1]['y'])
                # get y-intercept price
                yInt = 0
                yInt = getYint(data, currentDBtime) #replace with new API call getting real time price
                percentDif = getPercentDif(yInt, currentDBPrice)
                # print( percentDif)

                increment = .1

                if ((2 * increment) <= percentDif <= 10.5) and percentCounter != 2:
                    percentCounter = 2
                    bankBalance = bankBalance + (currentDBPrice * 2)
                    shares = shares - 2
                    shareValue = shares * currentDBPrice
                    # print(bankBalance,shares,shareValue,currentDBtime, yInt, currentDBPrice, percentDif, percentCounter)

                if ((1 * increment) <= percentDif <= (2 * increment)) and percentCounter != 1:
                    percentCounter = 1
                    bankBalance = bankBalance + currentDBPrice
                    shares = shares - 1
                    shareValue = shares * currentDBPrice
                    # print(bankBalance,shares,shareValue,currentDBtime, yInt, currentDBPrice, percentDif, percentCounter)

                elif ((-1 * increment) <= percentDif <= (1 * increment)) and percentCounter != 0:
                    percentCounter = 0
                    # print(bankBalance,shares,shareValue,currentDBtime, yInt, currentDBPrice, percentDif, percentCounter)

                elif ((-1 * increment) >= percentDif >= (-2 * increment)) and percentCounter != -1:
                    percentCounter = -1
                    bankBalance = bankBalance - currentDBPrice
                    shares = shares + 1
                    shareValue = shares * currentDBPrice
                    # print(bankBalance,shares,shareValue,currentDBtime, yInt, currentDBPrice, percentDif, percentCounter)
                
                elif ((-2 * increment) >= percentDif >= -10.5) and percentCounter != -2:
                    percentCounter = -2
                    bankBalance = bankBalance - (currentDBPrice * 2)
                    shares = shares + 2
                    shareValue = shares * currentDBPrice
                    # print(bankBalance,shares,shareValue,currentDBtime, yInt, currentDBPrice, percentDif, percentCounter)

        i += 1

        currentDBPrice = decimal.Decimal(data[-1]['y'])
        percentCounter = 0
        shareValue = shares * currentDBPrice
        totalMoney = bankBalance + shareValue
    # print('ENDING AT:', totalMoney)
    # print(bankBalance, shareValue, shares, currentDBPrice)

    return(totalMoney, bankBalance, shareValue, shares, currentDBPrice)

