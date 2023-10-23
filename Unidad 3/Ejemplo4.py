# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#place

from tkinter import *


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")


label1 = Label(principal, text="Soy una etiqueta")
# x,y = pixeles
label1.place(x=10,y=50, width=100, height=40)

label2 = Label(principal, text="Soy otra etiqueta")
#se utiliza x,y para establecer dependiendo del anchor
label2.place(x=340,y=100, width=100, height=40, anchor=SE)


principal.mainloop()

