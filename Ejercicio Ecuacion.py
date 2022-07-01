"""
Se sabe que la suma de dos ángulos desconocidos (α+β) es igual a cierto valor x que se
carga por teclado.
Además se sabe que la diferencia entre esos mismos dos ángulos (α − β) es igual a otro
valor y que también se carga por teclado. Desarrolle un programa que dados los
valores x e y, determine el valor de los dos ángulos α y β.
"""

x=int(input("Ingrese valor de x: "))
y=int(input("Ingrese valor de y: "))

b=(x-y)/2
a=x-b

print("El valor de a es:",a,"y el valor de b es:",b)
