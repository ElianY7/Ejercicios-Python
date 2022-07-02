precio=float(input("Ingrese el precio de lista: "))

precio_cont=precio*(1 - 0.1) #Descuento del 10%

precio_tar=precio*(1 + 0.05) #Recargo 5%

print("El precio con descuento por contado es:",precio_cont)
print("El precio con recargo por tarjeta es:",precio_tar)
