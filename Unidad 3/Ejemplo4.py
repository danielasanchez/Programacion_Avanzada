# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:48:54 2023

@author: Daniela Sánchez
"""

from tkinter import *

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("800x500+400+200")

#fg = color de la letra
#bg = color de fondo
label1= Label(principal,text="Mi Etiqueta",
              font=("Arial",16,"bold","underline"),
              fg="blue",bg="green")

label1.pack()

principal.mainloop()