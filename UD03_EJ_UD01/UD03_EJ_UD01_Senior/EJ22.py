hours = int(input("Ingrese las horas (0-23): "))
minutes = int(input("Ingrese los minutos (0-59): "))
seconds = int(input("Ingrese los segundos (0-59): "))
if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
            if hours == 24:
                hours = 0
    print("La hora después de un segundo es: " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
else:
    print("Error: La hora ingresada no es válida.")

