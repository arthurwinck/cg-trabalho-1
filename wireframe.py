from tipos import Tipo, Obj

class Wireframe(Obj):
    def __init__(self, nome: str, tipo: Tipo, coord_list: list[tuple]) -> None:
        self.nome = nome
        self.tipo = tipo

        self.coord_list = self.init_coord_list(tipo, coord_list)
        
    def init_coord_list(self, tipo: Tipo, coord_list: list = None) -> list | None:
        if coord_list != None:
            return coord_list
        else:
            print("Wireframe não possui coordenadas próprias")
            return None