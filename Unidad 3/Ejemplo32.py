# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
# Listbox
from tkinter import *

def obtener():
    #elementos seleccionados
    print(carrera.curselection())
    selec=carrera.curselection()
    print(carrera.get(selec[0]))
    # carrera.delete(2,END)
    


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")


label1 = Label(principal, text="Respuesta:")
label1.pack()
label1.config(width=10,bg="gray",pady=20)

# selectmode: browse, single, multiple, extended
carrera = Listbox(principal,height=5,selectmode=BROWSE)
carrera.insert(1,"LNI")
carrera.insert(2,"LC")
carrera.insert(3,"LA")
carrera.insert(0,"LIN")

carrera.pack()

print("la cantidad de opciones es: ",carrera.size())
#elementos
print("las opciones son: ",carrera.get(0,END))

boton1 = Button(principal, text="Obtener", bg="gray",
                command=obtener,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.place(x=150,y=190)
boton1.config(pady=10,width=10)


principal.mainloop()

