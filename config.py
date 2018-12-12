from configparser import ConfigParser
from datetime import datetime
from os import path
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


def first_run():
    if config['first_run'] == 0:
        return False
    else:
        return True


def generate_configuration():
    if platform.lower() == "windows":
        try:
            check_output(['type NUL > {}'.format(config_file),], shell=True)
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