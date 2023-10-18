# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#Pack


from tkinter import *


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")


label1 = Label(principal, text="Soy una etiqueta")
# side = TOP, BOTTOM, LEFT o RIGHT
# fill = X, Y o BOTH
# expand = TRUE
label1.pack(side=BOTTOM,fill=X,pady=5)

label2 = Label(principal, text="Soy otra etiqueta")
label2.pack(side=BOTTOM,fill=X,pady=5)

principal.mainloop()

