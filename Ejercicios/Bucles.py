# Bucles

# 1. Imprimir los 25 primeros números naturales.

print("Ejercicio 1")

for i in range(25):
    print(i+1)

# 2. Imprimir los números impares desde el 1 al 25, ambos inclusive.

print("Ejercicio 2")

for i in range(25):
    if (i+1)%2!=0:
        print(i+1)

# 3. Calcula e imprime la suma desde el 14 hasta el 38, ambos inclusive.

print("Ejercicio 3")

suma=0
for i in range(14,38):
    suma+=i
    print(suma)

# 4. Calcula e imprime el producto de la serie 2x4x6x8x … x20.

print("Ejercicio 4")

producto=1
for i in range(2,20):
    if i%2==0:
        producto*=i
        print(producto)

# 5. Calcula e imprime la suma de la serie 50+48+46+ … +20.

print("Ejercicio 5")

suma=0
for i in range(50, 20, -2):
    suma+=i
    print(suma)
