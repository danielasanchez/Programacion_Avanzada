"""
@author: Daniela Sanchez

"""
from io import open

archivo = open('MiArchivo.txt','r+')#lectura y escritura

contenido = archivo.readlines()

contenido[0]="Sabado"

print(contenido)

#indican posicion, de lo contrario se agrega al final
archivo.seek(0)

archivo.writelines(contenido)

archivo.close()
