# 4. Calcula e imprime el producto de la serie 2x4x6x8x … x20.

print("Ejercicio 4")

producto=1
for i in range(2,20):
    if i%2==0:
        producto*=i
        print(producto)