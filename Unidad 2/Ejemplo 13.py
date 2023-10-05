"""
@author: Daniela Sanchez

"""
from io import open

archivo = open('MiArchivo.txt','a')#append

archivo.write("Domingo")#se coloca en la ultima posicion

archivo.close()
