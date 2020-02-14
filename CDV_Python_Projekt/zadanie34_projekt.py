# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:58:22 2020

@author: DJaskulski
"""
#34. Utwórz klasę Kwadrat z konstruktorem ustalającym jego bok oraz metodami: 
#wyświetlającymi wartość tego boku, obliczającymi pole i obwód figury


class Kwadrat:

    def __init__(self, bok):
        self.bok = bok
        print (f"Bok kwardatu wynosi: {self.bok}")
        
    def pole(self):
        pole = self.bok**2
        print (f"Pole kwadratu wynosi: {pole}")

    def obwod (self):
        obwod = 4*self.bok
        print (f"Obwod kwadratu wynosi: {obwod}")

def main():
    print("Podaj dlugosc boku: ")
    dlugosc = float(input())
    try:
        bok = Kwadrat(dlugosc)
        bok.pole()
        bok.obwod() 
    except ValueError:
        print("Podaj liczbe a nie slowo!")

if __name__== "__main__":
    main()