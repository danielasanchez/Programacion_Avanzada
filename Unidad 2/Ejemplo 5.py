"""
@author: Daniela Sanchez

"""

def divide(n1,n2):
    try:
        result = n1/n2
        return result
    except:
        raise TypeError("Error, no se puede dividir entre cero")

divide(5,0)
