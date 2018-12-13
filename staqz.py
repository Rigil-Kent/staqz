import requests
import json
from datetime import datetime
import config as settings
from stock import Stock
import techanalysys
import click


PORTFOLIO = settings.PORTFOLIO.split(',')


def initialize_portfolio():
    pass


def main():
    while True:
        if settings.first_run():
            settings.check_configuration(settings.config_file)
            print("This is the first run of STAQZ! Congrats!")

        pass


def staqs():
    pass

for symbol in PORTFOLIO:
    print(Stock(symbol))