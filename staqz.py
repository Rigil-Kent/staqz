from os import path
import config as settings
from stock import Stock
import techanalysys
import click


PORTFOLIO = settings.PORTFOLIO.split(',')


def main():
    
    if settings.first_run() or not path.isfile(settings.config_file):
        settings.check_configuration(settings.config_file)
        print("This is the first run of STAQZ! Congrats!")

    for symbol in PORTFOLIO:
        print(Stock(symbol))


def staqs():
    pass

main()