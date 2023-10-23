# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:48:54 2023

@author: Daniela Sánchez
"""

from tkinter import *

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("800x500+400+200")

#height = cantidad de lineas
#width = cantidad de caracteres
label1= Label(principal,text="Mi Etiqueta",
              font=("Arial",16,"bold","underline"),
              fg="blue",bg="green",height=4, width=20)

label1.pack()

principal.mainloop()