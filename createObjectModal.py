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
        Button(self.pop, text="Ponto", width=5, command=lambda:self.levantar_frame(self.point_frame)).place(x=10, y=10)
        Button(self.pop, text="Linha", width=5, command=lambda:self.levantar_frame(self.line_frame)).place(x=10, y=40)
        Button(self.pop, text="Poligono", width=5, command=lambda:self.levantar_frame(self.poligono_frame)).place(x=10, y=70)

    def modal_ponto(self):
        self.point_frame = Frame(self.pop, bg="gray", borderwidth=1, relief="raised", width=300, height=300)
        self.point_frame.place(x=100, y=0) 
        Label(self.point_frame, bg="gray", text="Nome :").place(x=5, y=5)
        self.nome_point = Entry(self.point_frame, width=12)
        self.nome_point.place(x=52, y=5)
        Label(self.point_frame, bg="gray", text="X :").place(x=5, y=50)
        self.px = Entry(self.point_frame, width=5)
        self.px.place(x=25, y=50)
        Label(self.point_frame, bg="gray", text="Y :").place(x=100, y=50)
        self.py = Entry(self.point_frame, width=5)
        self.py.place(x=120, y=50)
        Button(self.point_frame, text="CONCLUIR", command=lambda:self.criar_ponto()).place(x=50, y=100)
        self.msg_label = Label(self.point_frame, text="", bg="gray")
        self.msg_label.place(x=10, y=150)

    def modal_linha(self):
        self.line_frame = Frame(self.pop, bg="gray", borderwidth=1, relief="raised", width=300, height=300)
        self.line_frame.place(x=100, y=0) 
        Label(self.line_frame, bg="gray", text="Nome :").place(x=2, y=5)
        self.nome_line = Entry(self.line_frame, width=12)
        self.nome_line.place(x=50, y=5)
        Label(self.line_frame, bg="gray", text="X1 :").place(x=2, y=50)
        self.lx1 = Entry(self.line_frame, width=5)
        self.lx1.place(x=30, y=50)
        Label(self.line_frame, bg="gray", text="Y1 :").place(x=97, y=50)
        self.ly1 = Entry(self.line_frame, width=5)
        self.ly1.place(x=125, y=50)
        Label(self.line_frame, bg="gray", text="X2 :").place(x=2, y=80)
        self.lx2 = Entry(self.line_frame, width=5)
        self.lx2.place(x=30, y=80)
        Label(self.line_frame, bg="gray", text="Y2 :").place(x=97, y=80)
        self.ly2 = Entry(self.line_frame, width=5)
        self.ly2.place(x=125, y=80)
        Button(self.line_frame, text="CONCLUIR", command=lambda:self.criar_linha()).place(x=50, y=150)
        self.msg_label2 = Label(self.line_frame, text="", bg="gray")
        self.msg_label2.place(x=10, y=180)

    def modal_poligono(self):
        self.poligono_frame = Frame(self.pop, bg="gray", borderwidth=1, relief="raised", width=300, height=300)
        self.poligono_frame.place(x=100, y=0) 
        Label(self.poligono_frame, bg="gray", text="Nome :").place(x=5, y=5)
        self.nome_poly = Entry(self.poligono_frame, width=12)
        self.nome_poly.place(x=52, y=5)
        Label(self.poligono_frame, bg="gray", text="X :").place(x=5, y=50)
        self.polx = Entry(self.poligono_frame, width=5)
        self.polx.place(x=25, y=50)
        Label(self.poligono_frame, bg="gray", text="Y :").place(x=100, y=50)
        self.poly = Entry(self.poligono_frame, width=5)
        self.poly.place(x=120, y=50)
        Button(self.poligono_frame, text="ADICIONAR", command=lambda:self.add_ponto_poligono()).place(x=0, y=100)
        Button(self.poligono_frame, text="CONCLUIR", command=lambda:self.criar_poligono()).place(x=100, y=100)
        self.msg_label3 = Label(self.poligono_frame, text="", bg="gray")
        self.msg_label3.place(x=10, y=150)

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

class CreateTransformModal():
    def __init__(self, interface):
        self.interface = interface

    def levantar_frame(self, frame:Frame, frame2:Frame = None, frame3:Frame = None,):
        frame.tkraise()
        if frame2:
            frame2.tkraise()
        if frame3:
            frame3.tkraise()

    def execute(self, obj):
        self.obj = obj
        self.pop = Toplevel(self.interface.main_window)
        self.pop.geometry("600x500+250+200")
        self.pop.title("Transformacoes")
        self.pop.config(bg="gray")
        
        self.modal_transformar()
        self.levantar_frame(self.transform_frame)

    def retorna_valores(self):
        self.interface.transformar((self.transladx.get(), self.translady.get()),(self.escalonax.get(), self.escalonay.get()), self.rotateang.get(), self.obj)


    def modal_transformar(self):
        self.transform_frame = Frame(self.pop, bg="gray", borderwidth=1, relief="raised", width=600, height=500)
        self.transform_frame.place(x=0, y=0) 
        Button(self.transform_frame, text="Executar transformacoes",command=self.retorna_valores, width=20).place(x=350, y=450)


        Label(self.transform_frame, bg="gray", text="ESCALONAMENTO").place(x=10, y=100)
        Label(self.transform_frame, bg="gray", text="X :").place(x=200, y=100)
        self.transladx = Entry(self.transform_frame, width=5)
        self.transladx.place(x=220, y=100)
        Label(self.transform_frame, bg="gray", text="Y :").place(x=300, y=100)
        self.translady = Entry(self.transform_frame, width=5)
        self.translady.place(x=320, y=100)

        Label(self.transform_frame, bg="gray", text="TRANSLACAO").place(x=10, y=200)
        Label(self.transform_frame, bg="gray", text="X :").place(x=200, y=200)
        self.escalonax = Entry(self.transform_frame, width=5)
        self.escalonax.place(x=220, y=200)
        Label(self.transform_frame, bg="gray", text="Y :").place(x=300, y=200)
        self.escalonay = Entry(self.transform_frame, width=5)
        self.escalonay.place(x=320, y=200)

        Label(self.transform_frame, bg="gray", text="ROTACAO").place(x=10, y=300)
        Label(self.transform_frame, bg="gray", text="Angulo").place(x=250, y=300)
        self.rotateang = Entry(self.transform_frame, width=5)
        self.rotateang.place(x=300, y=300)