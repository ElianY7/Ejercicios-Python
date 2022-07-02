sec=int(input("Ingrese segundos a convertir: "))

dias=sec//86400    #Hay 86400 segundos en un día
sec%=86400

horas=sec//3600    #Hay 3600 segundos en una hora
sec%=3600

minutos=sec//60    #Hay 60 segundos en un minuto
sec%=60

print("Hay",dias,"dias,",horas,"horas,",minutos,"minutos y",sec,"segundos.")
