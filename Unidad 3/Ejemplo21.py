# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""

from tkinter import *

def obtener():
    print(opcion.get())


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")

opcion=IntVar() 
opcion.set(4)


label1 = Label(principal, text="Respuesta:")
label1.pack()
label1.config(width=10,bg="gray",pady=20)


opcion1 = Radiobutton(principal,text="opcion 1",
                      bg="gray",variable=opcion,value=1,
                      command=obtener).pack()
opcion2 = Radiobutton(principal,text="opcion 2",
                      bg="gray",variable=opcion,value=2,
                      command=obtener).pack()
opcion3 = Radiobutton(principal,text="opcion 3",
                      bg="gray",variable=opcion,value=3,
                      command=obtener).pack()
opcion4 = Radiobutton(principal,text="opcion 4",
                      bg="gray",variable=opcion,value=4,
                      command=obtener).pack()


principal.mainloop()

