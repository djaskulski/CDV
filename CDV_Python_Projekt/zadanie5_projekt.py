# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:10:21 2020

@author: DJaskulski
"""
#5. Utwórz skrypt, który będzie komunikować, czy wprowadzona liczba jest 
#dodatnia czy nie

def roznaOdZera(a):
    if a > 0:
        print("Podana liczba jest dodatnia!")
    elif a < 0:
        print("Podana liczba jest ujemna!")
    elif a == 0:
        print("Jeden rabin powie tak, inny rabin powie nie")
    else:
        print("Miales jedno proste zadanie...")
        
a = float(input("Podaj liczbe: "))

roznaOdZera(a)
