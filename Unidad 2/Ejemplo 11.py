"""
@author: Daniela Sanchez

"""
from io import open

archivo = open('MiArchivo.txt','r')#lectura

# lectura linea por linea
contenido = archivo.readline()
print(contenido)

contenido = archivo.readline()
print(contenido)

contenido = archivo.readline()
print(contenido)

#for linea in archivo:
#    print(linea)


archivo.close()
