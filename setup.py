import config as settings
from distutils.core import setup
import sys
import os
import threading
import webbrowser
import config as settings
from subprocess import check_output
from config import ConfigParser
from flask import Flask, render_template, request


setup_app = Flask(__name__)
__description__ = ""
__first_run__ = 1
__config__ = "globals.cfg"
__py_version__ = sys.version_info[:2]
__py_required__ = (3, 5)


if __py_version__ < __py_required__:
    raise SystemExit("""
    ==========================
    Unsupported Python version
    ==========================

    You are currently at {}. Please upgrade to {}.
    """.format(__py_version__, __py_required__))


def generate_configuration(url, key, portfolio, config_file):
    if sys.platform.lower() == "windows":
        try:
            check_output(['type NUL > {}'.format(config_file),], shell=True)
        except Exception as msg:
            return msg
    elif sys.platform.lower() == "linux":
        try:
            check_output(['touch {}'.format(config_file),], shell=True)
        except Exception as msg:
            return msg
    else:
        print("""
        ====================
        Sorry, your OS is not yet supported!
        ====================
        """)

    with open(config_file, 'w') as file:
        config = ConfigParser()
        config.add_section('defaults')
        config.set('defaults','first_run',str(False))

        config.add_section('api')
        config.set('api', 'url', url)
        config.set('api', 'key', key)

        config.add_section('user')
        config.set('user', 'portfolio', portfolio)

        try:
            config.write(file)
            sys.stdout.write("""
        =========================
        Configuration file initialized!
        =========================
        """)
        except Exception as err:
            raise SystemError("""
        ========================
        {}
        ========================
        """.format(err))


@setup_app.route('/setup')
def first_run():
    
    return render_template("setup.html" )


@setup_app.route('/thanks')
def thank_you():
    url = request.args.get('url')
    key = request.args.get('key')
    portfolio = request.args.get('portfolio')
    generate_configuration(url, key, portfolio, __config__)
    return render_template('thanks.html', url=url, key=key, portfolio=portfolio)


@setup_app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if not os.path.isfile(__config__): 
    # pause the webbrowser.open call long enough to startup Flask - opens in default browser
    threading.Timer(1.25, lambda: webbrowser.open("http://127.0.0.1:5000/setup")).start()    
    setup_app.run()
    

'''
setup(
    name="Staqz",
    version=__py_version__,
    description=__description__,
    author="Bryan Bailey",
    author_email="bryan.bailey@manjilabs.com",
    url="http://staqz.manjilabs.com",
    packages=[],
)'''
