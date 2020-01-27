def CalculoFactorial (numero):
    factorial=1
    for i in range (numero,1,-1):
        factorial=factorial*i
    return factorial

numero=int(input("Introduce un número entero: "))
fact=CalculoFactorial(numero)
print("El factorial del número "+str(numero)+" es: "+str(fact))