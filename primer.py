# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

total=float(0)
n=int(input("Digite el numero de llantas "))

if n < 5  :
    total=n*300
    print("El total a pagar por llanta es : $300 ")
elif n <= 10 :
    total=n*250
    print("El total a pagar por llanta es : $250")
else :
        total = n*200
        print("El total a pagar por llanta es : $200")
        
print ("El total a pagar por las " + str(n) + "llantas compradas es : "+ "$"+ str(total))

