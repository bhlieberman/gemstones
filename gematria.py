from math import floor
from string import ascii_lowercase
from functools import reduce
from abc import ABC, abstractmethod
from deprecation import deprecated
from unsync import unsync

from translate import *
from hebrew_letters import CHARS_MAP
from nums_iter import rs_iter as rust_num_to_parts


class MisparGadol(ABC):
    @classmethod
    @abstractmethod
    def calculate(cls, /, *args):
        raise NotImplementedError


class Gematria(MisparGadol):
    '''This is a simple interface for performing numerological
    calculations using text entry'''
    mispar_gadol = lambda x: (10**(floor((x-1)//9))) * (((x-1)%9+1))
    total = 0 # running total for splitting number into components
    parts = [] # the 'components' of numbers
    _letters_ord = {k: v for k, v in [(letter, i) for i, letter in enumerate(ascii_lowercase, 1)]}

    def __init__(self):
        self._letters_utf = {k: v for k, v in [(letter, i) for i, letter in enumerate(ascii_lowercase, 97)]}
        self._letters_ord = {k: v for k, v in [(letter, i) for i, letter in enumerate(ascii_lowercase, 1)]}

    def __str__(self):
        return f"This is Gematria"

    def letters_utf(self, letter=None):
        if letter is not None:
            return self._letters_utf[letter]
        else:
            return self._letters_utf

    def letters_ord(self, letter=None):
        if letter is not None:
            return self._letters_ord[letter]
        else:
            return self._letters_ord

    @classmethod
    def calculate(cls, letter):
        '''Calculates the numerical value of a letter using mispar gadol method'''
        x = cls._letters_ord[letter]
        return cls.mispar_gadol(x)

    def convert_word(self, word):
        '''returns the total value of a word as the sum
        of its UTF-8 codepoint values'''
        _list = [letter for letter in word]
        _list_num = [self.letters_utf(letter) for letter in _list]
        self.total = reduce(lambda x, y: x + y, _list_num)
        return self

    @deprecated(details="Use the rust_num_to_parts method instead")
    def num_to_parts(self):
        '''iterative interface for splitting running total on class instance into components'''
        length = len(str(self.total))
        output = self.parts
        for _, val in enumerate(str(self.total)):
            output.append(int(val + '0'*(length - 1)))
            length -= 1
        return output

    def rust_num_to_parts(self):
        '''This method calls out to a Rust function,
        iteratively splitting the total into its parts'''
        return rust_num_to_parts(self.total)

    @unsync
    async def translator(self):
        '''Calls the Google Translate API'''
        letters = ''.join([CHARS_MAP[int(letter)] for letter in self.parts])
        return await translate(letters, 'en')
        
