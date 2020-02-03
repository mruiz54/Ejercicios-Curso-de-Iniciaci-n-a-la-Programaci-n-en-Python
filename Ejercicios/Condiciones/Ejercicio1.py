# 1. Pedir dos números por teclado y decir cual es mayor.

print("Ejercicio 1")

def Es_mayor (numero_1, numero_2):
    if numero_1 > numero_2 :
        print("El primer número introducido es mayor que el segundo.")
    elif numero_2 > numero_1 :
        print("El segundo número introducido es mayor que el primero.")
    else :
        print("Ambos números son iguales.")
numero_1 = float (input("Introduce el primero número: "))
numero_2 = float (input("Introduce el segundo número: "))

Es_mayor(numero_1, numero_2)