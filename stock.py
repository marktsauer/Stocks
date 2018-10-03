import requests
import json

apikey = 'MLQIDKUU3X5BCPGD'
symbol = 'SPY'
interval = '1min'

def callStock():
    URL = "https://www.alphavantage.co/query"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'function': 'TIME_SERIES_INTRADAY', 'symbol': symbol, 'interval': interval, 'apikey': apikey}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    # extracting data in json format
    data = json.loads(r.text)
    #data = r.json()
    print(data)

callStock()
