from configparser import ConfigParser
from datetime import datetime
from os import path
import json
import platform
from subprocess import check_output


config = ConfigParser()
platform = platform.system()
config_file = "globals.cfg"
config.read(config_file)


URL = config['api']['url']
KEY = config['api']['key']
FUNCTION = config['api']['function']
TIME_FRAME = datetime.today().strftime('%Y-%m-%d')
PORTFOLIO = config['user']['portfolio']

def first_run():
    if int(config['defaults']['first_run']) == 0:
        return False
    else:
        return True


def add_url(url):
    '''Change the API url'''
    config['api']['url'] = url
    try:
        with open(config_file, 'w') as file:
            config.write(file)
    except Exception as err:
        return err



def add_key(key):
    '''Change your API key'''
    config['api']['key'] = key
    try:
        with open(config_file, 'w') as file:
            config.write(file)
    except Exception as err:
        return err


def generate_configuration():
    if platform.lower() == "windows":
        try:
            check_output(['type NUL > {}'.format(config_file),], shell=True)
            url = input("Enter the API url: ")
            add_url(url)
            key = input("Enter your key: ")
            add_key(key)
        except Exception as err:
            return err
    elif platform.lower() == "linux":
        try:
            check_output(['touch {}'.format(config_file),], shell=True)
        except Exception as err:
            return err
    else:
        print("Sorry. Staqz doesn't support your OS (YET)!")


def check_configuration(config_file):
    if (path.isfile(config_file)):
        return
    else:
        try:
            generate_configuration()
        except Exception as err:
            return err