from tipos import Obj, Tipo
import numpy as np

class Linha(Obj):
    def __init__(self, nome, coordenadas):
        super().__init__(nome, "black", Tipo.LINHA, coordenadas)
        #self.cor = "#0000ff"