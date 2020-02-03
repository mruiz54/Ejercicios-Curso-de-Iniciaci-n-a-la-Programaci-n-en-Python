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