#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from abc import ABCMeta, abstractmethod
from typing import Hashable, Type, TypeVar, Generic, List
import numbers

__appname__     = "abc"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

#LabelType = TypeVar('LabelType', bound=Hashable)
LabelType = TypeVar('LabelType')


class VertexMeta(Generic[LabelType], metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, label: LabelType) -> None:
        return NotImplemented


VertexType = VertexMeta[LabelType]


class GraphMeta(Generic[LabelType], metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        return NotImplemented

    @abstractmethod
    def add_vertex(self, vert: VertexType) -> None:
        return NotImplemented

    @abstractmethod
    def add_edge(self,
                 from_vert: VertexType,
                 to_vert: VertexType,
                 weight: numbers.Number
                 ) -> None:
        return NotImplemented

    @abstractmethod
    def get_vertex(self, key: LabelType) -> VertexType:
        return NotImplemented

    @abstractmethod
    def get_vertices(self) -> List[VertexType]:
        return NotImplemented

    @abstractmethod
    def __contains__(self, key: VertexType) -> bool:
        return NotImplemented
