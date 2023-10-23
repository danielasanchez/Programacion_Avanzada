# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
# Checkbutton
from tkinter import *

def obtener():
    print("El primer Checkbutton",op1.get())
    print("El segundo Checkbutton",op2.get())
    print("El tercero Checkbutton",op3.get())
    print("El cuarto Checkbutton",op4.get())
    op1.set(False)
    op2.set(False)
    op3.set(False)
    op4.set(False)


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")

#variable de control String, Int, Double, Boolean
op1=BooleanVar()#IntVar() 0 o 1
op2=BooleanVar()
op3=BooleanVar() 
op4=BooleanVar()
op1.set(True)


label1 = Label(principal, text="Respuesta:")
label1.pack()
label1.config(width=10,bg="gray",pady=20)


opcion1 = Checkbutton(principal,text="opcion 1",
                      bg="gray",variable=op1).pack()
opcion2 = Checkbutton(principal,text="opcion 2",
                      bg="gray",variable=op2).pack()
opcion3 = Checkbutton(principal,text="opcion 3",
                      bg="gray",variable=op3).pack()
opcion4 = Checkbutton(principal,text="opcion 4",
                      bg="gray",variable=op4).pack()



boton1 = Button(principal, text="Obtener", bg="gray",
                command=obtener,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.place(x=150,y=190)
boton1.config(pady=10,width=10)


principal.mainloop()

