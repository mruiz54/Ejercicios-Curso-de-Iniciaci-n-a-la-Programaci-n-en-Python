# Operaciones

# 1. Pedir dos números por teclado e imprimir la suma de ambos.

print("Ejercicio 1")

def sumar (numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado

numero_1 = float(input("Introduce el primer número: "))
numero_2 = float(input("Introduce el segundo número: "))

resultado = sumar (numero_1, numero_2)

print ("El resultado es: " + str(resultado))

# 2. Pedir dos números por teclado e imprimir la media aritmética.

print("Ejercicio 2")

def media (num_1, num_2):
    resultado = sumar (num_1, num_2)
    media = resultado / 2
    return media

num_1 = float(input("Introduce el primer número: "))
num_2 = float(input("Introduce el segundo número: "))

resultado = media (num_1, num_2)

print("La media de ambos números es: " + str(resultado))

# 3. Pedir peso y altura para calcular la masa corporal: mc = peso / altura^2.

print("Ejercicio 3")

def masa_corporal (peso, altura):
    mc=peso/(altura^2)
    return mc

peso = int(input("Introduzca su peso: "))
altura = int(input("Introduzca su altura: "))

resultado=masa_corporal(peso, altura)

print ("Su masa corporal es: " + str(resultado))

# 4. Pedir radio para calcular la circunferencia de un círculo: C = 2*PI*r.

print("Ejercicio 4")

PI = 3.14159265358979323846

def longitud_circunferencia (radio):
    C=2*PI*radio
    return C

radio = float(input("Introduzca el radio de su circunferencia: "))

longitud = longitud_circunferencia(radio)

print("La longitud de su circunferencia es: " + str(longitud))

# 5. Pedir un número en Celsius y convertir a Fahrenheit: F = 1.8*C + 32.

print("Ejercicio 5")

def Convertir (temperatura):
    F = 1.8*temperatura + 32
    return F

temperatura = float(input("Introduzca la temperatura en grados Celsius: "))

convertida = Convertir(temperatura)

print("La temperatura introducida convertida a grados Fahrenheit es: " + str(convertida))
