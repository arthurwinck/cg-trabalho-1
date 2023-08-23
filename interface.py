from tkinter import *
from tkinter.ttk import Style
from createObjectModal import CreateObjectModal
from window import Window
from linha import Linha
from poligono import Poligono
import numpy as np

class Interface():
    def __init__(self) -> None:
        self.default_vw_size = 570
        self.objetos_dict = {}
        self.initialize()
        self.create_object_modal = CreateObjectModal(self)

    def initialize(self) -> None:
        self.create_main_window()
        self.create_menu()
        self.create_display_file()
        self.create_object_list()
        self.create_view_port()
        self.create_buttons()
        self.create_objects()
        self.redraw()

    def create_main_window(self) -> None:
        self.main_window = Tk()
        self.main_window.geometry("930x700+450+200")
        self.main_window.title("Sistema 2D")
        self.main_window["bg"]= "gray"

        style = Style()
        style.theme_use('alt')

    def create_menu(self) -> None:
        self.menubar = Menu(self.main_window)
        self.menubar.option_add("*tearOff", FALSE)
        self.main_window["menu"] = self.menubar
        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label="Menu")
        self.menu_file.add_command(label="Importar", command=self.importar)

    def set_tamanho_viewport(self) -> None:
        self.xvMin = 0
        self.xvMax = self.default_vw_size - (20 * 2)
        self.yvMin = 0
        self.yvMax = self.default_vw_size - (20 * 2)

        self.margem = 20

    def create_display_file(self) -> None:
        self.dFile_frame = Frame(self.main_window, borderwidth=1, relief="raised", bg="gray")
        self.dFile_frame.place(x=10, y=10, width=200, height=670)

    def create_object_list(self) -> None:
        self.scroll_frame = Frame(self.dFile_frame, bg="black")
        self.scroll_frame.place(x=170, y=20, height=120)
        self.movimento_frame = Frame(self.dFile_frame, bg="black")
        self.movimento_frame.place(x=170, y=20, height=120)
        self.objetos_texto = Label(self.dFile_frame, text="Objetos", bg="gray")
        self.objetos_texto.config(font =("Courier", 14), foreground="black")
        self.objetos_texto.pack()
        self.bara_rolagem = Scrollbar(self.movimento_frame, orient=VERTICAL)
        self.object_list = Listbox(self.dFile_frame, bg="gray40", yscrollcommand=self.bara_rolagem.set)
        self.scrollbar = Scrollbar(self.scroll_frame, orient=VERTICAL)
        #listbox contendo os objetos criados
        self.object_list = Listbox(self.dFile_frame, bg="gray40", yscrollcommand=self.scrollbar.set) 
        #dicionario para que tenhamos uma referencia aos objetos
        self.scrollbar.config(command=self.object_list.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.object_list.place(x=10, y=20, width=155 , height=125)

    def create_view_port(self) -> None:
    
        self.canvas = Canvas(self.main_window, width=570, height=570, bg="floral white")
        self.canvas.place(x=230, y=10)
        
        self.set_tamanho_viewport()

        self.window = Window("Window", [(-11,-11,-5),(11,-11,-5),(11,11,-5),(-11,11,-5)])

        self.eixo_x = Linha("x", [(-1,0), (1,0)] )
        self.eixo_y = Linha("y", [(0,-1), (0, 1)])

        self.objetos_dict["eixo_x"] = self.eixo_x
        self.objetos_dict["eixo_y"] = self.eixo_y

    def create_objects(self) -> None:
        poligono = Poligono(nome="teste", coordenadas=[(0,0.1), (0.1, 0), (0.1, 0.1)])
        self.object_list.insert(END, poligono.nome)
        self.objetos_dict["teste"] = poligono

    def create_buttons(self) -> None:
        ################# bottoes de adicionar e deletar ##################
        self.botao_add = Button(self.dFile_frame, text="Adicionar", command=lambda:self.create_object_modal.execute())
        self.botao_add.place(x=30, y=155, width=60)

        self.botao_del = Button(self.dFile_frame, text="Apagar", command= lambda:self.apagar_objeto())
        self.botao_del.place(x=110, y=155, width=60)

        ####################botoes de movimento da window####################
        self.botao_del = Button(self.dFile_frame, text="<", command=lambda:self.left())
        self.botao_del.place(x=30, y=235, width=40)

        self.botao_del = Button(self.dFile_frame, text=">", command=lambda:self.right())
        self.botao_del.place(x=130, y=235, width=40)

        self.botao_del = Button(self.dFile_frame, text="^", command=lambda:self.up())
        self.botao_del.place(x=80, y=200, width=40)

        self.botao_del = Button(self.dFile_frame, text="v", command=lambda:self.down())
        self.botao_del.place(x=80, y=270, width=40)

        ######################botoes de zoom######################
        self.botao_del = Button(self.dFile_frame, text="Zoom --", command=lambda:self.zoom_out())
        self.botao_del.place(x=30, y=315, width=60)

        self.botao_del = Button(self.dFile_frame, text="Zoom ++", command=lambda:self.zoom_in())
        self.botao_del.place(x=110, y=315, width=60)

    def importar(self) -> None:
        pass

    def redraw(self) -> None:
        #primeiro apaga tudo
        self.canvas.delete("all") 

        #redesenha os eixos 
        # self.canvas.create_line(self.xvp(self.eixo_x.coordenadas[0][0]), self.yvp(self.eixo_x.coordenadas[0][1]), self.xvp(self.eixo_x.coordenadas[1][0]), self.yvp(self.eixo_x.coordenadas[1][1]), fill="red", width=3)
        # self.canvas.create_line(self.xvp(self.eixo_y.coordenadas[0][0]), self.yvp(self.eixo_y.coordenadas[0][1]), self.xvp(self.eixo_y.coordenadas[1][0]), self.yvp(self.eixo_y.coordenadas[1][1]), fill="green", width=3)

        #Desenha a zona do canvas
        self.canvas.create_line(self.xvMin+self.margem, self.yvMin+self.margem ,self.xvMax+self.margem, self.yvMin+self.margem, fill="red", width=3) #Horizontal cima
        self.canvas.create_line(self.xvMax+self.margem, self.yvMin+self.margem, self.xvMax+self.margem, self.yvMax+self.margem, fill="red", width=3) #Vertical direita
        self.canvas.create_line(self.xvMin+self.margem, self.yvMax+self.margem, self.xvMax+self.margem, self.yvMax+self.margem, fill="red", width=3) #Horizontal baixo
        self.canvas.create_line(self.xvMin+self.margem, self.yvMin+self.margem, self.xvMin+self.margem, self.yvMax+self.margem, fill="red", width=3)

        for key, obj in self.objetos_dict.items():
            self.draw(obj)

    def xvp(self, xw):
        return ( ((xw-(-1))/(1-(-1)))*(self.xvMax-self.xvMin) + self.margem)
    
    def yvp(self, yw):
        return ( (1-((yw-(-1))/(1-(-1))))*(self.yvMax-self.yvMin) + self.margem)

    def left(self):
        self.move((0.1,0,0))
        
    def right(self):
        self.move((-0.1,0,0))

    def up(self):
        self.move((0,-0.1,0))

    def down(self):
        self.move((0,0.1,0))

    def move(self, vetor):
        matriz = self.transladar2D(vetor[0], vetor[1])
        self.window.mover_xy(matriz)
        self.update(matriz)
        self.redraw()

    def transladar2D(self, dx, dy):
        return np.matrix([[1,0,0], [0,1,0], [dx,dy,1]])

    def escalonar2D(self, sx, sy):
        return np.matrix([[sx,0,0], [0,sy,0], [0,0,1]])

    def draw(self, obj):
        tup = obj.coordenadas
            
        if obj.tipo.value == 1: #se ponto
                self.canvas.create_oval(self.xvp(tup[0][0])-3, self.yvp(tup[0][1])-3, self.xvp(tup[0][0])+3, self.yvp(tup[0][1])+3, fill=obj.cor)

        elif obj.tipo.value == 2: #se linha
                self.canvas.create_line(self.xvp(tup[0][0]), self.yvp(tup[0][1]), self.xvp(tup[1][0]), self.yvp(tup[1][1]), fill=obj.cor, width=3)

        elif obj.tipo.value == 3: #se poligono
            for i in range (len(tup)-1):
                if tup[i] and tup[i+1]:
                    self.canvas.create_line(self.xvp(tup[i][0]), self.yvp(tup[i][1]), self.xvp(tup[i+1][0]), self.yvp(tup[i+1][1]), fill=obj.cor, width=3)
                self.canvas.create_line(self.xvp(tup[i+1][0]), self.yvp(tup[i+1][1]), self.xvp(tup[0][0]), self.yvp(tup[0][1]), fill=obj.cor, width=3)
                

    def update(self, matriz):
        for key, obj in self.objetos_dict.items():
            obj.mover_xy(matriz)

    def pegar_escala(self):
        self.window.escala_x = abs(self.windowObj.coordenadas[1][0] - self.windowObj.coordenadas[0][0]) #BD - BE (x)
        self.window.escala_y = abs(self.windowObj.coordenadas[3][1] - self.windowObj.coordenadas[0][1]) #CE - BE (y)

    def zoom_in(self):
        matriz = self.escalonar2D(1.1, 1.1)
        self.window.mover_xy(matriz)
        self.update(matriz)
        self.redraw()

    def zoom_out(self):
        matriz = self.escalonar2D(0.9, 0.9)
        self.window.mover_xy(matriz)
        self.update(matriz)
        self.redraw()

    def apagar_objeto(self):
        for linha in self.object_list.curselection():  
            del self.objetos_dict[self.object_list.get(linha)] 
            self.object_list.delete(linha)
        self.redraw()