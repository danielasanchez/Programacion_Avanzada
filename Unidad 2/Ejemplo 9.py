"""
@author: Daniela Sanchez

"""
from io import open

texto = ["Martes\n","Miercoles\n","Jueves\n","Viernes\n"]

archivo = open('MiArchivo.txt','w')#sobreescribe

archivo.write("Lunes\n") #Una linea

archivo.writelines(texto) #Multiple lineas

archivo.close()

