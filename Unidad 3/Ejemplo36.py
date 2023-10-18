# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#TopLevel

from tkinter import *

def ventanita():
    # revisar propiedades de bg, bd, etc.
    ventana = Toplevel(principal)
    ventana.title("Mi ventanita")
    ventana.geometry("180x80+500+300")
    # minsize(x,y)
    # maxsize(x,y)
    ventana.resizable(0,0)
    # Deshabilita las otras ventanas (Modal)
    ventana.grab_set()
    # aparece delante de la principal
    ventana.transient(master=principal)
    # podemos agregar widgets
    label1 = Label(ventana, text="Soy una etiqueta")
    label1.pack()
    input1 = Entry(ventana, highlightthickness=4, highlightcolor="blue",
                   selectbackground="pink", selectforeground = "green")
    input1.pack()

    
principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")


boton1 = Button(principal, text="ver", bg="gray",
                command=ventanita,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.pack()#place(x=150,y=190)
boton1.config(pady=10,width=10)


principal.mainloop()

