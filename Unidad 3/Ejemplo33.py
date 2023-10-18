# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#grid

from tkinter import *


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")


label1 = Label(principal, text="Soy una etiqueta")
# relx, rely = eslaca del 0 al 1
label1.grid(row=0,column=0)

label2 = Label(principal, text="Soy la segunda etiqueta")
# columnspan =  cantidad de columnas que puede abarcar
# ipadx = ancho de la etiqueta
label2.grid(row=1,column=1,columnspan=2,ipadx=10)


label3 = Label(principal, text="Soy otra etiqueta")
# ipady = alto de la etiqueta
# pady = pixeles de separacion
label3.grid(row=2,column=2, ipady=2,pady=15)


principal.mainloop()

