# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:14:05 2020

@author: DJaskulski
"""
#31. Korzystając z instrukcji np.random.choice oraz reshape z pakietu numpy 
#stworzyć funkcję generują macierz kwadratową stopnia N wypełnioną wartościami
#0 i 255 w losowy sposób

import numpy as np

N = int(input("Podaj wymiar macierzy kwadratowej: "))
macierzLosowa = np.random.choice([0,255], N*N, p=[0.7, 0.3]).reshape(N,N)
print(macierzLosowa)