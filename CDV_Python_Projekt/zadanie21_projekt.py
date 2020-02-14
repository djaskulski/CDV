# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:05:25 2020

@author: DJaskulski
"""
#21. Utwórz fukcję, która jako argument będzie przyjmować listę liczb 
#zmiennoprzecinkowych, a jej wynikiem będzie średnia arytmetyczna. Porównaj jej
#wynik z wynikiem fukcji mean z pakietu numpy

import numpy as np

def mojaLista():
    global x
    k = int(input("Dlugosc listy: "))
    list1 = []
    for i in range(k):
        list1.append([])
        list1[i] = float(input("Podaj elementy listy: "))
    x = list1
    return x
 
def srednia(list1):
    return sum(list1) / len(list1)

print("Moja lista: ", mojaLista())

print("Moja srednia: ", srednia(x))
print("Srednia NumPy: ", np.mean(x))