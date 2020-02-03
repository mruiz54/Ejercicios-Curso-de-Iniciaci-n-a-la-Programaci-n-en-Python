# 1. Pedir dos números por teclado e imprimir la suma de ambos.

print("Ejercicio 1")

def sumar (numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado

numero_1 = float(input("Introduce el primer número: "))
numero_2 = float(input("Introduce el segundo número: "))

resultado = sumar (numero_1, numero_2)

print ("El resultado es: " + str(resultado))