# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:34:18 2023

@author: Daniela
"""

class Perro():
    nombre="Whisky"
    raza = "Chihuahua"
    edad = 11
    
    def __init__(self):
        print("Objeto Creado")
        
        
perrito1=Perro()
perrito2=Perro()

print(perrito1.nombre)
print(perrito2.nombre)