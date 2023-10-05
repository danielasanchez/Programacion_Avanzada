"""
@author: Daniela Sanchez

"""

def divide(n1, n2):
    try:
        resultado = n1/n2
        print("El resultado de dividir {} entre {} es {}".format(n1,n2,resultado))
    except:
        print("Revisa que estes utilizando los datos correctos")
    else:
        print("La operación se realizó correctamente")
    finally:
        print("Operación finalizada")
        
divide(3,2)
