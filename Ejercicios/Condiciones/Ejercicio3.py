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