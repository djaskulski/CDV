# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:31:05 2020

@author: DJaskulski
"""
#Zapoznaj się z danymi dotyczącymi ofiar katastrofy Titanica. W oparciu o 
#artykuł zawarty na stronie: 
#https://stackabuse.com/pandas-library-for-data-visualization-in-python/ 
#wykonaj analizę pliku z danymi.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv", sep="\t")

print("Typ danych: ", type(titanic))
print("Wymiar danych: ", titanic.shape)

print(titanic.isnull().sum()) # brakujace dane
mean_age = round((titanic["Age"].mean())) # srednia dla [Age]
titanic["Age"].fillna(mean_age, inplace=True) # uzupelnienie [Age] srednia
titanic.drop(["Cabin"], axis=1, inplace=True) # wymazanie kolumny [Cabin]
dom_embarked = titanic.loc[:, "Embarked"].mode() # dominanta dla [Embarked]
titanic["Embarked"].fillna(dom_embarked[0], inplace=True) # uzupelnienie [Embarked] dominanta
print(titanic.isnull().sum()) # brakujace dane

#rozklad przezycia
plt.figure(figsize=(20, 10), dpi=100)
titanic["Survived"].value_counts().plot(kind="bar", color="k", alpha=1)
plt.title("Rozklad przezycia dla 156 pasazerow, 0 = Zgineli / 1 = Ocaleli")
plt.gca().set(ylabel="Liczba")
plt.grid(zorder=0)
  
#rozklad wiek/plec
plt.figure(figsize=(20, 10), dpi=100)
sns.kdeplot(titanic.Age[titanic.Sex == "male"], shade=True, color="r", alpha=1, label="Mezczyzni")
sns.kdeplot(titanic.Age[titanic.Sex == "female"], shade=True, color="b", alpha=1, label="Kobiety")
plt.title("Rozklad wieku według plci")
plt.gca().set(xlabel="Wiek", ylabel="Odsetek")
plt.grid(True)
plt.legend()
  
#rozklad klas
plt.figure(figsize=(20, 10), dpi=100)
titanic["Pclass"].value_counts().plot(kind="bar", color="y", alpha=1)
plt.title("Klasa kajut")
plt.gca().set(ylabel="Liczba")
plt.grid(zorder=0)

#rozklad wiek/przezywalnosc
plt.figure(figsize=(20, 10), dpi=100)
sns.kdeplot(titanic.Age[titanic.Survived == 0], shade=True, color="m", label="Zmarli")
sns.kdeplot(titanic.Age[titanic.Survived == 1], shade=True, color="g", label="Ocaleni")
plt.title("Stopien przezycia w zestawieniu z wiekiem")
plt.gca().set(ylabel="Odsetek", xlabel="Wiek")
plt.grid(True)
plt.legend()

#rozklad plec/przezywalnosc
plt.figure(figsize=(20, 10), dpi=100)
plt.bar(np.array([0, 1])-0.35, titanic.Survived[titanic.Sex == "male"].value_counts().sort_index(), width=0.25, color="r", label="Mezczyzni", alpha=1)
plt.bar(np.array([0, 1]), titanic.Survived[titanic.Sex == "female"].value_counts().sort_index(), width=0.25, color="b", label="Kobiety", alpha=1)
plt.title("Stopien przezycia ze wzgledu na plec")
plt.gca().set(ylabel="Liczba")
plt.xticks(np.arange(0, 2, 1))
plt.grid(zorder=0)
plt.legend()

#rozklad klasa/przezywalnosc
plt.figure(figsize=(20, 10), dpi=100)
sns.kdeplot(titanic.Pclass[titanic.Survived == 0], shade=True, color="m", label="Zmarli")
sns.kdeplot(titanic.Pclass[titanic.Survived == 1], shade=True, color="g", label="Ocaleni")
plt.title("Stopien przezycia w zestawieniu z klasa")
plt.gca().set(ylabel="Odsetek", xlabel="Wiek")
plt.grid(True)
plt.legend()

print("""
      
      WNIOSKI:
      Na statku znajodwało się 156 osób z czego: zmarły 102 osoby (65,4%),
      przeżyły 54(34,6%).
      
      Na pokładzie największy odsetek stanowiły osoby w wieku
      20-30 zarówno wsród kobiet jak i mężczyzn. Jednoczenie mężczyźni byli
      przeważającą grupą w wieku 20+. Kobiety dominowały w przedziale do 20 lat.
      
      Podróżni najczęsciej wybierali klasę 3 (61,6%), następnie klasę 2 i 1 
      (po 19,2%).
      
      Największa różnica między ocaleniami, a zgonami przypada na przedziały
      0-10 i 20-40 lat - na korzysć ocaleń. Niestety ta sama różnica dla zgonów
      jest największa w przedziale 10-20 i 40+ lat.
      
      Zginęło ponad 80 mężczyzn i niecałe 20 kobiet, a katastrofę przeżyło nie-
      całe 20 mężczyzn i równo 40 kobiet. 
      
      Najwięcej szczęscia mieli podróżujący klasą 2 to wsród nich jest najwiekszy
      odsetek przeżyć w stosunku do zgonów. Z kolei najmniej tego szczęscia mieli
      pasażerowie klasy 3, gdzie odsetek zgonów znacznie przekracza odsetek
      przeżyć. Dla klasy pierwszej ten stosunek wynosi prawie 1 do 1.
      
      """)