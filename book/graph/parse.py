#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from mygraph import Graph, Vertex
import math

__appname__     = "parse"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""


TURTLE = 'S'


def load_maze(fp):
    maze = [list(line[:-1]) for line in fp]

    for y, row in enumerate(maze):
        for x, column in enumerate(row):
            if column == TURTLE:
                return x, y, maze

    return None, maze


DIRECTION = [(int(math.sin(i / 2 * math.pi)), int(math.cos(i / 2 * math.pi)))
             for i in range(4)]


def make_graph_from_maze(coordinate, maze, graph=Graph()):
    x, y = coordinate
    path = maze[y][x]
    cur_vertex = Vertex(coordinate)

    if path == '+':
        return (None, graph)

    if coordinate in graph.data:
        return graph.get_vertex(coordinate), graph

    if x < 0 or y < 0 or x > len(maze[0]) or y > len(maze):
        return Vertex('GOAAAAAAL'), graph

    graph.add_vertex(cur_vertex)

    for x_offset, y_offset in DIRECTION:

        other_vertex, _ = make_graph_from_maze((x + x_offset, y + y_offset),
                                               maze,
                                               graph)
        if other_vertex is not None:
            graph.add_edge(cur_vertex, other_vertex, 1)

    return cur_vertex, graph


# start_point, graph = make_graph_from_maze(turtle_coords, maze)
