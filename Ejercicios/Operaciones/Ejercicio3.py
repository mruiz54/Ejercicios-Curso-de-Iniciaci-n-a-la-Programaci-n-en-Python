# 3. Pedir peso y altura para calcular la masa corporal: mc = peso / altura^2.

print("Ejercicio 3")

def masa_corporal (peso, altura):
    mc=peso/(altura^2)
    return mc

peso = int(input("Introduzca su peso: "))
altura = int(input("Introduzca su altura: "))

resultado=masa_corporal(peso, altura)

print ("Su masa corporal es: " + str(resultado))