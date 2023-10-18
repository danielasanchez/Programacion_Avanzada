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
    op1.set("desactivada")
    op2.set("desactivada")
    op3.set("desactivada")
    op4.set("desactivada")

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")

#variable de control String, Int, Double, Boolean
op1=StringVar()
op2=StringVar()
op3=StringVar()
op4=StringVar()
op1.set("desactivada")
op2.set("desactivada")
op3.set("desactivada")
op4.set("desactivada")

label1 = Label(principal, text="Respuesta:")
label1.pack()
label1.config(width=10,bg="gray",pady=20)


opcion1 = Checkbutton(principal,text="opcion 1",
                      bg="gray",variable=op1, 
                      onvalue="valor 1",offvalue="desactivada").pack()
opcion2 = Checkbutton(principal,text="opcion 2",
                      bg="gray",variable=op2, 
                      onvalue="valor 2",offvalue="desactivada").pack()
opcion3 = Checkbutton(principal,text="opcion 3",
                      bg="gray",variable=op3, 
                      onvalue="valor 3",offvalue="desactivada").pack()
opcion4 = Checkbutton(principal,text="opcion 4",
                      bg="gray",variable=op4, 
                      onvalue="valor 4",offvalue="desactivada").pack()



boton1 = Button(principal, text="Obtener", bg="gray",
                command=obtener,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.pack()#place(x=150,y=190)
boton1.config(pady=10,width=10)


principal.mainloop()

