# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""

from tkinter import *

def obtener():
    texto=text1.get(1.0,END)
    print(texto)
    text1.delete(1.0,END)


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")

label1 = Label(principal, text="Respuesta:")
label1.place(x=50,y=60)
label1.config(width=10,bg="gray")


text1 = Text(principal, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green")
# height = lineas
# width = caracteres
# wrap = WORD ,  CHAR o NONE
text1.config(height=4,width=20,wrap=NONE)
text1.place(x=130,y=60)

#r.c o END
text1.insert(1.0,"Hola mundo")


boton1 = Button(principal, text="Obtener", bg="gray",
                command=obtener,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.place(x=170,y=180)
boton1.config(pady=10,width=10)


principal.mainloop()

