import random

contador = 0
numero_negativo = False

while contador < 100:
    numero = random.randint(-50, 50)
    print(numero)
    
    if numero < 0:
        numero_negativo = True
    
    contador += 1

if numero_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")