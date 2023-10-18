# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:46:25 2023

@author: Daniela
"""

# Recursividad

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3)) 


# 3! = 3x2x1