"""
@author: Daniela Sanchez

"""

try:
    print("Código que queremos ejecutar")
except:
    print("Código que se ejecute si ocurre la excepción")
else:
    print("Llegamos aquí si no hay excepción")
finally:
    print("Esto se ejecuta siempre")
