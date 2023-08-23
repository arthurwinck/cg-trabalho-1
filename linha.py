from tipos import Obj, Tipo
from numpy import matrix

class Linha(Obj):
    
    def __init__(self, nome: str, cor: str, tipo: Tipo, coordenadas: list):
        super().__init__(nome, cor, tipo, coordenadas)
        self.esta_na_window = bool


    