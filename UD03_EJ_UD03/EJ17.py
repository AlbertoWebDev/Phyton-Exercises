try:
    hora = int(input("Introduce la hora a la que el ciclista parte de la ciudad: "))
    minutos = int(input("Introduce los minutos a la que el ciclista parte de la ciudad: "))
    segundos = int(input("Introduce los segundos a la que el ciclista parte de la ciudad: "))
    tiempoViajeSeg = int(input("Introduce cuantos segundos tardará en llegar a su ciudad destino: "))
except ValueError:
    print("No has introducido un número íntegro.")
else:
    if (0 <= hora <=23 and 0 <= minutos <= 59 and 0 <= segundos <= 59):
        segundos_partida = (hora * 3600) + (minutos * 60) + segundos
        
        segundos_llegada_total = segundos_partida + tiempoViajeSeg
                
        hora_llegada = (segundos_llegada_total // 3600) % 24
        
        minutos_llegada = (segundos_llegada_total % 3600) // 60
        
        segundos_llegada = segundos_llegada_total % 60
        
        print("\nHora de Llegada: ")
        print("El ciclista llegó a la Ciudad B a las: " + str(hora_llegada) + " horas, " + str(minutos_llegada) + " minutos y " + str(segundos_llegada) + " segundos.")
    else:
        print("No has introducido una hora correcta.")