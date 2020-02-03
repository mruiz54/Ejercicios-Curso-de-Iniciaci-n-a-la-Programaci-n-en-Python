# 4. Crea una función que reciba 2 números y devuelva el resto de la división del primer número dividido entre el segundo. Imprime el resultado.

print("Ejercicio 4")

def Resto (numero_1, numero_2):
    resto=numero_1%numero_2
    return resto

numero_1 = float (input("Introduce el primer número: "))
numero_2 = float (input("Introduce el segundo número: "))

resultado=Resto (numero_1, numero_2)
print("El resto de la división del primer número entre el segundo es: " + str(resultado))