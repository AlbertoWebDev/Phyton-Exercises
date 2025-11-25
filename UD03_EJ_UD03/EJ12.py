try:
    x1 = input("Introduce el valor de x1: ")
    y1 = input("Introduce el valor de y1: ")
    x2 = input("Introduce el valor de x2: ")
    y2 = input("Introduce el valor de y2: ")
    distancia = ((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)**0.5
except ValueError:
    print("Error: Por favor, introduce valores numéricos válidos.")
else:
    distanciaAbs = abs(distancia)
    print("La distancia entre los puntos es:", distanciaAbs)