# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:00:54 2021

@author: CamiloMuñoz
"""

"Ejercicio 1"

persona1=(float(input("Digite el valor ingresado por la primera persona : ")))
persona2=(float(input("Digite el valor ingresado por la segunda persona : ")))
persona3=(float(input("Digite el valor ingresado por la tercera persona : ")))
 
total=persona1+persona2+persona3

porcentaje1=(persona1*100)/total
porcentaje2=(persona2*100)/total
porcentaje3=(persona3*100)/total
print("La primera persona aporto el siguiente porcentaje : " + str(porcentaje1))
print("La segunda persona aporto el siguiente porcentaje : " + str(porcentaje2)) 
print("La tercera persona aporto el siguiente porcentaje : " + str(porcentaje3))


print ("Ejercicio 2")



sueldo = float(input("Digite el sueldo del empleado "))
numeroHijos = int(input("cuantos hijos tiene el empleado? "))
bono = float(numeroHijos*80000)
total = sueldo + bono
print("El bono otorgado al empleado es de : " + str(bono))
print("Para un sueldo total de : " + str(total))


print ("Ejercicio 3")

# 3 Un banco da a sus ahorradores un interes de 1.5% sobre el monto
#   ahorrado. Teniendo como dato de entrada el saldo inicial del
#   ahorrador determine el saldo final.

saldoInicial=float(input("digitel su saldo inicial"))
saldoFinal = saldoInicial*0.985
print("El saldo total ahorrado sera de :" +srt(saldoFinal))


print ("Ejercicio 4")

# 4 Una inmobiliria vende terrenos a $80.000 el metro cuadrado. El
#   cliente debe dar una cuota inicial del 35% y el resto lo paga en 12
#   cuotas. Determine el valor a pagar por cuota inicial y el monto de
#   cada cuota.

metrosCuadrados = float(input("Digite la cantidad de metros cuadrados "))
cuotaInicial = 80000*0.35
valorcuota = (80000*0.65)/12
print("El valor de la cuota inicial es de : " + str(cuotaInicial) )
print("El Valor de las cuota mensual sera de  : " + str(valorcuota) + "Durante 12 meses")
    


print ("Ejercicio 5 ")

# 5 Una empresa le hace los siguientes descuentos sobre el sueldo base
#   a sus trabajadores: 1% por ley de politica pública, 4% por seguro
#   social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
#   programa en Java que determine el monto de cada descuento y el
#   monto total a pagar al trabajador.

sueldoBase = float(input("Digite el sueldo base del trabajador "))
descuentoPoli = sueldoBase * 0.01
descuentoSeguSo = sueldoBase * 0.04
descuentoSeguFo =sueldoBase * 0.005
descuentoCaja = sueldoBase * 0.05
sueldoTotal = sueldoBase - descuentoSeguSo - descuentoSeguFo - descuentoPoli - descuentoCaja
print("El descuento por ley de politica pública es :" + str(descuentoPoli))
print("El descuento por seguro social es :" +  str(descuentoSeguSo))
print("El descuento por seguro forzoso es :" + str(descuentoSeguFo))
print("El descuento por caja de ahorro es :" + str(descuentoCaja))
      
print ("Ejercicio 6 ")

# 6 El periódico el Informador cobra por un aviso clasificado un monto
#   que depende del número de palabras, tamaño en cetímetros y
#   número de colores. Cada palabra tiene un costo de $20.000, cada
#   centímetro tiene un costo de $15.000 y cada color tiene un costo de
#   $25.000. Realice un algoritmo que determine el monto a pagar por un
#   aviso clasificado.

palabras=int (input("Digite el numero de palabras"))
centimetros=int (input("Digite el numero de centimetros"))
colores=int (input("Digite el numero de colores"))

palabras=palabras*20000
centimetros=centimetros*15000
colores=colores*25000
total=palabras+centimetros+colores
print("el total a pagar por el clasificado es : "+ str(total))

# 7 Una empresa paga a sus empleados un bono por antigüedad que
#   consiste en $100.000 por el primer año laboral y $120.000 por cada
#   año siguiente. Realice un programa en Java que determine el monto
#   del bono a pagar a un trabajador que tiene varios años en la empresa.

print ("Ejercicio 7")

years=input("Digite la cantidad de años trabajados")
if years < 2:
    bono=100000
else :
    bono=100000+(120000*years)
print("El bono a pagar es de " + str(bono))




# 8 Una Universidad le paga a sus profesores $20.000 la hora y le hace
#   un descuento del 5% por concepto de caja de ahorro. Determine el
#   monto del descuento y el monto total a pagar al profesor.

print ("Ejercicio 8")

horas=float(input("Digite la cantidad de horas trabajadas"))
sueldo=horas*20000
descuento=sueldo*0.05
total=sueldo-descuento
print("El monto descontado es : "+str(descuento))
print("El monto a pagar es de : "+str(total))


# 9 Un centro de comunicaciones alquilan tarjetas para realizar llamadas
#   y cobran el monto consumido de la tarjeta mas un recargo del 20%.
#   Teniendo como dato de entrada el monto inicial y el monto final de la
#   tarjeta, determine el costo de la llamada.

print ("Ejercicio 9")

saldoInicial=float(input("Digite el saldo inicial de la tarjeta" ))
saldoFinal=float(input("Digite el valor final "))
consumo=saldoInicial-saldoFinal

total=consumo*(1.2)

print("El total a pagar sera de : " + str (total))



# 10 En una fototienda cobran por el revelado de un rollo $1.500 por cada
#    foto. Realice un programa en Java que determine el monto a pagar
#    por un revelado completo sabiendo que adiconalmente le cobran el
#    IVA (16%).

print ("Ejercicio 10")

cantidadRollos=float(input("Digite la cantidad de fotos a revelar "))
precio=(cantidadRollos*1500)*1.16
print("El total a pagar es de : " + str(precio))


# 11 En un hospital existen tres áreas: Ginecología, Pediatría y
#    Traumatología. El presupuesto anual del hospital se reparte
#    conforme a la siguiente tabla:
#    Area - Porcentaje Presupuestal
#    Ginecología - 40%
#    Traumatología - 30%
#    Pediatría - 30%
#    Obtener la cantidad de dinero que recibirá cada área, para cualquier
#    monto presupuestal.
print ("Ejercicio 11")

presupuesto=float(input("Digite el presupuesto total : "))
gine=presupuesto*0.4
trauma=presupuesto*0.3
pediatra=presupuesto*0.3
print("El valor destinado a Ginecología es : " + str(round(gine)))
print("El valor destinado a Traumatología es : " + str(round(trauma)))
print("El valor destinado a Pediatría es : " + str(round(pediatra)))



# 12 Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
#    que consiste en dejar gratis el alquiler de una película. Realice un
#    programa en Java que teniendo como dato de entrada el total de
#    películas alquiladas, y el número de días de alquiler, determine el
#    monto a pagar.

print ("Ejercicio 12")

cantidadPeliculas = int(input("Digite el numero de peliculas a alquilar "))
cantidadDias = int(input("Digite el numero de dias "))
total = (cantidadPeliculas - 1) * 1500 * cantidadDias;
print("El monto a pagar es : $"+ str(total))


# 13 Una Agencia de viajes cobra por un Tour a Cartagena $25.000
#    diarios por persona. Realice un programa en Java que determine el
#    monto a pagar por una familia que desee realizar dicho Tour
#    sabiendo que también cobran el 12% de IVA.

print ("Ejercicio 13")

cantidadPersonas=float(input("Digite la cantidad de personas "))
cantidadDias=float(input("Digite la cantidad de dias "))
precio=((cantidadPersonas*cantidadDias)*25000)*1.12
print("El total a pagar es de : $" + str(round(precio)))


# 14 Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
#    clientes. Cobra por una habitación $100.000 el primer día y por el
#    resto $200.000 por día. Realice un programa en Java que determine
#    el valor total a pagar por la habitación si la estadía fue de varios
#    días.

print ("Ejercicio 14")
cantidadDias=float(input("Digite la cantidad de dias "))
if cantidadDias < 2 :
    total=100,000
else:
    total=(100000)+(200000)*cantidadDias
print("El total a pagar sera de : $" + str(round(total)))

# 15 El banco del Pueblo da microcréditos a empresarios para ser
#    cancelados en un lapso de 2 años (24 meses). Al monto del 
#    préstamo se le cobra un interés del 24%. El empresario debe pagar
#    la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
#    cuotas ordinarias. Realice un algoritmo que teniendo como dato de
#    entrada el monto del préstamo, determine el monto total a pagar por
#    el préstamo, el monto de las cuotas especiales y el monto de las
#    cuotas ordinarias.

print ("Ejercicio 15")

cantidadPrestada=float(input("Digite la cantidad a prestar "))
totalPago=cantidadPrestada*1.24
primeras=totalPago*0.125
finales=totalPago*0.05
print("El valor de las cuotas especiales iniciales es de : $" + str(round(primeras)))
print("El valor de las cuotas ordinarias finales es de : $" + str(round(finales)))
print("El valor total a pagar es de : $" + str(round(totalPago)))
























