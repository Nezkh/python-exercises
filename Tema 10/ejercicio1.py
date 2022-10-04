from tkinter import *
from tkinter.ttk import *

def seleccion():
    monitor.config(text="Elegiste la opción {}" .format(opcion.get()))
    
def reset():
    opcion.set(None)
    monitor.config(text="")
    
root = Tk()
root.geometry("200x200")
opcion = IntVar()
opcion.set(None)

Radiobutton(root, text="Opción 1", variable=opcion, value=1, command=seleccion).pack(anchor= W)
Radiobutton(root, text="Opción 2", variable=opcion, value=2, command=seleccion).pack(anchor= W)
Radiobutton(root, text="Opción 3", variable=opcion, value=3, command=seleccion).pack(anchor= W)
Radiobutton(root, text="Opción 4", variable=opcion, value=4, command=seleccion).pack(anchor= W)

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack(anchor=S)

root.mainloop()