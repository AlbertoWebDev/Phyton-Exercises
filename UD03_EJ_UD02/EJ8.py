import random

contador = 0
numero_negativo = 0

while contador < 100:
    numero = random.randint(-50, 50)
    print(numero)
    
    if numero < 0:
        numero_negativo += 1
    
    contador += 1

if numero_negativo:
    print("Se ha leído " + str(numero_negativo) + " números negativos.")
else:
    print("No se ha leído ningún número negativo.")