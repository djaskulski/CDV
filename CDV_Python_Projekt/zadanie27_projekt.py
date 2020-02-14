# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:03:40 2020

@author: DJaskulski
"""
#27. Utwórz funkcję, która jako argument będzie przyjmować listę liczb 
#zmiennoprzecinkowych, a jej wynikiem będzie czwarty moment centralny.

from scipy.stats import kurtosis
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

def czwartyMomentCentralny(x):
    return (sum(abs(x - np.mean(x)) ** 4) / len(x))      
 
print("Moja lista: ", mojaLista())

print("Czwarty moment centralny: ", czwartyMomentCentralny(x))
print("Kurtoza - SciPy: ", kurtosis(x))
