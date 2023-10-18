# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#canvas

from tkinter import *
from PIL import ImageTk, Image
   
principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("480x380+400+200")
principal.config(bg="gray")


canva1 = Canvas(principal, bg="pink", width=300,height=250)
canva1.pack()
# x,y
canva1.create_rectangle(150,100,250,200, width=10, fill="blue")
canva1.create_line(0,0,100,150,250,250,width=4,fill="purple")
canva1.create_oval(5,5,100,100,width=4,fill="red")
canva1.create_arc(50,50,150,150,start=0, extent=260, width=4,fill="green")

# img = Image.open(r"C:\Users\Daniela\Documents\perrito.png").resize((300,300))
img = Image.open("perrito.png").resize((100,100))
img = ImageTk.PhotoImage(img)
canva1.create_image(30,150,image=img,anchor=NW)
principal.mainloop()

