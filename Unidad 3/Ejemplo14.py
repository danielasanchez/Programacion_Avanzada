# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:48:54 2023

@author: Daniela Sánchez
"""

from tkinter import *

def mifuncion():
    print("Ya le diste :(")

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("800x500+400+200")

#activebackground
#activeforeground
#command
#state (DISABLED/ACTIVE)
boton1 = Button(principal, text="No darle click", bg="gray",
                command=mifuncion,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.place(x=250,y=150)
boton1.config(padx=20,pady=20)

boton2 = Button(principal, text="Tampoco", bg="gray",
                command=principal.destroy,
                activebackground="red",
                activeforeground="yellow",
                #state=DISABLED
                )

boton2.place(x=450,y=150)
boton2.config(padx=20,pady=20)

principal.mainloop()

