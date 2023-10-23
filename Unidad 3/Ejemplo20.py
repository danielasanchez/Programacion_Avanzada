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

# selectbackground = color del fondo al seleccionar el texto
# selectforeground = color del texto al seleccionarlo
input1 = Entry(principal, 
               highlightthickness=4, 
               highlightcolor="blue",
               selectbackground="pink", 
               selectforeground = "green")

input1.pack()

principal.mainloop()

