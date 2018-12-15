import requests
import json
from datetime import datetime
import time
import config as settings


class Stock():
    TEST_INTERVAL = 60
    SLEEP_INTERVAL = 300


    def __init__(self, symbol):
        self.api_url = settings.URL
        self.api_key = settings.KEY
        self.function = settings.FUNCTION
        self.symbol = symbol
        self.current_time = datetime.today().strftime('%Y-%m-%d')
        self.response = requests.get("{}/query?function={}&symbol={}&apikey={}".format(self.api_url, self.function, self.symbol, self.api_key ))
        self.data = self.response.json()
        self.open = self.data['Time Series (Daily)'][str(self.current_time)]['1. open']
        self.high = self.data['Time Series (Daily)'][str(self.current_time)]['2. high']
        self.low = self.data['Time Series (Daily)'][str(self.current_time)]['3. low']
        self.close = self.data['Time Series (Daily)'][str(self.current_time)]['4. close']
        self.volume = self.data['Time Series (Daily)'][str(self.current_time)]['5. volume']
        #self.intra_response = requests.get("{}/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey={}".format(self.api_url, self.symbol, self.api_key))

        
    
    def __repr__(self):
        return "Here's how {} is doing today: \nHigh: {}, Low: {}, Open: {}, Close: {}, Volume: {}".format(self.symbol, self.high, self.low, self.open, self.close, self.volume)


    def compare_high(self):
        original_value = self.high
        time.sleep(Stock.TEST_INTERVAL)
        updated_value = self.high

        if original_value >= updated_value:
            return "No worthwhile change to report on {}".format(self.symbol)
        else:
            return "Mo' money!"


    def compare_low(self):
        original_value = self.low
        time.sleep(Stock.TEST_INTERVAL)
        updated_value = self.low

        if original_value >= updated_value:
            return "No worthwhile change to report on {}".format(self.symbol)
        else:
            return "Headed to the poor house...Sell!"
    

    def compare_open_close(self):
        close_value = self.close
        open_value = self.open

        if open_value > close_value:
            pass
        elif close_value > open_value:
            pass
        else:
            pass