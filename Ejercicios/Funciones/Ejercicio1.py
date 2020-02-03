# 1. Crea una función que reciba un número e imprima si es par o impar.

print("Ejercicio 1")

def Es_par (numero):
    if numero%2==0 :
        print("El número introducido anteriormente es par.")
    else :
        print("El número introducido anteriormente es impar.")

numero = int(input("Introduzca un número: "))
Es_par(numero)