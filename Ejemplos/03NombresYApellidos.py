from random import randint

Nombres=["Pedro","Isabel","Federico","Eufrasio","Jose Luis","Lorenzo","Julia","Manuel","Antonia","Antonio","Ángela","Eladio"]
Apellidos=["Ruiz","Martínez","Coca","Cabrera","Bueno","Olmo","Hidalgo","Mesa"]

indice_nombre=randint(0,11)
indice_apellido=randint(0,7)

print("Nombre y Apellido: "+Nombres[indice_nombre]+" "+Apellidos[indice_apellido])