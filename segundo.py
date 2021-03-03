# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:52:34 2021

@author: CamiloMuñoz
"""

cedula=int(input("digite la cedula "))
subtotal=float(input("Digite el subtotal de la compra 12"))
total=float(0)
digitos=cedula % 100

if digitos == 1  :
    total=subtotal*0.9
    print("se realizo un descuento del 10% ")
elif digitos == 25  :
   total=subtotal*0.8
   print("se realizo un descuento del 20% ")
elif digitos == 44  :
   total=subtotal*0.75
   print("se realizo un descuento del 35% ")
elif digitos == 57  :
   total=subtotal*0.5
   print("se realizo un descuento del 50% ")
else :
    total=subtotal
    print("No es posible realizar descuento con esa cedula")

print("Su total a pagar es : $" + str(total)+ "pesos")