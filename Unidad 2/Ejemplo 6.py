"""
@author: Daniela Sanchez

"""

class MiExcepcion(Exception):
    pass

def divide(n1,n2):
    if (n2 == 0):
        raise MiExcepcion("El divisor es cero")
    else:
        print("operacion exitosa")

divide(5,0) 

