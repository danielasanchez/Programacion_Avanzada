# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:48:54 2023

@author: Daniela Sánchez
"""

from tkinter import *

#Creamos la ventana principal partiendo de la clase Tk
principal = Tk()
principal.title("Mi primer ventana")
#le ponen un icono a la ventana
principal.iconbitmap("icono.ico")
#altoxancho 
principal.geometry("800x500")
# principal.geometry("375x200+500+250") #Dimensiones y Posiciones

#se indica si se permite cambiarle el tamaño manualmente
#se puede usar False,True,0 y 1
principal.resizable(False,1)

# principal.config(cursor="heart")
#background
principal.config(bg="gray")
# relief = flat raised sunken groove ridge (aplica tambien para otros widgets)
principal.config(bd=5, relief="ridge") 


#Ejecutamos el metodo para que se visualice la ventana
#va al final del codigo, ya que agregamos todo lo que 
#queremos mostrar
principal.mainloop()



