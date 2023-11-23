# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:33:55 2023

@author: Daniela
"""

from tkinter import *
import json
import copy
from tkinter import messagebox


def VentanaHistorial(principal):

    def registro(idx_and_item,frame,ventana):
        index, item = idx_and_item
        lb1 = Label(frame, text='producto: '+ item['name']+ " precio: $"+str(item['price']))
        lb1.pack()
        

    #Mostramos con un map cada producto    
    def Mostrar(listaProductos,frame,ventana):
            #la funcion map nos permite iterar entre los elementos de la listaProductos
            #enumerate() en Python enumera los elementos de una lista
            # result = list(map(lambda e: registro(e,frame,ventana), enumerate(listaProductos)))
            pass
    
    #antes de iniciar con la creacion de la ventana
    #intentamos leer un archivo json
    try:
        #si hay compras las carga
        with open('Compra.json', 'r') as archivo:
            compra = json.load(archivo)
            
        # revisar propiedades de bg, bd, etc.
        ventana = Toplevel(principal)
        ventana.title("Ventas")
        ventana.geometry("330x250+420+220")
        # minsize(x,y)
        # maxsize(x,y)
        ventana.resizable(0,0)
        # Deshabilita las otras ventanas (Modal)
        ventana.grab_set()
        # aparece delante de la principal
        ventana.transient(master=principal)
        # podemos agregar widgets
        label1 = Label(ventana, text="Venta realizada")
        label1.pack()
        #se crea este frame donde se pondran los widgets
        frame = Frame(ventana)
        frame.pack()
        
        #como solo tenemos una compra en el historial
        #lo cargado en compra contiene nuestra informacion
        #la key total de compra contiene el total
        #y la key productos la lista de productos
        #con la siguiente  funcion mandamos la lista de productos
        Mostrar(compra['productos'],frame,ventana)
        
        #aqui solo creamos una etiqueta y directamente mostramos el total
        lb1 = Label(ventana, text=" total: $"+str(compra['total']))
        lb1.pack()
    except:
        #si no hay crea una lista vacia
        compra = []
        messagebox.showinfo("Error","No haz realizado una compra")
        
    


    

    