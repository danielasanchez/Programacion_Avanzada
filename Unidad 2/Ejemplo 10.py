"""
@author: Daniela Sanchez

"""
from io import open

#Poner un archivo que exista o usar try-except

archivo = open('MiArchivo.txt','r')#lectura

# contenido = archivo.read() #cadena
contenido = archivo.readlines() #lista

archivo.close()

print(contenido)
