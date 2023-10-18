# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:46:25 2023

@author: Daniela
"""

# map 
# permite generar una nueva lista


alumnos = [
            {'nombre':'Juan', 'edad':18},
            {'nombre':'Jose', 'edad':17}
           ]

# metodo 1
meses = list(map(lambda a: a['edad'] * 12,alumnos))

#metodo 2
# mesesFunc = lambda a: a['edad'] * 12
# meses = list(map(mesesFunc,alumnos))


#metodo 3
# def mesesFunc(a):
#     return a['edad'] * 12

# meses = list(map(mesesFunc,alumnos))


print(meses)