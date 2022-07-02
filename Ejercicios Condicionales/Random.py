import random

numero_azar = random.randint(0,9) #Esto genera un numero entero al azar entre 0 y 9

print("El numero aleatorio es:", numero_azar)

lista = ["Rojo","Verde","Amarillo","Azul","Negro","Blanco"]

color_random = random.choice(lista) #choice elige entre una lista de elementos

print("El color al azar es:", color_random)
