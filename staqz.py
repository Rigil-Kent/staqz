from os import path
import config as settings
from stock import Stock
import techanalysys
import click


PORTFOLIO = settings.PORTFOLIO.split(',')


def main():
    for symbol in PORTFOLIO:
        print(Stock(symbol))
        print(Stock(symbol).compare_high())


def staqs():
    if not Stock.market_open():
        raise SystemExit("""
            ===========================================
            Markets are closed today! At ease, soldier!
            ===========================================
            """)
    else:
        pass


main()