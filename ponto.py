import numpy as np
from tipos import Obj, Tipo

class Ponto(Obj):
    def __init__(self, nome, coordenadas):
        super().__init__(nome, "green", Tipo.PONTO, coordenadas)