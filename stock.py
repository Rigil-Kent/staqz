import requests
import json
from datetime import datetime, timedelta
import calendar
import time
import config as settings
from decimal import *


class Stock():
    __test_sleep__ = 60
    __sleep__ = 300
    __today__ = calendar.day_name[datetime.today().weekday()].lower()
    __offset__ = timedelta(minutes=5)

    def __init__(self, symbol):
        self.api_url = settings.URL
        self.api_key = settings.KEY
        self.function = settings.FUNCTION
        self.symbol = symbol
        self.current_time = datetime.today().now() - Stock.__offset__
        #self.response = requests.get("{}/query?function={}&symbol={}&apikey={}".format(self.api_url, self.function, self.symbol, self.api_key ))
        self.intra_response = requests.get("{}/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey={}".format(self.api_url, self.symbol, self.api_key))       
        self.data = self.intra_response.json()
        self.stock_data = next(iter(self.data['Time Series (1min)'].values()))
        self.open = float(self.stock_data['1. open'])
        self.high = float(self.stock_data['2. high'])
        self.low = float(self.stock_data['3. low'])
        self.close = float(self.stock_data['4. close'])
        self.volume = int(self.stock_data['5. volume'])

        
    
    def __repr__(self):
        return "Here's how {} is doing today: \nHigh: {}, Low: {}, Open: {}, Close: {}, Volume: {}".format(self.symbol, self.high, self.low, self.open, self.close, self.volume)

    
    def market_open(self):
        if  Stock.__today__ == "saturday" or Stock.__today__ == "sunday":
            return False
        else:
            return True

    def get_open(self):
        request = requests.get("{}/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey={}".format(self.api_url, self.symbol, self.api_key))
        request.json()
        __open__ = next(iter(self.data['Time Series (1min)'].values()))
        return __open__['1. open']


    def get_high(self):
        request = requests.get("{}/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey={}".format(self.api_url, self.symbol, self.api_key))
        request.json()
        __high__ = next(iter(self.data['Time Series (1min)'].values()))
        return __high__['2. high']

    
    def get_low(self):
        request = requests.get("{}/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey={}".format(self.api_url, self.symbol, self.api_key))
        request.json()
        __low__ = next(iter(self.data['Time Series (1min)'].values()))
        return __low__['3. low']


    def get_close(self):
        request = requests.get("{}/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey={}".format(self.api_url, self.symbol, self.api_key))
        request.json()
        __close__ = next(iter(self.data['Time Series (1min)'].values()))
        return __close__['4. close']


    def get_volume(self):
        request = requests.get("{}/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey={}".format(self.api_url, self.symbol, self.api_key))
        request.json()
        __volume__ = next(iter(self.data['Time Series (1min)'].values()))
        return __volume__['5. volume']


    def compare_high(self):
        if not self.market_open():
            return "Sorry, the market is closed"

        original_value = self.high
        time.sleep(Stock.__test_sleep__)
        updated_value = self.get_high()

        if original_value >= updated_value:
            return "No worthwhile change to report on {}".format(self.symbol)
        else:
            return "Mo' money!"


    def compare_low(self):
        if not self.market_open():
            return "Sorry, the market is closed"

        original_value = self.low
        time.sleep(Stock.__test_sleep__)
        updated_value = self.get_low()

        if original_value >= updated_value:
            return "No worthwhile change to report on {}".format(self.symbol)
        else:
            return "Headed to the poor house...Sell!"
    

    def compare_open_close(self):
        if not self.market_open():
            return "Sorry, the market is closed"

        close_value = self.get_close()
        open_value = self.get_open()

        if open_value > close_value:
            return "Open price has risen. Not an ideal to buy."
        elif open_value < close_value:
            return "Opening price has dropped. Looks like a great opportunity."
        else:
            return "I'm not sure what's going on here...and at this point I'm too afraid to ask..."