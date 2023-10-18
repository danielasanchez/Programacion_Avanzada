# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:46:25 2023

@author: Daniela
"""

# filter
# permite generar una nueva lista basados en una condicion

edades = [18, 19, 20, 18, 19]

# metodo 1
mayores = list(filter(lambda e: e>18,edades))

# metodo 2
# mayoresFunc = lambda e: e>18
# mayores = list(filter(mayoresFunc,edades))

# metodo 3
# def mayoresFunc(e):
#     return e>18

# mayores = list(filter(mayoresFunc,edades))


print(mayores)