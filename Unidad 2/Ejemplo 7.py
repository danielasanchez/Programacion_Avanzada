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

# divide(5,0)

try:
    divide(5,0) 
    print("La operación se realizo correctamente.")
except MiExcepcion:
    print("No puedes dividir entre cero.") 
