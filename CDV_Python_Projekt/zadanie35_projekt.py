# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:14:18 2020

@author: DJaskulski
"""
#35. Utwórz klasę Prostokąt, a następnie na jej podstawie (korzystając z mechanizmu 
#dziedziczenia) utwórz klasę Kwadrat

class Prostokat():
    
    def __init__(self, a, b):
        self._a = a
        self._b = b        
            
    def __str__(self):
        return f"Bok a:{self._a}, bok b:{self._b}"
    
    def pole(self):
        return self._a * self._b
    
    def obwod(self):
        return 2 * self._a + 2 * self._b
    
class Kwadrat(Prostokat):
    
    def __init__(self, a):
        self._a = a
        self._b = a
        
    def __str__(self):
        return f"bok a:{self._a}"
    
    
prostokat = Prostokat(2,4)
kwadrat = Kwadrat(5)


print(prostokat)
print(f"Pole prostokata = {prostokat.pole()}")
print(f"Obwod prostokata = {prostokat.obwod()}")

print(kwadrat)
print(f"Pole kwadratu = {kwadrat.pole()}")
print(f"Obwod kwadratu = {kwadrat.obwod()}")