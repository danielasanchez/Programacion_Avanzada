# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:33:55 2023

@author: Daniela
"""

from tkinter import *
import json
import copy



#aqui tengo la clase productos, al igual que en la ventana
#donde los listamos, si solo se quiere poner una vez
#se tendria que ver si se pasa por parametro

class Producto():
    def __init__(self, name, price,category):
        self.name=name
        self.price=price
        self.category=category
        
    
producto1 = Producto("Lapiz",15.5,"Papeleria")
producto2 = Producto("Pluma",20.5,"Papeleria")     
producto3 = Producto("Borrador",5.0,"Papeleria")
producto4 = Producto("Cuaderno",34.0,"Papeleria")   
producto5 = Producto("Sabritas Original",22.0,"Alimentos")
producto6 = Producto("Coca Cola",23.0,"Alimentos")   

productos=[producto1,producto2,producto3,producto4,producto5,producto6]


class Compra():
    def __init__(self, productos, total):
        self.productos=productos
        self.total=total
    
    def calcular(self):
        total=0
        for item in self.productos:
            total+=item.price
        
        self.total=total
        return total



def VentanaCompra(principal):
    def enviar():
        # try:
        #     #si hay compras las carga
        #     with open('Compras.json', 'r') as archivo:
        #         compras = json.load(archivo)
        # except:
        #     #si no hay crea una lista vacia
        #     compras = []


        # creo una copia del objeto compra
        # y la convierto a diccionario para ser almacenada en un
        # json
        temp = copy.copy(compra)
        temp =temp.__dict__
        del temp['productos']

        temp['productos']=[]
        #elimino productos de temporal para reemplazarlos por los mismos productos
        #pero en formato de diccionario
        for i in compra.productos:
            temp["productos"].append(i.__dict__)

        # #si existen o no compras anteriores agrego la compra convertida a 
        # #diccionario
        # compras.append(temp)


        #guardo en el archivo json
        with open("Compra.json", "w") as archivo:
            json.dump(temp, archivo)    

        serializacion = json.dumps(temp,indent=4)
        print(serializacion)
        
        ventana.destroy()
        
    def sumar(item):
        #hasta que el usuario no agrega un producto
        #se habilita el boton
        button1.config(state=NORMAL)
        #se agrega a la estancia compra un producto
        compra.productos.append(item)
        #se ejecuta el metodo de la instancia
        total = compra.calcular()
        #se actualiza la propiedad total del instancia compra
        compra.total=total
        
        #se actualiza la etiqueta con el total
        label2.config(text="$ "+str(total))

        return total
        
    def registro(idx_and_item,frame,ventana):
        index, item = idx_and_item
        lb1 = Label(frame, text="producto: "+str(item.name))
        lb1.grid(row=index, column=1)
        lb2 = Label(frame, text="precio: "+str(item.price))
        lb2.grid(row=index, column=2)
        bt1 = Button(frame, text="+", command= lambda : sumar(item))
        bt1.grid(row=index, column=3)

    #Mostramos con un map cada producto    
    def Mostrar(lista,frame,ventana):
        if len(lista)>0:
            #la funcion map nos permite iterar entre los elementos de la lista
            #enumerate() en Python enumera los elementos de una lista
            result = list(map(lambda e: registro(e,frame,ventana), enumerate(lista)))

    
    compra = Compra([],0)
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
    label1 = Label(ventana, text="Realiza tu compra")
    label1.pack()
    label2 = Label(ventana, text="$")
    label2.pack()
    #se crea este frame donde se pondran los widgets
    frame = Frame(ventana)
    frame.pack()
    Mostrar(productos,frame,ventana)
    button1 = Button(ventana, text="Terminar", command=enviar, state=DISABLED)
    button1.pack()
    