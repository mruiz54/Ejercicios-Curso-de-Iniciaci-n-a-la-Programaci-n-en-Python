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