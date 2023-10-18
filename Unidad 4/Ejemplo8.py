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



def mesesFunc(a):
    a['meses'] = a['edad'] * 12
    return a

meses = list(map(mesesFunc,alumnos))


print(meses)