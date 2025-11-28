import random

numero_secreto = random.randint(1, 100)

intentos_maximos = 10
intentos_restantes = intentos_maximos

adivinado = False

while intentos_restantes > 0 and not adivinado:
    
    print("\nIntentos restantes:", intentos_restantes)
    
    try:
        suposicion = int(input("Introduce tu número (entre 1 y 100): "))
    except ValueError:
        print("Debes introducir un número entero.")
        intentos_restantes -= 1
        continue # Vuelve al inicio del bucle

    if suposicion < 1 or suposicion > 100:
        print("AVISO: El número debe estar entre 1 y 100. Pierdes un intento.")
        intentos_restantes -= 1
        continue # Vuelve al inicio del bucle
        
    intentos_restantes -= 1
    intentos_usados = intentos_maximos - intentos_restantes
    
    if suposicion == numero_secreto:
        adivinado = True
        
    elif suposicion < numero_secreto:
        print("El número secreto es MAYOR que", suposicion, ".")
        
    elif suposicion > numero_secreto:
        print("El número secreto es MENOR que", suposicion, ".")




if adivinado:
    print("Lo has adivinado!")
    print("El número era:", numero_secreto)
    print("Lo has acertado en", intentos_usados, "intentos.")
else:
    print("Has agotado tus", intentos_maximos, "intentos.")
    print("El número secreto generado era:", numero_secreto)