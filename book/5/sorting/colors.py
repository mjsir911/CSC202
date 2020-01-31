#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import functools

__appname__     = "colors"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

step = True

class FreezeList(list):
    def __init__(self, optional=None):
        self.next = False

    def __getitem__(self, index):
        while not self.next:
            import time
            time.sleep(0.00001)
        self.next = False
        super().__getitem__(index)



@functools.total_ordering
class Color():
    def __init__(self, val):
        self.r = int((val >> 16) & 0xFF)
        self.g = int((val >> 8)  & 0xFF)
        self.b = int((val >> 0)  & 0xFF)

    def __int__(self):
        return (self.r << 16) | (self.g << 8) | self.b

    def _hue(self):

        import colorsys
        return colorsys.rgb_to_hsv(self.r, self.g, self.b)
        R = self.r / 255
        G = self.g / 255
        B = self.b / 255

        if R == G == B:
            return 240
        elif R == max((R, G, B)):
            return (G - B) / (R - min((R, G, B)))
        elif G == max((R, G, B)):
            return 2 + (B - R) / (G - min((R, G, B)))
        elif B == max((R, G, B)):
            return 4 + (R - G) / (B - min((R, G, B)))

    def _hilbert(self):
        import hilbert
        return hilbert.Hilbert_to_int((self.r * 255,
                                       self.g * 255,
                                       self.b * 255))

    _sort_method = _hue

    def __eq__(self, other):
        return self._sort_method() == other._sort_method()

    def __lt__(self, other):
        return self._sort_method() < other._sort_method()


    def __repr__(self):
        return f'Color(#{self.r}{self.g}{self.b})'

