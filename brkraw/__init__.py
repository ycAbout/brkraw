from .lib import *

__version__ = '0.3.0.rc2'
__all__ = ['BrukerLoader', '__version__']


def load(path):
    return BrukerLoader(path)
