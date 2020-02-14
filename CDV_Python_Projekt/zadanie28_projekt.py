# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:55:26 2020

@author: DJaskulski
"""
#28. Utwórz funkcję, która jako argument będzie przyjmować dwie listy o równej
#liczbie elementów, a jej wynikiem będzie współczynnik korelacji

from scipy.stats import pearsonr
import numpy as np

def mojaLista1():
    global x
    k = int(input("Dlugosc listy 1: "))
    list1 = []
    for i in range(k):
        list1.append([])
        list1[i] = float(input("Podaj elementy listy 1: "))
    x = np.array(list1)
    return x

def mojaLista2():
    global y
    k = int(input("Dlugosc listy 2: "))
    list1 = []
    for i in range(k):
        list1.append([])
        list1[i] = float(input("Podaj elementy listy 2: "))
    y = np.array(list1)
    return y

def wspolczynnikKorelacji(x, y):
        n = len(x)
        m = len(y)
        if (n >= 2) and (len(x) == len(y)) or (x != y):
            licznik1 = (n * sum(x * y)) 
            licznik2 = (sum(x) * sum(y))
            mianownik1 = (n * sum(x**2) - (sum(x))**2)
            mianownik2 = (n * sum(y**2) - (sum(y))**2)
            r = (licznik1 - licznik2) / ((mianownik1 * mianownik2)**0.5)
            return float(r)
        else:
            print("""Dlugosc porownywanych list musi byc TAKA SAMA, 
#jednoczesnie rowna lub wieksza DWA. Ich wartosci zawarte w liscie 
#NIE moga byc IDENTYCZNE, lub prawie identyczne""")
                    
print("Moja lista1: ", mojaLista1())
print("Moja lista2: ", mojaLista2())

print("Wspolczynnik korelacji ", wspolczynnikKorelacji(x, y))
print("Wspolczynnik korelacji - Numpy: ", pearsonr(x, y))