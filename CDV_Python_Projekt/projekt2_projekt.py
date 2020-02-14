# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:30:51 2020

@author: DJaskulski
"""
#Utwórz klasę Vector2D. Wykorzystaj całą wiedzę jaką posiadasz na temat 
#wektorów na płaszczyźnie. Zdefiniuj wszystkie znane Ci operacje.

import math

class Vector2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def wspolrzedne(self):
        print("x="+str(self.x)+", y="+str(self.y))

    def plusWektor(self, inny):
        self.x = self.x + inny.x
        self.y = self.y + inny.y

    def minusWektor(self, inny):
        self.x = self.x - inny.x
        self.y = self.y - inny.y

    def razyLiczba(self, a):
        self.x = a*self.x
        self.y = a*self.y

    def razyWektor(self, inny):
        return self.x*inny.x + self.y*inny.y 

    def obrot(self, alfa):
        alfaDeg = alfa*math.pi/180
        sinus = math.sin(alfaDeg)
        cosinus = math.cos(alfaDeg)
        x = self.x
        y = self.y       
        self.x = x*cosinus - y*sinus
        self.y = x*sinus + y*cosinus

    def modul(self):
        return (self.x**2 + self.y**2)**0.5

    def wektorPrzeciwny(self):
        self.x = -self.x
        self.y = -self.y