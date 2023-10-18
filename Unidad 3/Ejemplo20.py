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

#variable de control Strin, Int, Double, Boolean
opcion=IntVar() 
#se le establece una opcion por default
opcion.set(4)


label1 = Label(principal, text="Respuesta:")
label1.pack()
label1.config(width=10,bg="gray",pady=20)


opcion1 = Radiobutton(principal,text="opcion 1",
                      bg="gray",variable=opcion,value=1).pack()
opcion2 = Radiobutton(principal,text="opcion 2",
                      bg="gray",variable=opcion,value=2).pack()
opcion3 = Radiobutton(principal,text="opcion 3",
                      bg="gray",variable=opcion,value=3).pack()
opcion4 = Radiobutton(principal,text="opcion 4",
                      bg="gray",variable=opcion,value=4).pack()



boton1 = Button(principal, text="Obtener", bg="gray",
                command=obtener,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.place(x=150,y=190)
boton1.config(pady=10,width=10)


principal.mainloop()

