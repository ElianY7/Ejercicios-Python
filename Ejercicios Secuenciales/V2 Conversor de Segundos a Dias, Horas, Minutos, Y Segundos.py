sec=int(input("Ingrese segundos a convertir: "))

dias=sec//86400    #Hay 86400 segundos en un día

horas=(sec%86400)//3600    #Hay 3600 segundos en una hora

minutos=((sec%86400)%3600)//60    #Hay 60 segundos en un minuto

segundos=((sec%86400)%3600)%60

print("Hay",dias,"dias,",horas,"horas,",minutos,"minutos y",segundos,"segundos.")
