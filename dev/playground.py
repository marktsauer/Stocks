import requests  # works fine with Python 2.7.9 (not 3.4.+)
import json
import time
 
def fetchPreMarket(symbol, exchange):
    link = "http://finance.google.com/finance/info?client=ig&q="
    url = link+"%s:%s" % (exchange, symbol)
    r = requests.get(url=url)
    print(url)
 
 
fetchPreMarket("SPY","NASDAQ")
