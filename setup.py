import config as settings
from distutils.core import setup
import sys
import os
import config as settings


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


__description__ = ""


__config__ = "globals.cfg"
if not os.path.isfile(__config__):
    raise SystemError("""
    =============================
    Configuration file NOT FOUND
    =============================
    """)
    settings.generate_configuration()

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
