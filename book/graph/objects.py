#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from typing import List
import myabc

__appname__     = "objects"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""


class Vertex():
    def __init__(self, label):
        self.label = label

    def __hash__(self):
        return hash(self.label)


class Graph(set):
    def adjacent(self, v1: Vertex, v2: Vertex) -> bool:
        """
        Tests for edge between vertex 1 and vertex 2
        """

    def neighbors(self, v: Vertex) -> List[Vertex]:
        """
        List all vertices y such that there is an edge from the vertex v to the
        vertex y
        """

    def add_vertex(self, v: Vertex) -> None:
        """
        Add the vertex v, if it is not there
        """

    def remove_vertex(self, v: Vertex) -> None:
        """
        Add the vertex v, if it is not there
        """

    def add_edge(self, v1: Vertex, v2: Vertex) -> None:
        """
        Add edge from vertex v1 to vertex v2, if it is not there
        """

    def remove_edge(self, v1, v2) -> None:
        """
        Remove edge from vertex v1 to vertex v2, if it is there
        """

class Test(myabc.GraphMeta):
    pass

print(Test.get_vertex.__annotations__)
