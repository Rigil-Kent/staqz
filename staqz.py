import requests
import json
from datetime import datetime
import config as settings
import techanalysys
import click



API_URL = settings.URL
API_KEY = settings.KEY
FUNCTION = settings.FUNCTION
TIME_FRAME = datetime.today().strftime('%Y-%m-%d')
PORTFOLIO = settings.PORTFOLIO.split(',')


def init_request(url=API_URL):
    if url == None:
        url = input("Please enter the API url: ")
    try:
        request = requests.get("{}/query?function={}&symbol={}&apikey={}".format(url,FUNCTION,symbol,API_KEY))
        return request
    except Exception as err:
        print(err)


def main():
    while True:
        if settings.first_run():
            settings.check_configuration(settings.config_file)
            print("This is the first run of STAQZ! Congrats!")

        pass


def staqs():
    pass

for symbol in PORTFOLIO:
    print(symbol)
    response = init_request().json()
    print("Here's how {} did today\n{}".format(response['Meta Data']['2. Symbol'] , response['Time Series (Daily)'][TIME_FRAME]))
