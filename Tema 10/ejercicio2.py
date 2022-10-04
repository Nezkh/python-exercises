from cProfile import label
from cgitb import text
from tkinter import *

master = Tk()
master.geometry("200x300")
    
listbox = Listbox(master)
for item in ["Japon", "Tailandia", "China", "Italia", "Francia", "Estados Unidos", "Mexico"]:
    listbox.insert(END, item)

tit = Label(text="Elige el pais donde te gustaría viajar")
tit.pack()

listbox.pack()

master.mainloop()