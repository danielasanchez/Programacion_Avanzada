# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:14:37 2023

@author: Daniela
"""
# Metodo de encadenamiento (Chaining)
# Ejecutar metodos de manera secuencial

class Perro():
    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        print("Objeto Creado")
        
    def comer(self):
        print("Comer")
        return self
        
    def dormir(self):
        print("Dormir")
        return self
        
    def ladrar(self):
        print("Ladrar")         
        return self
        
perrito1 = Perro("Whisky","Chihuahua",11)
perrito1.comer().dormir().ladrar().ladrar()