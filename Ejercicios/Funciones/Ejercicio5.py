# 5. Crea una función que reciba la base y la altura de un triángulo y devuelva su área. A = ½ bh.

print("Ejercicio 5")

def Área_triángulo (base, altura):
    A = 0.5*base*altura
    return A
    
base = float (input("Introduzca la base del triángulo: "))
altura = float (input("Introduzca la altura del triángulo: "))

Area=Área_triángulo(base, altura)
print("El área del triángulo con los datos introducidos es: " + str(Area))