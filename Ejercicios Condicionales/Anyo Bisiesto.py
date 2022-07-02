anyo=int(input("Ingrese año a verificar: "))

if anyo % 4 == 0 and (anyo % 100 !=0 or anyo % 400 == 0):
  print("El año",anyo,"es bisiesto")

else:
  print("El año",anyo,"NO es bisiesto")
