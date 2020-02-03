# 6. Crea una función para calcular el IVA de un producto. Deberá recibir un precio y devolver el precio IVA incluido.

print("Ejercicio 6")

def IVA (precio):
    nuevo_precio=precio*1.21
    return nuevo_precio

precio = float (input("Introduzca el precio sin IVA: "))

precio_con_IVA = IVA(precio)
print("El precio con IVA es: " + str(precio_con_IVA))