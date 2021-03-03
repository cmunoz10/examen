"""
Created on Wed Mar  3 17:05:01 2021

@author: CamiloMuñoz
"""

# 1 Hacer un algoritmo que calcule el total a pagar por la compra de
#   camisas. Si se compran tres :camisas o mas se aplica un descuento
#   del 30% sobre el total de la compra y si son menos de tres :camisas
#   un descuento del 10%.


valor = int(input("ingrese el valor de las camisetas a comprar "))
unidades = int(input("ingrese numero de camisetas a comprar "))

total = 0

if (unidades >= 3):
    total = (valor * unidades) * 0.7    
else:
    total = (valor * unidades) * 0.9    

print("El total a pagar por la compra de las camisas es :: $" + str(total))


# 2 En un supermercado se hace una promoción, mediante la cual el
#   cliente obtiene un descuento dependiendo de un número que se
#   escoge al azar. Si el número escogido es :menor que 74 el descuento
#   es :del 15% sobre el total de la compra, si es :mayor o igual a 74 el
#   descuento es :del 20%. Obtener cuanto dinero se le descuenta


numero = int(input("ingrese el numero escogido al azar "))
valor = int(input("ingrese el valor de la compra "))



if (numero < 74):
   total = valor * 0.85    
   descuento = valor * 0.15
else:
    total = valor * 0.8
    descuento = valor * 0.2
print("Se realizo un descuento de $"+ str(round(descuento)) + " a la compra.")
print("Para un total a pagar de : $" + str(round(total))  )



# 3 Una compañía de seguros está abriendo un departamento de
#   finanzas y estableció un programa para captar clientes, que conssite
#   en lo siguiente: Si el monto por el que se efectúa la fianza es :menor
#   que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
#   es :mayor que $50.000 la cuota a pagar será el 2% del monto. La
#   afianzadora desea determinar cual será la cuota que debe pagar al
#   cliente.



fianza = int(input("ingrese el monto de la fianza "))

if (fianza < 50000):   
    valorCuota = fianza * 0.03
else:
    valorCuota = fianza * 0.02

print("El total valor de la cuota que debe pagar el cliente es :$ "+ str(round(valorCuota)))

# 4 Una fábrica ha sido sometida a un programa de control de
#   contaminación para lo cual se efectúa una revisión de los puntos de
#   contaminación generados por la fábrica. El programa de control de
#   contaminación consiste en medir los puntos que emite la fábrica en
#   cinco días de una semana y si el promedio es :superior a los 170
#   puntos entonces :tendrá la sanción de parar su producción por una
#   semana y una multa del 50% de las ganancias diarias cuando no se
#   detiene la producción. Si el promedio obtenido de puntos es :de 170 o
#   menos entonces :no tendrá ni sanción ni multa. El dueño de la fábrica
#   desea saber cuanto dinero perderá después de ser sometido a la
#   revisión


puntosDia1 = int(input("ingrese los puntos registrados el dia  1 "))
puntosDia2 = int(input("ingrese los puntos registrados el dia 2 "))
puntosDia3 = int(input("ingrese los puntos registrados el dia 3 "))
puntosDia4 = int(input("ingrese los puntos registrados el dia 4 "))
puntosDia5 = int(input("ingrese los puntos registrados el dia 5 "))

valorSemana = int(input("ingrese el valor de las ganancias de la semana "))
promedio = (puntosDia1 + puntosDia2 + puntosDia3 + puntosDia4 + puntosDia5) / 5


if (promedio > 170):   
    perdida = valorSemana * 0.5    
else:
    perdida=0
print("El valor de la sanción sera de : $ "+ str(round(perdida)))


# 5 Una persona se encuentra con un problema de comprar un automóvil
#   o un terreno, los cuales :cuestan exactamente lo mismo. Sabe que
#   mientras el automóvil se devalúa, con el terreno sucede lo contrario.
#   Esta persona comprará el automóvil si al cabo de tres :años la
#   devaluación de este no es :mayor que la mitad del incremento del
#   valor del terreno. Ayúdale a esta pesona a determinar si debe o no
#   comprar el automóvil.


valor = int(input("ingrese el valor del terreno y el auto "))
porceAuto = float(input("ingrese el % de devaluacion del auto "))
porceTerreno = float(input("ingrese el % de valorizacion del terreno "))
valorAutoDevaluado = (valor * (porceAuto / 100) * 3)
valorTerrenoAvaluado = (valor * (porceTerreno / 100) * 3)


if (valorAutoDevaluado <= (valorTerrenoAvaluado / 2)):
    print("Recomendamos comprar el carro")
          
