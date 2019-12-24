from tkinter import *
from tkinter import ttk

class mainApp(Tk): # mainAPP es en si es una ventana y le ponemos que herede de Tk
    size = "480x340"# aqui podremos cambiarlo sin tener que cambiarlo en mas partes
    
    def __init__(self):
        Tk.__init__(self)
        
        #root es el nombre que elegimos, se peude poner lo que quieras
        self.geometry(self.size) #le damos tamaño a la ventana
        self.title("Mi ventana")
        self.configure(bg = "blue")
        
        def start(self):
            self.mainloop()

if __name__ == '__main__':
    app = mainApp()
    
    app.start()
    
#los controles visuales son widget
    #ttk.Button
    #ttk.Radiobutton
    #ttk.Entry
    #Tk lleva todos los metodos necesarios para poner widgets y relacionarlos
