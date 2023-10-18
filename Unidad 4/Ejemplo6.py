# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:46:25 2023

@author: Daniela
"""

# map 
# permite generar una nueva lista



edades = [18, 19, 20, 18, 19]

# metodo 1
meses = list(map(lambda e: e*12,edades))

#metodo 2
# mesesFunc = lambda e: e*12
# meses = list(map(mesesFunc,edades))


#metodo 3
# def mesesFunc(e):
#     return e*12

# meses = list(map(mesesFunc,edades))


print(meses)