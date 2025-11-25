try:
    v1 = int(input("Introduce la velocidad en km/h del primer vehículo: "))
    v2 = int(input("Introduce la velocidad en km/h del segundo vehículo (el que va atrás): "))
    distancia = int(input("Ingresa la distancia entre ambos coches (km)."))
except ValueError:
    print("No has introducido valores íntegros.")
    exit()
else:
    d = abs(distancia)
    if (v2 == v1):
        print("Ambos vehículos viajan a la misma velocidad. No puede retomarse el código.")
        exit()
    elif (v2 < v1):
        print("El vehículo de atrás (" + str(v2) + " km/h) no es más rápido que el de adelante (" + str(v1) + " km/h). Nunca lo alcanzará.")        
        exit()
    elif (v2 > v1):
        velRelativa = v2 - v1
        tiempoHoras = d / velRelativa
        tiempoMinutos = tiempoHoras * 60
        print("El vehículo de atrás alcanzará al de adelante en " + str(round(tiempoHoras, 2)) + " horas (" + str(round(tiempoMinutos, 2)) + " minutos).")
        exit()