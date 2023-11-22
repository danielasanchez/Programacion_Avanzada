# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:33:55 2023

@author: Daniela
"""

from tkinter import *


class Producto():
    def __init__(self, name, price):
        self.name=name
        self.price=price
        
    
producto1 = Producto("Lapiz",15.5)
producto2 = Producto("Pluma",20.5)     
producto3 = Producto("Borrador",5.0)
producto4 = Producto("Cuaderno",34.0)   


productos=[producto1,producto2,producto3,producto4]


def VentanaProductos(principal):
    def registro(idx_and_item,frame,ventana):
        index, item = idx_and_item
        lb1 = Label(frame, text="producto: "+str(item.name))
        lb1.grid(row=index, column=1)
        lb1 = Label(frame, text="precio: "+str(item.price))
        lb1.grid(row=index, column=2)
        # lb2 = Label(frame, text="Edad: "+str(item.edad))
        # lb2.grid(row=index, column=3)
        # bt1 = Button(frame, text="Registrar", command= lambda : ventanitaRegistro (ventana,item))
        # bt1.grid(row=index, column=4)

    #es funcion usara un map para ir mostrando cada uno de los registros    
    def filtrados(arreglo,frame,ventana):
        if len(arreglo)>0:
            result = list(map(lambda e: registro(e,frame,ventana), enumerate(arreglo)))


    # revisar propiedades de bg, bd, etc.
    ventana = Toplevel(principal)
    ventana.title("Productos")
    ventana.geometry("330x250+420+220")
    # minsize(x,y)
    # maxsize(x,y)
    ventana.resizable(0,0)
    # Deshabilita las otras ventanas (Modal)
    ventana.grab_set()
    # aparece delante de la principal
    ventana.transient(master=principal)
    # podemos agregar widgets
    label1 = Label(ventana, text="Mis productos")
    label1.pack()
    #se crea este frame donde se pondran los widgets
    frame = Frame(ventana)
    frame.pack()
    filtrados(productos,frame,ventana)
    