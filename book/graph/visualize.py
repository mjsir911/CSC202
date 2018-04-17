#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import matplotlib.pyplot as plt

__appname__     = "visualize"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

x1, x2 = 1, 2
y1, y2 = 3, 4

from parse import start_point
x, y = start_point.label

already_drawn = set()
def recursive_draw(point):
    x1, y1 = point.label
    plt.scatter([x1], [-y1])
    for connection in point.connections:
        x2, y2 = connection.label
        args = ((x1, x2), (-y1, -y2))
        if args in already_drawn:
            continue
        already_drawn.add(args)
        recursive_draw(connection)

        plt.plot(*args)

recursive_draw(start_point)

plt.ylabel('some numbers')
plt.show()
