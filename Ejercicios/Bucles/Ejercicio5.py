# 5. Calcula e imprime la suma de la serie 50+48+46+ … +20.

print("Ejercicio 5")

suma=0
for i in range(50, 20, -2):
    suma+=i
    print(suma)