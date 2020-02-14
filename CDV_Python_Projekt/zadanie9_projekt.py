# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:28:26 2020

@author: DJaskulski
"""
#9. Utwórz skrypt z interfejsem tekstowym, który wyliczy sumę n kolejnych liczb 
#(użytkownik podaje pierwszą i ostatnią liczbę sumy). Uwaga – w zadaniu należy 
#zbudować funkcję własną realizującą dane zadanie

def sumaCiagu(a, b):
    for i in range(a, b):
        a = a+i+1
    return a
    
a = int(input("Podaj poczatek ciagu: "))
b = int(input("Podaj koniec ciagu: "))

print("Suma zadanego ciagu to: ", sumaCiagu(a, b))
