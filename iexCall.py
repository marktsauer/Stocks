def callIEXStock():
    URL = "https://api.iextrading.com/1.0"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'symbols' : 'AAPL'}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    # extracting data in json format
    data = json.loads(r.text)
    #data = r.json()
    print(data)

#callStock()
callIEXStock()

