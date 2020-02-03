# 8. Crea una función que reciba un número y calcule si es primo o no.

print("Ejercicio 8")

import math

def Es_primo (numero):
    primo = True
    i=2
    if numero < 2:
        primo = False
    else:
        while primo and i<=math.sqrt(numero):
            if numero%i==0:
               primo=False
            i=i+1
    return primo

numero = int(input("Introduzca un número: "))

primo = Es_primo(numero)

if primo:
    print("El número introducido es primo")
else:
    print("El número introducido no es primo")