else:
        print("No recomendamos comprar el carro")

# 6 En una fábrica de computadoras se planea ofrecer a los clientes :un
#   descuento que dependerá del número de computadoreas que
#   compre. Si las computadoras son menos de cinco se les :dará un 10%
#   de descuento sobre el total de la compra; si el número de
#   computadoras es :mayor o igual a cinco pero menos de diez se le
#   otorga un 20% de descuento; y si son 10 o más se les :da un 40%. El
#   precio de cada computadora es :de $11.000.


cantidad = int(input("ingrese la cantidad de computadores a comprar "))

if (cantidad < 5):
    descuento = cantidad * 11000 * 0.1
    print("El valor del descuento es :$" + str(round(descuento)))
elif (cantidad >= 5 and cantidad < 10):
    descuento = cantidad * 11000 * 0.2
    print("El valor del descuento es :$"+str(round(descuento)))
else:
    descuento = cantidad * 11000 * 0.4
    print("El valor del descuento es :$"+ str(round(descuento)))
    
    
# 7 Un proveedor de estéreos ofrece un descuento del 10% sobre el
#   precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
#   independientemente de esto, ofrece un 5% de descuento si la marca
#   es :SONY. Determinar cuanto pagará, con IVA incluido, un cliente
#   cualquiera por la compra de su aparato. IVA es :del 16%


marca = input("ingrese el nombre de la marca \n 1.sony \n 2.Panasonyc \n 3.Samsung \n ")
valor = float(input("ingrese el valor del producto "))

if (valor >= 2000):
    descuento = valor * 0.1

if (marca == 1):
    total = ((valor - descuento) * 0.95) + (valor * 0.16)
else:
    total = (valor - descuento) + (valor * 0.16)
    
print("El valor total a pagar por el cliente es :$" + str(round(total)))


# 8 Una empresa quiere hacer una compra de varias piezas de la misma
#   clase a una fábrica de refacciones. La empresa, dependiendo del
#   monto total de la compra, decidirá que hacer para pagar al fabricante.
#   Si el monto total de la compra excede de $500.000 la empresa tendrá
#   la capacidad de invertir de su propio dinero un 55% del monto de la
#   compra, pedir prestado al banco un 30% y el resto lo pagará
#   solicitando un crédito al fabricante. Si el monto total de la compra no
#   excede de $500.00 la empresa tendrá capacidad de invertir de su
#   propio dinero un 70% y el restante 30% lo pagará solicitando crédito
#   al fabricante. El fabricante cobra por concepto de interes :un 20%
#   sobre la cantidad que se le pague a crédito. Obtener la cantidad a
#   inverir, valor del préstamo, valor del crédito y los intereses.



valor = float(input("ingrese el valor de la compra "))
prestamo=0
if (valor > 500000):
    cantidad = valor * 0.55
    prestamo = valor * 0.3
    credito = valor * 0.15
    intereses = credito * 1.2 
else:
    cantidad = valor * 0.7
    credito = valor * 0.3
    intereses = credito * 1.2 
    
print("La cantidad a invertir es :$"+ str(round(cantidad)))
print("El valor del prestamo es :$"+ str(round(prestamo)))
print("El valor del credito es :$"+ str(round(credito)))
print("El valor de los intereses es :$"+ str(round(intereses)))

# 9 Leer 2 números; si son iguales :que lo multiplique, si el primero es
#   mayor que el segundo que los reste y sino que los sume.


numero1 = float(input("ingrese el 1 numero "))
numero2 = float(input("ingrese el 2 numero "))
resultado = 0

if (numero1 == numero2):
    resultado = numero1 * numero2
elif (numero1 > numero2):    
    resultado = numero1 - numero2
else:
    resultado = numero1 + numero2
    
print("El resultado de la operacion es :"+ str(round(resultado)))

# 10 Leer tres :números diferentes :e imprimir el número mayor de los
#    tres



numero1 = float(input("ingrese el numero 1"))
numero2 = float(input("ingrese el numero 2"))
numero3 = float(input("ingrese el numero 3"))

if ((numero1 == numero2 or numero1 == numero3) or (numero2 == numero3 or numero2 == numero1)):
    print("Los numeros deben ser diferentes")
elif (numero1 > numero2 and numero1 > numero3):    
       print("El numero mayor es el : " + str(round(numero1) ))
elif (numero2 > numero1 and numero2 > numero3):    
      print("El numero mayor es el : " + str(round(numero2) ))
elif (numero3 > numero2 and numero3 > numero1):    
     print("El numero mayor es el : " + str(round(numero3) ) )
    
    



















    