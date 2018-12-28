import config as settings
from distutils.core import setup
import sys
import os
import threading
import webbrowser
import config as settings
from flask import Flask, render_template, request


setup_app = Flask(__name__)

__first_run__ = 1

__py_version__ = sys.version_info[:2]
__py_required__ = (3, 5)
if __py_version__ < __py_required__:
    raise SystemExit("""
    ==========================
    Unsupported Python version
    ==========================

    You are currently at {}. Please upgrade to {}.
    """.format(__py_version__, __py_required__))


@setup_app.route('/')
def first_run():
    url = request.args.get('url')
    key = request.args.get('key')
    function = "TIME_SERIES_DAILY"
    portfolio = request.args.get('portfolio')
    return render_template("setup.html", url=url, key=key, portfolio=portfolio)


__description__ = ""


__config__ = "globals.cfg"
if not os.path.isfile(__config__): 
    # pause the webbrowser.open call long enough to startup Flask - opens in default browser
    threading.Timer(1.25, lambda: webbrowser.open("http://127.0.0.1:5000")).start()    
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
