"""
@author: Daniela Sanchez

"""

def divide(n1, n2):
    try:
        resultado = n1/n2
        print("El resultado de dividir {} entre {} es {}".format(n1,n2,resultado))
    except ZeroDivisionError:
        print("No puedes dividir entre cero")
    except TypeError:
        print("Revisa el tipo de dato")
    except:
        print("Revisa que estes utilizando los datos correctos")
    else:
        print("La operación se realizo correctamente")
    finally:
        print("Operación finalizada")

divide(3,2)
divide(3,"2")
divide(3,0)
