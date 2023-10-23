# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""

from tkinter import *
from PIL import ImageTk, Image


def obtener():
    print(opcion.get())


def limpiar():
    opcion.set(None)

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x330+400+200")


opcion=IntVar() 



label1 = Label(principal, text="Respuesta:")
label1.pack()
label1.config(width=10,pady=20)

img1 = Image.open("Titulo1.png").resize((120,80))
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open("Homero.png").resize((120,100))
img2 = ImageTk.PhotoImage(img2)

img3 = Image.open("Titulo2.png").resize((120,70))
img3 = ImageTk.PhotoImage(img3)

img4 = Image.open("Philip.png").resize((100,100))
img4 = ImageTk.PhotoImage(img4)


opcion1 = Radiobutton(principal,text="opcion 1",
                      variable=opcion,value=1,
                      image=img1,selectimage=img2,
                      command=obtener).pack()
opcion2 = Radiobutton(principal,text="opcion 2",
                      variable=opcion,value=2,
                      image=img3,selectimage=img4,
                      command=obtener).pack()

boton1 = Button(principal, text="limpiar", bg="gray",
                command=limpiar,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.place(x=150,y=250)
boton1.config(pady=10,width=10)



principal.mainloop()

