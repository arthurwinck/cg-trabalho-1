from enum import Enum
from abc import ABC, abstractmethod

class Tipo(Enum):
    PONTO = 1
    LINHA = 2
    POLIGONO = 3

class Obj(ABC):

    @abstractmethod
    def __init__(self, nome : str, cor : str, tipo : Tipo, coordenadas : list):
        self.nome = nome
        self.cor = cor
        self.tipo = tipo
        self.coordenadas = coordenadas

    @property
    def nome(self):
        return self.nome
    
    @property
    def cor(self):
        return self.cor
    
    @property
    def tipo(self):
        return self.tipo
    
    @property
    def coordenadas(self):
        return self.coordenadas
    
    @nome.setter
    def nome(self, nome : str):
        self.nome = nome

    @coordenadas.setter
    def coordenadas(self, coordenadas : list):
        self.coordenadas = coordenadas