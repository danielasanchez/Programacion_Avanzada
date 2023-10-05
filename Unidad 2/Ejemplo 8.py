"""
@author: Daniela Sanchez

"""
class MiExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje=mensaje

def divide(n1,n2):
    if (n2 == 0):
        mensaje= "El divisor es cero"
        raise MiExcepcion(mensaje)
    else:
        print("operacion exitosa")

divide(5,0) 
