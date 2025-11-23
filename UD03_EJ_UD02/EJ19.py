print("Piensa un número entre 1 y 100.")
print("Responde 'mayor' si tu número es mayor que mi intento, 'menor' si es menor, 'igual' si coincide.")

minimo = 1
maximo = 100
intentos = 0

while minimo <= maximo:
    intento = (minimo + maximo) // 2
    intentos += 1

    while True:
        respuesta = input("Intento #" + str(intentos) + ": ¿Es " + str(intento) + "? (mayor/menor/igual): ").strip().lower()
        if respuesta in ("mayor", "menor", "igual"):
            break
        print("Respuesta no válida. Escribe 'mayor', 'menor' o 'igual'.")

    if respuesta == "igual":
        print("He adivinado tu número (" + str(intento) + ") en " + str(intentos) + " intentos.")
        break
    elif respuesta == "mayor":
        minimo = intento + 1
    else:
        maximo = intento - 1
else:
    print("Error: No has introducido respuestas coherentes.")