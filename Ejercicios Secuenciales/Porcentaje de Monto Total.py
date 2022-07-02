p1=float(input("Ingrese el monto de la primera persona: "))
p2=float(input("Ingrese el monto de la segunda persona: "))
p3=float(input("Ingrese el monto de la tercera persona: "))

monto_total = p1 + p2 + p3

pp1=(p1*100)/monto_total
pp2=(p2*100)/monto_total
pp3=(p3*100)/monto_total


print("El porcentaje de la primera persona es:",round(pp1,2),"el segundo es:",round(pp2,2),"y el tercero es:",round(pp3,2))
