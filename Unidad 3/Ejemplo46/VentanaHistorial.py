# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:33:55 2023

@author: Daniela
"""

from tkinter import *
import json
import copy

def VentanaHistorial(principal):

    def registro(idx_and_item,frame,ventana):
        index, item = idx_and_item
        lb1 = Label(frame, text='compra: '+str(index)+ " total: $"+str(item['total']))
        lb1.pack()
        
        #este codigo es para si queremos ver cada producto
        # for i in item['productos']:
        #     Label(frame, text=i['name']).pack()

    #Mostramos con un map cada producto    
    def Mostrar(lista,frame,ventana):
        if len(lista)>0:
            #la funcion map nos permite iterar entre los elementos de la lista
            #enumerate() en Python enumera los elementos de una lista
            result = list(map(lambda e: registro(e,frame,ventana), enumerate(lista)))

    
    #antes de iniciar con la creacion de la ventana
    #intentamos leer un archivo json
    try:
        #si hay compras las carga
        with open('Compras.json', 'r') as archivo:
            compras = json.load(archivo)
    except:
        #si no hay crea una lista vacia
        compras = []
        print('No hay compras')
    

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
    label1 = Label(ventana, text="Ventas realizadas")
    label1.pack()
    #se crea este frame donde se pondran los widgets
    frame = Frame(ventana)
    frame.pack()
    Mostrar(compras,frame,ventana)

    