#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

__appname__     = "mygraph"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

import myabc

from typing import Generic, TypeVar


class Graph(myabc.GraphMeta):
    def __init__(self):
        self.data = dict()

    def adjacent(self, vert1, vert2):
        return vert2 in vert1.connections

    def add_vertex(self, vert):
        self.data[vert.label] = vert

    def add_edge(self, from_vert, to_vert, weight):
        from_vert(to_vert, weight)

    def get_vertex(self, key):
        return self.data[key]

    def get_vertices(self):
        return set(self.data.items())

    def __contains__(self, key):
        return key in self.data.items()


class Vertex():
    def __init__(self, label):
        self.label = label
        self.connections = {}

    def __call__(self, other, weight):
        self.connections[other] = weight

    def __repr__(self):
        return 'Vertex({})'.format(self.label)
