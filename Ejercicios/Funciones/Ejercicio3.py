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