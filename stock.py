import requests
import json
import time
import datetime


__url__ = "https://www.alphavantage.co"
__apikey__ = "O5R2662HM646PDS6"
__function__ = {
    "intra" : "TIME_SERIES_INTRADAY", #updates every 5m
    "daily" : "TIME_SERIES_DAILY",
    "current": "GLOBAL_QUOTE", #quick return of current market value
    "search": "SYMBOL_SEARCH",
}
__threshold__ = 31
__call_limit_min__ = 4
__call_limit_day__ = 499
min_call, day_call = 1, 1



def __isPenny__(price):
    '''Share prices under 5.00 are typically considered penny stocks. Expanded to 5.5'''
    if price <= 5.5:
        return True


def __capitalization__(price, volume):
    '''The Capitalization (market cap) is the value of outstanding shares divided by the price of a single share.'''
    cap = volume / price

    if cap < 250000000:
        return 'Micro Cap'
    elif cap < 1000000000:
        return "Small Cap"
    elif cap < 5000000000:
        return "Mid Cap"
    else:
        return "Ultra Cap"


def __wait__(minute, day):
    global min_call, day_call

    if day_call > day:
        raise SystemExit("The max alotted API calls have been made today. Please try again tomorrow.")
    else:
        day_call += 1
        return

    if min_call > minute:
        print("Processing...")
        time.sleep(30)
        min_call = 1
        return
    else:
        min_call += 1
        return


def __alert__(amount):
    if amount > __threshold__:
        return True
    else:
        return False


def get_financials(symbol):
    #__wait__(__call_limit_min__, __call_limit_day__)
    request = requests.get("{}/query?function={}&symbol={}&apikey={}".format(__url__,__function__['current'],symbol,__apikey__))
    data = request.json()
    

    if data['Global Quote']['01. symbol'] == symbol:
        price = float(data['Global Quote']['05. price'])
        change = float(data['Global Quote']['09. change'])
        volume = int(data['Global Quote']['06. volume'])
        opening = float(data['Global Quote']['02. open'])
        high = float(data['Global Quote']['03. high'])
        low = float(data['Global Quote']['04. low'])
        close = float(data['Global Quote']['08. previous close'])
        change_percent = data['Global Quote']['10. change percent']
        penny_stock = __isPenny__(price)
        financials = [price, change, volume, opening, high, low, close, change_percent, penny_stock]

    return financials


def get_name(symbol):
    #__wait__(__call_limit_min__, __call_limit_day__)
    request =  requests.get("{}/query?function={}&keywords={}&apikey={}".format(__url__, __function__['search'], symbol, __apikey__)) 
    data = request.json()
    if data['bestMatches'][0]['1. symbol'] == symbol:
        return data['bestMatches'][0]['2. name']
    else:
        return "Cannot parse stock symbol"
