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
# relx, rely = escala del 0 al 1
label1.place(relx=0.5,rely=0.7)

label2 = Label(principal, text="Soy otra etiqueta")
label2.place(relx=0.5,rely=0.8,relwidth=0.4,relheight=0.1)

principal.mainloop()

