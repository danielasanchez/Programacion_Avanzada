# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:48:54 2023

@author: Daniela Sánchez
"""

from tkinter import *
from PIL import ImageTk, Image

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("800x500+400+200")

# img = Image.open(r"C:\Users\Daniela\Documents\perrito.png").resize((300,300))
img = Image.open("perrito.png").resize((300,300))
img = ImageTk.PhotoImage(img)

label1 = Label(principal,image=img)
label1.place(x=100,y=150)

principal.mainloop()