#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import pygame
import numpy as np
import sorts

__appname__     = "__main__"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""


def scaleup(a, scale):
    return np.kron(a, np.ones((scale, scale)))


pygame.init()
from pygame.locals import *
flags = DOUBLEBUF | HWSURFACE
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

size = np.array((0xFF + 0x00, 0xF))
scale = 5

screen = pygame.display.set_mode(size * scale, flags)

screenarray = np.random.randint(0, 0xFFFFFF, size)

pygame.surfarray.blit_array(screen, scaleup(screenarray, scale))


import sorts
import sys

sortfunc = sorts.sorting_algorithms.get(sys.argv[1], sorts.insertionSort) if len(sys.argv) > 1 else sorts.insertionSort

def wrapfunc(func, *args):
    import time
    #time.sleep(3)
    func(*args)

old_array = screenarray.copy()


import colors
colors.step = False

import threading
threads = [threading.Thread(target=wrapfunc, args=(sortfunc, y)) for y in
        screenarray.T]

for thread in threads:
    thread.start()

from time import sleep
while True:
    colors.step = True
    sleep(0.000001)
    colors.step = False
    pygame.surfarray.blit_array(screen, scaleup(screenarray, scale))
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
