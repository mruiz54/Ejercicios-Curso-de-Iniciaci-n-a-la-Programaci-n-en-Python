def Multiplica_por_dos (numero):
    numero=numero*2
    return numero
def Genera_mensaje(numero):
    cadena="Nuestro número multiplicado por dos es " + str(numero)
    return cadena
def Imprime_mensaje(una_cadena):
    print(una_cadena)
def Imprime_mensaje_inicial():
    print("Este mensaje es solo para dar la bienvenida")
    
Imprime_mensaje_inicial()
numero=int(input("Introduce un número entero: "))
numero=Multiplica_por_dos(numero)
mi_mensaje=Genera_mensaje(numero)
Imprime_mensaje(mi_mensaje)