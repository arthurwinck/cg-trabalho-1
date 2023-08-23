from tipos import Obj, Tipo

class Poligono(Obj):
    #coordenadas = [()]
    def __init__(self, nome, coordenadas):
        super().__init__(nome, "blue", Tipo.POLIGONO, coordenadas)
        #self.cor = "#7600d0"