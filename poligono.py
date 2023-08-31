from tipos import Obj, Tipo
import numpy as np

class Poligono(Obj):
    #coordenadas = [()]
    def __init__(self, nome, coordenadas):
        super().__init__(nome, "blue", Tipo.POLIGONO, coordenadas)
        self.centro = self.calcular_centro2d()
        #self.cor = "#7600d0"

    def calcular_centro2d(self) -> None:
        tam = float(len(self.coordenadas))

        lista_x = list(map(lambda x: x[0], self.coordenadas))
        lista_y = list(map(lambda y: y[1], self.coordenadas))

        centro_x = float(sum(lista_x))
        centro_y = float(sum(lista_y))

        return (centro_x/tam, centro_y/tam)

    def mover_xy(self, mat: np.matrix):
        self.coordenadas = self.mult_pontos_matriz(mat)
        self.centro = self.calcular_centro2d()