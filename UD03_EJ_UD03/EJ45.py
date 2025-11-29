limite_inferior = 0
limite_superior = 0
limites_validos = False
while not limites_validos:
    try:
        limite_inferior = int(input("Introduce el límite INFERIOR del intervalo: "))
        limite_superior = int(input("Introduce el límite SUPERIOR del intervalo: "))
    except ValueError:
        print("Error, debes introducir números enteros.")
        continue
    
    if limite_inferior > limite_superior:
        print("Aviso, el límite inferior no puede ser mayor que el superior. Inténtalo de nuevo.")
    else:
        limites_validos = True

print("\nIntervalo definido:", limite_inferior, "a", limite_superior, "(ambos inclusive).")
print("Ahora introduce números. El análisis terminará cuando introduzcas el 0.")

suma_dentro_intervalo = 0
conteo_fuera_intervalo = 0
igual_al_limite_flag = False
primer_numero_introducido = False

while True:
    
    try:
        numero = int(input("Introduce un número (0 para terminar): "))
    except ValueError:
        print("Error, debes introducir un número entero.")
        continue

    if numero == 0:
        if not primer_numero_introducido:
            print("Programa finalizado. No se analizaron números distintos de cero.")
        break
    
    primer_numero_introducido = True

    if numero > limite_inferior and numero < limite_superior:
        suma_dentro_intervalo = suma_dentro_intervalo + numero
        
    elif numero == limite_inferior or numero == limite_superior:
        igual_al_limite_flag = True
        conteo_fuera_intervalo = conteo_fuera_intervalo + 1

    else:
        conteo_fuera_intervalo = conteo_fuera_intervalo + 1

print("Suma de los números DENTRO del intervalo abierto (", limite_inferior, ", ", limite_superior, "):", suma_dentro_intervalo)

print("Cantidad de números FUERA del intervalo (incluye números iguales a los límites):", conteo_fuera_intervalo)

if igual_al_limite_flag:
    print("Sí, se introdujo al menos un número igual a los límites del intervalo.")
else:
    print("No se introdujo ningún número igual a los límites del intervalo.")