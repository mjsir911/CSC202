#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

__appname__     = ""
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

import timeit
def time(func):
    name = func.__name__
    def time(*args, **kwargs):
        return timeit.timeit(setup='from __main__ import {}'.format(name),
                stmt='{}(*{}, **{})'.format(name, args, kwargs), number=1)
    func.time = time
    return func

#def time(func):

# 1) Devise an experiment to verify that the list index operator is O(1)
import random
import numpy
@time
def e1(l, i):
    l[i]

data = []
for k in range(10000):
    for i in range(1, 10):
        for j in range(i):
            t = e1.time([None] * i, j)
            data.append({'i': i, 'j': j, 'time': t})

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(
        xs=[d['i'] for d in data],
        ys=[d['j'] for d in data],
        zs=[d['time'] for d in data])
plt.show()
fig.show()



# 2) Devise an experiment to verify that get item and set item are O(1) for # dictionaries
# 3) Devise an experiment that compares the performance of the del operator on # lists and dictionaries
# 4) Given a list of numbers in random order, write a linear time algorthm to find
# the kth smallest number in the list. Explain why your algorithm is linear
# 5) Can you improve the algorithm from the previous problem to be O(n * log(n))
