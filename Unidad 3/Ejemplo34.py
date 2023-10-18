# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#frame

from tkinter import *


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")


frame1 = Frame(principal, bg="blue")
frame1.place(x=0,y=0, relwidth=0.8, relheight=0.5, )

frame2 = Frame(principal, bg="red")
#rel = valores entre 0 y 1
frame2.place(relx=0.8,rely=0.5, relwidth=0.2, relheight=0.5)



principal.mainloop()

