#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

__appname__     = "__main__"
__author__      = "@AUTHOR@"
__copyright__   = ""
__credits__     = ["@AUTHOR@"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "@AUTHOR@"
__email__       = "@EMAIL@"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

from pauser import IncrementalSorter
from sorts import sorting_algorithms, insertionSort
from sys import argv
from colors import Color
import random

sortfunc = sorting_algorithms.get(argv[1], insertionSort) if len(argv) > 1 else insertionSort

import numpy as np

height = 1
width = 300
mul = 5
screenarray = [Color(random.randint(0, 0xFFFFFF)) for _ in range(width)]


def scaleup(a):
    return np.kron(a, np.ones((mul, mul)))

import pygame
pygame.init()
scale = 7
from pygame.locals import *
screen = pygame.display.set_mode((width * mul, height * mul), DOUBLEBUF | HWSURFACE)
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

import time
for state in IncrementalSorter(sortfunc, screenarray):
    time.sleep(0.001)
    state = [int(c) for c in state]
    state = np.array([state])
    state = np.transpose(state)
    state = scaleup(state)
    pygame.surfarray.blit_array(screen, state)
    pygame.display.flip()
