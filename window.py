from tipos import Obj
from tkinter import *
from tipos import Tipo

class Window(Obj):
    def __init__(self, nome, coordenadas=[(-10,-10,0), (10,-10,0), (10,10,0), (-10,10,0)]):
        super().__init__("window", "gray", Tipo.WINDOW, coordenadas)
        self.escala_x = float()
        self.escala_y = float()