"""Se ingresan las medidas de frente y fondo de un terreno.
Determinar si es cuadrado o rectangular y calcular su superficie."""


frente = float(input("Ingrese medidad del frente en m: "))
fondo = float(input("Ingrese medidad del fondo en m: "))

sup=fondo*frente

if fondo==frente:
  print("Es un cuadrado")
  
else:
  print("Es un rectangulo")
  
print("La superficie total es:",sup,"m")
