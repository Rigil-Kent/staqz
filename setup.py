import config as settings
from distutils.core import setup
import sys
import os
import config as settings



__first_run__ = 1
__version__ = sys.version_info[:2]
__required__ = (3, 5)
if __version__ < __required__:
    sys.stderr.write("""
    ==========================
    Unsupported Python version
    ==========================
    """)
    sys.exit(1)


__description__ = ""


__config__ = "globals.cfg"
if not os.path.isfile(__config__):
    sys.stderr.write("""
    =============================
    Configuration file NOT FOUND
    =============================
    """)
    settings.generate_configuration()


setup(
    name="Staqz",
    version=__version__,
    description=__description__,
    author="Bryan Bailey",
    author_email="bryan.bailey@manjilabs.com",
    url="http://staqz.manjilabs.com",
    packages=[],
)
