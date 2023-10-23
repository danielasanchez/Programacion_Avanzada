# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
# Checkbutton
from tkinter import *

def obtener():
    print(op1.get())
    print(op2.get())
    print(op3.get())
    print(op4.get())
    op1.set(0)
    op2.set(0)
    op3.set(0)
    op4.set(0)

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")

#variable de control String, Int, Double, Boolean
op1=IntVar()
op2=IntVar()
op3=IntVar()
op4=IntVar()
op1.set(1)



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

