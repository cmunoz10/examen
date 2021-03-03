# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:44:54 2021

@author: CamiloMuñoz
"""
estudiantes=float(input("Digite el valor de la muestra: "))
muestra=float(0)
if estudiantes < 20  :
    muestra=estudiantes*0.5
    print("se tomara el 50% de la muestra ")
elif estudiantes <= 30  :
    muestra=estudiantes*0.6
    print("se tomara el 60% de la muestra ")
else :
    muestra=estudiantes*0.7
    print("se tomara el 70% de la muestra ")
        
print ("La muestra total de estudiantes sera de " + str(muestra)+ " estudiantes")



