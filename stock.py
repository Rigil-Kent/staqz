import requests
import json
from datetime import datetime
import config as settings


class Stock():
    

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
        
    
    def __repr__(self):
        return "Here's how {} is doing today: \nHigh: {}, Low: {}, Open: {}, Close: {}, Volume: {}".format(self.symbol, self.high, self.low, self.open, self.close, self.volume)


