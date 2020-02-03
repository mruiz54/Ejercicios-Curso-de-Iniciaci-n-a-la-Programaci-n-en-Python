# 7. Crea una función que reciba un número, calcule su factorial, devuelva el resultado e imprímelo.

print("Ejercicio 7")

def Factorial (numero):
    producto=1
    for i in range (numero,1,-1):
        producto*=i
    return producto

numero = int (input("Introduzca un número: "))

factorial = Factorial(numero)
print("El factorial del número introducido es: " + str(factorial))