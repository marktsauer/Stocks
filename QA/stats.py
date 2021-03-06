import json
import math
import decimal

# simple linear regression formula 
def getYint(data, x):

    tot = len(data) # get total number of (x,y) points in data
    
    Ex = 0 #sum of x
    for i in range(tot):
        Ex = decimal.Decimal(Ex) + decimal.Decimal((data[i]['x']))
    
    Ey = 0 #sum of y
    for i in range(tot):
        Ey = decimal.Decimal(Ey) + decimal.Decimal((data[i]['y']))
    
    Mx = Ex / tot #mean of x
    
    My = Ey / tot # mean of y
    
    Exy = 0 # sum of x*y
    for i in range(tot):
        xy = decimal.Decimal((data[i]['x'])) * decimal.Decimal((data[i]['y']))
        Exy = Exy + xy
    
    Ex2 = 0 # x squared in all rows
    for i in range(tot):
        x2 = decimal.Decimal((data[i]['x'])) * decimal.Decimal((data[i]['x']))
        Ex2 = Ex2 + x2

    Ey2 = 0 # y squared in all rows
    for i in range(tot):
        y2 = decimal.Decimal((data[i]['y'])) * decimal.Decimal((data[i]['y']))
        Ey2 = Ey2 + y2

    xMx2 = 0 # (x - Mx)2
    for i in range(tot):
        xmx = (decimal.Decimal((data[i]['x'])) - Mx) * (decimal.Decimal((data[i]['x'])) - Mx)
        xMx2 = xMx2 + xmx

    yMy2 = 0 # (y - My)2
    for i in range(tot):
        ymy = (decimal.Decimal((data[i]['y'])) - My) * (decimal.Decimal((data[i]['y'])) - My)
        yMy2 = yMy2 + ymy
    
    # pearson coorelation coefficient (r)
    rt = (tot * Exy) - (Ex * Ey)
    rb = decimal.Decimal(math.sqrt(((tot * Ex2) - (Ex * Ex)) * ((tot * Ey2) - (Ey * Ey))))
    r = rt / rb

    # standard deviations of x and y
    Sx = math.sqrt(xMx2 / (tot - 1))
    Sy = math.sqrt(yMy2 / (tot - 1))

    # slope (b)
    b = r * decimal.Decimal((Sy / Sx))

    # y-intercept (a) based on slope
    a = My - (b * Mx)

   
    # given a point on the x-axis(time), this will give you a point in the y-axis(price) 
    y = a + (b * decimal.Decimal(x))
    
    return(y)

# print(getYint(data, 31.0134543))



# get percent dif between current price and y-int price
def getPercentDif(getYint, currentDBPrice):
    percentChange = ((currentDBPrice - getYint) / currentDBPrice) * 100
    return(percentChange)


