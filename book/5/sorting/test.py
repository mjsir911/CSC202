#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import pygame
import numpy as np

__appname__     = "test"
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
    return np.kron(a, np.ones(scale))


if __name__ == '__main__':
    pygame.init()
    size = np.array((1000, 200))
    scale = 1

    screenarray = np.random.randint(0, 0xFFFFFF, (size[0], 1)) & 0xFFFFFF
    # screenarray = np.array([np.arange(0, 0xFFFFFF, 0xF0F0F0).T]).T
    # size[0] = len(screenarray)

    screen = pygame.display.set_mode((size[0] * scale, size[1]))

    pygame.surfarray.blit_array(screen, scaleup(screenarray, (scale, size[1])))

    pygame.display.flip()

    import sorts
    sortfunc = sorts.shellSort
    sortqueue = [sortfunc(y) for y in screenarray.T]

    for cur_sort in sortqueue:
        for _ in cur_sort:
            pass
    pygame.surfarray.blit_array(screen, scaleup(screenarray, (scale, size[1])))
    pygame.display.flip()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
