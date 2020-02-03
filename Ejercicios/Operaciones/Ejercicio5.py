# 5. Pedir un número en Celsius y convertir a Fahrenheit: F = 1.8*C + 32.

print("Ejercicio 5")

def Convertir (temperatura):
    F = 1.8*temperatura + 32
    return F

temperatura = float(input("Introduzca la temperatura en grados Celsius: "))

convertida = Convertir(temperatura)

print("La temperatura introducida convertida a grados Fahrenheit es: " + str(convertida))