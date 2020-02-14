# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:11:48 2020

@author: DJaskulski
"""
#25. Utwórz fukcję, która jako argument będzie przyjmować listę liczb 
#zmiennoprzecinkowych, a jej wynikiem będzie wariancja.

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

def wariancja(x):
    return (sum(abs(x - np.mean(x)) ** 2) / len(x))      
 
print("Moja lista: ", mojaLista())

print("Wariancja: ", wariancja(x))
print("Wariancja Numpy: ", np.var(x))
