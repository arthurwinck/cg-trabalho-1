from tkinter import *
from poligono import Poligono
from linha import Linha
from ponto import Ponto

class CreateObjectModal():
    def __init__(self, interface):
        self.interface = interface
        self.pontos_poligono = []

    def levantar_frame(self, frame:Frame, frame2:Frame = None, frame3:Frame = None, zerar = True):
        if zerar:
            self.pontos_poligono = []
        frame.tkraise()
        if frame2:
            frame2.tkraise()
        if frame3:
            frame3.tkraise()

    def execute(self) -> None:
        self.pop = Toplevel(self.interface.main_window)
        self.pop.geometry("400x300+450+200")
        self.pop.title("Criar novo objeto")
        self.pop.config(bg="gray")

        self.modal_ponto()
        self.modal_linha()
        self.modal_poligono()

        #Botoes para selecionar qual objeto adicionar
        Button(self.pop, text="Ponto", width=10, command=lambda:self.levantar_frame(self.point_frame)).place(x=10, y=10)
        Button(self.pop, text="Linha", width=10, command=lambda:self.levantar_frame(self.line_frame)).place(x=10, y=40)
        Button(self.pop, text="Poligono", width=10, command=lambda:self.levantar_frame(self.poligono_frame)).place(x=10, y=70)

    def modal_ponto(self):
        self.point_frame = Frame(self.pop, bg="gray", borderwidth=1, relief="raised", width=300, height=300)
        self.point_frame.place(x=100, y=0) 
        Label(self.point_frame, bg="gray", text="Ponto", font=("Courier", 14)).place(x=100, y=20)
        Label(self.point_frame, bg="gray", text="Nome :").place(x=30, y=70)
        self.nome_point = Entry(self.point_frame, width=12)
        self.nome_point.place(x=80, y=70)
        Label(self.point_frame, bg="gray", text="X :").place(x=40, y=120)
        self.px = Entry(self.point_frame, width=5)
        self.px.place(x=60, y=120)
        Label(self.point_frame, bg="gray", text="Y :").place(x=120, y=120)
        self.py = Entry(self.point_frame, width=5)
        self.py.place(x=140, y=120)
        Button(self.point_frame, text="CONCLUIR", command=lambda:self.criar_ponto()).place(x=170, y=180)
        self.msg_label = Label(self.point_frame, text="", bg="gray")
        self.msg_label.place(x=20, y=260)

    def modal_linha(self):
        self.line_frame = Frame(self.pop, bg="gray", borderwidth=1, relief="raised", width=300, height=300)
        self.line_frame.place(x=100, y=0) 
        Label(self.line_frame, bg="gray", text="Linha", font=("Courier", 14)).place(x=90, y=20)
        Label(self.line_frame, bg="gray", text="Nome :").place(x=30, y=70)
        self.nome_line = Entry(self.line_frame, width=12)
        self.nome_line.place(x=80, y=70)
        Label(self.line_frame, bg="gray", text="X1 :").place(x=40, y=110)
        self.lx1 = Entry(self.line_frame, width=5)
        self.lx1.place(x=60, y=110)
        Label(self.line_frame, bg="gray", text="Y1 :").place(x=120, y=110)
        self.ly1 = Entry(self.line_frame, width=5)
        self.ly1.place(x=140, y=110)
        Label(self.line_frame, bg="gray", text="X2 :").place(x=40, y=150)
        self.lx2 = Entry(self.line_frame, width=5)
        self.lx2.place(x=60, y=150)
        Label(self.line_frame, bg="gray", text="Y2 :").place(x=120, y=150)
        self.ly2 = Entry(self.line_frame, width=5)
        self.ly2.place(x=140, y=150)
        Button(self.line_frame, text="CONCLUIR", command=lambda:self.criar_linha()).place(x=170, y=190)
        self.msg_label2 = Label(self.line_frame, text="", bg="gray")
        self.msg_label2.place(x=20, y=260)

    def modal_poligono(self):
        self.poligono_frame = Frame(self.pop, bg="gray", borderwidth=1, relief="raised", width=300, height=300)
        self.poligono_frame.place(x=100, y=0) 
        Label(self.poligono_frame, bg="gray", text="Poligono", font=("Courier", 14)).place(x=90, y=20)
        Label(self.poligono_frame, bg="gray", text="Nome :").place(x=30, y=70)
        self.nome_poly = Entry(self.poligono_frame, width=12)
        self.nome_poly.place(x=80, y=70)
        Label(self.poligono_frame, bg="gray", text="X :").place(x=40, y=120)
        self.polx = Entry(self.poligono_frame, width=5)
        self.polx.place(x=60, y=120)
        Label(self.poligono_frame, bg="gray", text="Y :").place(x=120, y=120)
        self.poly = Entry(self.poligono_frame, width=5)
        self.poly.place(x=140, y=120)
        Button(self.poligono_frame, text="ADICIONAR", command=lambda:self.add_ponto_poligono()).place(x=40, y=180)
        Button(self.poligono_frame, text="CONCLUIR", command=lambda:self.criar_poligono()).place(x=170, y=180)
        self.msg_label3 = Label(self.poligono_frame, text="", bg="gray")
        self.msg_label3.place(x=20, y=260)

    def add_ponto_poligono(self):
        #try:
        x = float(self.polx.get()) #cuida que x e y nao recebeu entrada de string
        y = float(self.poly.get())
        self.pontos_poligono.append((x,y))
        self.msg_label3.config(text="Ponto adicionado!", foreground="SpringGreen2")


    def criar_poligono(self):
        nome = self.nome_poly.get()
        if not (nome in self.interface.objetos_dict.keys()):
            self.interface.object_list.insert(END, nome)
            pontos = self.pontos_poligono[:] 
            self.interface.objetos_dict[nome] = Poligono(nome, pontos)
            self.pontos_poligono = []
            self.interface.redraw()
            self.msg_label3.config(text="Polígono criado!", foreground="SpringGreen2")
        else:
            self.msg_label3.config(text="Nome já existente!", foreground="red")

    def criar_linha(self):
        nome = self.nome_line.get()
        if not (nome in self.interface.objetos_dict.keys()):
            x1 = float(self.lx1.get())
            y1 = float(self.ly1.get())

            x2 = float(self.lx2.get())
            y2 = float(self.ly2.get())

            self.interface.object_list.insert(END, nome)                
            self.interface.objetos_dict[nome] = Linha(nome, [(x1,y1),(x2,y2)])
            self.interface.redraw()
            self.msg_label2.config(text="Linha adicionada!", foreground="SpringGreen2")
        else:
            self.msg_label2.config(text="Nome já existente!", foreground="red")

    def criar_ponto(self):
        nome = self.nome_point.get()
        if not (nome in self.interface.objetos_dict.keys()):         #verifica se nao tem o objeto com mesmo nome 
            x = float(self.px.get())            #cuida que x e y nao recebeu entrada de string
            y = float(self.py.get())
            self.interface.object_list.insert(END, nome)         #insere o nome do objeto na listbox
            self.interface.objetos_dict[nome] = Ponto(nome, [(x,y)]) #adiciona o ponto no dicionario de objetos, chave = nome
            self.interface.redraw()
            self.msg_label.config(text="Ponto adicionado!", foreground="SpringGreen2")
        else:
            self.msg_label.config(text="Nome já existente!", foreground="red")

