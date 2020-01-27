# Funciones

# 1. Crea una función que reciba un número e imprima si es par o impar.

print("Ejercicio 1")

def Es_par (numero):
    if numero%2==0 :
        print("El número introducido anteriormente es par.")
    else :
        print("El número introducido anteriormente es impar.")

numero = int(input("Introduzca un número: "))
Es_par(numero)

# 2. Modifica la función anterior para que en vez de imprimirlo lo devuelva.

print("Ejercicio 2")

def Es_par (numero):
    if numero%2==0 :
        par=True
    else :
        par=False
    return par

numero = int(input("Introduzca un número: "))
par=Es_par(numero)

if par:
    print("El número introducido anteriormente es par.")
else :
    print("El número introducido anteriormente es impar.")

# 3. Crea una función que reciba 2 números, devuelve el mayor e imprímelo.

print("Ejercicio 3")

def Es_mayor (numero_1, numero_2):
    mayor=numero_1
    
    if numero_2 > numero_1 :
        mayor=numero_2
    return mayor

numero_1 = float (input("Introduzca el primer número: "))
numero_2 = float (input("Introduzca el segundo número: "))

mayor=Es_mayor(numero_1, numero_2)
print ("El mayor de los dos números es: " + str(mayor))

# 4. Crea una función que reciba 2 números y devuelva el resto de la división del primer número dividido entre el segundo. Imprime el resultado.

print("Ejercicio 4")

def Resto (numero_1, numero_2):
    resto=numero_1%numero_2
    return resto

numero_1 = float (input("Introduce el primer número: "))
numero_2 = float (input("Introduce el segundo número: "))

resultado=Resto (numero_1, numero_2)
print("El resto de la división del primer número entre el segundo es: " + str(resultado))

# 5. Crea una función que reciba la base y la altura de un triángulo y devuelva su área. A = ½ bh.

print("Ejercicio 5")

def Área_triángulo (base, altura):
    A = 0.5*base*altura
    return A
    
base = float (input("Introduzca la base del triángulo: "))
altura = float (input("Introduzca la altura del triángulo: "))

Area=Área_triángulo(base, altura)
print("El área del triángulo con los datos introducidos es: " + str(Area))

# 6. Crea una función para calcular el IVA de un producto. Deberá recibir un precio y devolver el precio IVA incluido.

print("Ejercicio 6")

def IVA (precio):
    nuevo_precio=precio*1.21
    return nuevo_precio

precio = float (input("Introduzca el precio sin IVA: "))

precio_con_IVA = IVA(precio)
print("El precio con IVA es: " + str(precio_con_IVA))

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
