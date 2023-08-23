from tkinter import *
from tkinter.ttk import Style
from wireframe import Wireframe
from tipos import Obj
from window import Window

class Interface():
    def __init__(self) -> None:
        self.create_main_window()
        self.create_menu()
        self.create_view_port()

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
        self.menu_file.add_command(label="Importar", command=self.teste)

    # Teste para command do menu_file
    def teste(self):
        pass

    def create_view_port(self):
        #relief opcoes: solid, flat, raised, sunken
        #Frame das opcoes escontradas na esquerda da tela
        self.dFile_frame = Frame(self.main_window, borderwidth=1, relief="raised", bg="gray")
        self.dFile_frame.place(x=10, y=10, width=200, height=670)

        #canvas referente a viewport
        self.canvas = Canvas(self.main_window, width=570, height=570, bg="floral white")
        self.canvas.place(x=230, y=10)
        
        self.obj_dict = {}
        
        #margem para area de clipping
        self.margem = 20 

        #tamanho da tela do viewport (canvas)
        self.xvMin = 0   #0
        self.xvMax = 570 -(self.margem*2) #570 é nosso padrao do canvas,
        self.yvMin = 0   #0                    a margem x2 é para tratar ambos lados
        self.yvMax = 570 -(self.margem*2) #570

        self.windowObj = Window("Window", [(-11,-11,-5),(11,-11,-5),(11,11,-5),(-11,11,-5)])


        ####################tela onde sao listados os objetos####################
        self.movimento_frame = Frame(self.dFile_frame, bg="black")
        self.movimento_frame.place(x=170, y=20, height=120)
        self.objetos_texto = Label(self.dFile_frame, text="Objetos", bg="gray")
        self.objetos_texto.config(font =("Courier", 14), foreground="black")
        self.objetos_texto.pack()
        self.bara_rolagem = Scrollbar(self.movimento_frame, orient=VERTICAL)
        #self.object_list = Listbox(self.dFile_frame, bg="gray40", yscrollcommand=self.bara_rolagem.set)
        
        ####################botoes de controle dos objetos####################
        self.botao_add = Button(self.dFile_frame, text="Adicionar")
        self.botao_add.place(x=30, y=155, width=60)

        self.botao_del = Button(self.dFile_frame, text="Apagar")
        self.botao_del.place(x=110, y=155, width=60)

        ####################botoes de movimento da window####################
        self.botao_del = Button(self.dFile_frame, text="<")
        self.botao_del.place(x=30, y=235, width=40)

        self.botao_del = Button(self.dFile_frame, text=">")
        self.botao_del.place(x=130, y=235, width=40)

        self.botao_del = Button(self.dFile_frame, text="^")
        self.botao_del.place(x=80, y=200, width=40)

        self.botao_del = Button(self.dFile_frame, text="v")
        self.botao_del.place(x=80, y=270, width=40)

        ######################botoes de zoom######################
        self.botao_del = Button(self.dFile_frame, text="Zoom --")
        self.botao_del.place(x=30, y=315, width=60)

        self.botao_del = Button(self.dFile_frame, text="Zoom ++")
        self.botao_del.place(x=110, y=315, width=60)


if __name__ == "__main__":
    interface = Interface()
    interface.main_window.mainloop()
