# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:48:54 2023

@author: Daniela Sánchez
"""

from tkinter import *

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("800x500+400+200")

#Se crea la etiqueta haciendo una instancia de la clase Label
label1= Label(principal,text="Mi Etiqueta")
label1.pack()

principal.mainloop()

