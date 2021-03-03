
cantidadPrestada=float(input("Digite la cantidad a prestar "))
totalPago=cantidadPrestada*1.24
primeras=totalPago*0.125
finales=totalPago*0.05
print("El valor de las cuotas especiales iniciales es de : $" + str(round(primeras)))
print("El valor de las cuotas ordinarias finales es de : $" + str(round(finales)))
print("El valor total a pagar es de : $" + str(round(totalPago)))