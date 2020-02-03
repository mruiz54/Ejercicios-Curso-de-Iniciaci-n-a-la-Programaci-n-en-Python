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