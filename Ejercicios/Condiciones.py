# Condiciones

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

# 2. Pedir un número por teclado y decir si es par o impar.

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

# 3. Pedir tres números por teclado e imprimir el mayor de ellos solamente.

print("Ejercicio 3")

def Elige_el_mayor (numero_1, numero_2, numero_3):
    if numero_1 > numero_2:
        if numero_1 > numero_3:
            mayor = numero_1
        else :
            mayor = numero_3
    else :
        if numero_2 > numero_3:
            mayor = numero_2
        else :
            mayor = numero_3
    return numero_3

numero_1 = float(input("Introduce el primer número: "))
numero_2 = float(input("Introduce el segundo número: "))
numero_3 = float(input("Introduce el tercer número: "))

grande = Elige_el_mayor (numero_1, numero_2, numero_3)

print("El mayor número de los tres es el: " + str(grande))

# 4. Pedir un número por pantalla y decir si está entre 10 y 15 o no.

print("Ejercicio 4")

def Esta_entre (numero, inf, superior):
	entre = False
	if numero < superior:
		if numero > inf:
			entre = True
	return entre

numero = float(input("Introduce un numero: "))
esta = Esta_entre (numero, 10, 15)

if esta:
	print("El número introducio está entre 10 y 15")
else:
	print("El número introducido no está entre 10 y 15")

# 5. Pedir lado y alto de un cuadrilátero y decir si es cuadrado o rectángulo.

print("Ejercicio 5")

def Es_cuadrado (lado, alto):
	cuadrado = False
	if lado == alto:
		cuadrado = True
	return cuadrado

lado = float(input("Introduce el lado del cuadrilátero: "))
alto = float(input("Introduce la altura del cuadrilátero: "))

cuadrado = Es_cuadrado (lado, alto)

if cuadrado:
	print("El cuadrilátero es un cuadrado")
else:
	print("El cuadrilátero es un rectángulo")

