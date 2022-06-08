"""this is the IO class for the Gemstones app,
it will contain logic for reading multiple IO
types and writing results from calculations to
new files
"""
import builtins
import io
from typing import Dict, List
from more_itertools import consume
from contextlib import contextmanager

from gematria import Gematria

class Book(io.TextIOWrapper):
    '''The user must provide a line number
    on which the provided text begins the desired input.
    See README for example'''
    def __init__(self, path, *args, **kwargs):
        self._fobj = builtins.open(path, *args, **kwargs)

    def readlines(self, line_no):
        return consume((line for line in super().readlines()), line_no)

    def close(self):
        self._fobj.close()


@contextmanager
def f_open(path: str, /, *args, **kwargs):
    file = Book(path, *args, **kwargs)
    try:
        yield file
    except FileNotFoundError:
        raise
    finally:
        file.close()