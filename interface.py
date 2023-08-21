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


if __name__ == "__main__":
    interface = Interface()
    interface.main_window.mainloop()
