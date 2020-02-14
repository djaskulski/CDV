# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:08:25 2020

@author: DJaskulski
"""
#11. Utwórz skrypt z interfejsem tekstowym który obliczy silnię od danego 
#argumentu. Wykonać zadanie na dwa sposoby – iteracyjnie i rekurencyjnie

def silniaIteracyjnie(liczba):
    wynik = 1
    for i in range(1, liczba+1):
        wynik *= i
    return wynik

def silniaRekurencynie(liczba):
    if liczba <= 1:
        return 1
    else:
        return liczba * silniaRekurencynie(liczba-1)

        
liczba = int(input('Podaj liczbe: '))

print("Silnia iteracyjnie: ", silniaIteracyjnie(liczba))
print("Silnia rekurencyjnie: ", silniaRekurencynie(liczba))