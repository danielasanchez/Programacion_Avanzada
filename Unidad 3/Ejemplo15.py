# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""

from tkinter import *

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("400x300+400+200")
principal.config(bg="gray")

label1 = Label(principal, text="Nombre").pack()

# highlightthickness = tamaño del borde al seleccionar
# highlightcolor = color de borde al seleccionar
input1 = Entry(principal, 
               highlightthickness=4, 
               highlightcolor="blue")

input1.pack()


principal.mainloop()

