from enum import Enum
from abc import ABC, abstractmethod
import numpy as np

class Tipo(Enum):
    PONTO = 1
    LINHA = 2
    POLIGONO = 3
    WINDOW = 4

class Obj(ABC):

    @abstractmethod
    def __init__(self, nome : str, cor : str, tipo : Tipo, coordenadas : list):
        self._nome = nome
        self._cor = cor
        self._tipo = tipo
        self._coordenadas = coordenadas

    def mult_pontos_matriz(self, mat):
        res = []
        for i in self.coordenadas:
            x = i[0]
            y = i[1]
            ponto = [float(x),float(y), float(1)]
            result = np.matmul(ponto, mat)
            res.append((result.item(0),result.item(1)))
        return res

    def mover_xy(self, mat: np.matrix):
        self.coordenadas = self.mult_pontos_matriz(mat)
        #print(self.coordenadas)

    def normalize(self, mat: np.matrix):
        pass

    @property
    def nome(self):
        return self._nome
    
    @property
    def cor(self):
        return self._cor
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def coordenadas(self):
        return self._coordenadas
    
    @nome.setter
    def nome(self, nome : str):
        self._nome = nome

    @coordenadas.setter
    def coordenadas(self, coordenadas : list):
        self._coordenadas = coordenadas

    @cor.setter
    def cor(self, cor: str):
        self._cor = cor