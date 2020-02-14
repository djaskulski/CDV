# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:13:04 2020

@author: DJaskulski
"""
#26. Utwórz funkcję, która jako argument będzie przyjmować listę liczb 
#zmiennoprzecinkowych, a jej wynikiem trzeci moment centralny.

from scipy.stats import skew
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

def trzeciMomentCentralny(x):
    return (sum(abs(x - np.mean(x)) ** 3) / len(x))      
 
print("Moja lista: ", mojaLista())

print("Trzeci moment centrlny: ", trzeciMomentCentralny(x))
print("Wspolczynnik skosnosc - Scipy: ", skew(x))
