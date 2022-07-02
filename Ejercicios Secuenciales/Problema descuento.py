pan_cant=int(input("Cantidad de pan: "))
desc=pan_cant*3.49*0.6
print("El descuento es:",desc)
print("El coste final es:",round(pan_cant*3.49-desc,2))
