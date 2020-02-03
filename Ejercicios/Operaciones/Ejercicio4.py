# 4. Pedir radio para calcular la circunferencia de un círculo: C = 2*PI*r.

print("Ejercicio 4")

PI = 3.14159265358979323846

def longitud_circunferencia (radio):
    C=2*PI*radio
    return C

radio = float(input("Introduzca el radio de su circunferencia: "))

longitud = longitud_circunferencia(radio)

print("La longitud de su circunferencia es: " + str(longitud))