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