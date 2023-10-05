"""
@author: Daniela Sanchez

"""
import pickle

lista = [1,2,3,4,5]

archivo = open('archivo.pckl','wb')

#escribimos
pickle.dump(lista,archivo)
archivo.close()

#leemos
archivo = open('archivo.pckl','rb')
lista2 = pickle.load(archivo)
archivo.close()

