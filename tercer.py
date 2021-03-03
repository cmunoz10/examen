# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:32:53 2021

@author: CamiloMuñoz
"""
subtotal=float(input("Digite el subtotal a pagar el colchones : "))
colchones=int(input("Digite la cantidad de colchones en la compra: "))
total=float(0)
if colchones < 3  :
    total=subtotal
    print("no es posible descuento ")
elif colchones < 6  :
    total=subtotal*0.8
    print("se realizo un descuento del 20%")
elif colchones < 8  :
    total=subtotal*0.75
    print("se realizo un descuento del 25%")
    
else :
        total = subtotal*0.7
        print("se hizo un descuento del 30%")
        
print ("El total a pagar es " + str(total))


