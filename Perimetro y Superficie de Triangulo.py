x=float(input("Ingrese valor de x: "))
y=float(input("Ingrese valor de y: "))
z=float(input("Ingrese valor de z: "))

per=x+y+z #El perimetro es la suma de los tres lados

s=per/2 #El semiperimetro es la mitad del perimetro

sup=(s*(s-x)*(s-y)*(s-z))**(1/2) #Formula de Heron para saber la superficie

print("El valor del permitro es:",per,"Cm")
print("El valor de la superficie es:",sup,"Cm")
