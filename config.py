from configparser import ConfigParser
from datetime import datetime, timedelta
import calendar
from os import path
import sys
import json
import platform
from subprocess import check_output
import setup as options


config = ConfigParser()
platform = platform.system()
config_file = options.__config__


def add_url(url):
    '''Change the API url'''
    config['api']['url'] = url
    try:
        with open(config_file, 'w') as file:
            config.write(file)

        sys.stdout.write("""
        =========================
        API URL has changed!
        =========================
        """)
    except Exception as err:
        raise SystemError("""
        ========================
        {}
        ========================
        """.format(err))



def add_key(key):
    '''Change your API key'''
    config['api']['key'] = key
    try:
        with open(config_file, 'w') as file:
            config.write(file)

        sys.stdout.write("""
        ====================
        API key has changed!
        ====================
        """)
    except Exception as err:
        raise SystemError("""
        ====================
        {}
        ====================
        """.format(err))


def generate_configuration():
    if platform.lower() == "windows":
        try:
            check_output(['type NUL > {}'.format(config_file),], shell=True)
            url = input("Enter the API url: ")
            add_url(url)
            key = input("Enter your key: ")
            add_key(key)
        except Exception as err:
            raise SystemError("""
        ====================
        {}
        ====================
        """.format(err))
    elif platform.lower() == "linux":
        try:
            check_output(['touch {}'.format(config_file),], shell=True)
            url = input("Enter the API url: ")
            add_url(url)
            key = input("Enter your key: ")
            add_key(key)
        except Exception as err:
            raise SystemError("""
        ====================
        {}
        ====================
        """.format(err))
    else:
        print("Sorry. Staqz doesn't support your OS (YET)!")

    if config['defaults']['first_run'] == 1:
        config['defaults']['first_run'] = 0


def get_prior_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    
    day_num = start_date.weekday()
    day_num_target = calendar.day_name[day_num]
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


config.read(config_file)
#FIRST_RUN = int(config['defaults']['first_run'])

URL = config['api']['url']
KEY = config['api']['key']
FUNCTION = config['api']['function']
TIME_FRAME = datetime.today().strftime('%Y-%m-%d %X')
PORTFOLIO = config['user']['portfolio']