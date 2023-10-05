"""
@author: Daniela Sanchez

"""
from io import open

archivo = open('MiArchivo.txt','r+')#lectura y escritura

archivo.write("Hola mundo")#sobreescribe la primer posicion

archivo.close()
