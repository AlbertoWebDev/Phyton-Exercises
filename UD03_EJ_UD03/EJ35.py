try:
    numero_dia = int(input("Introduce el día de la semana (1 = Lunes, 7 = Domingo): "))
except ValueError:
    print("ERROR: Debes introducir un número entero.")
else:
    if 1 <= numero_dia <= 7:
        
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        if numero_dia == 1:
            print("El día correspondiente es: ", dias_semana[0])
        elif numero_dia == 2:
            print("El día correspondiente es: ", dias_semana[1])
        elif numero_dia == 3:
            print("El día correspondiente es: ", dias_semana[2])
        elif numero_dia == 4:
            print("El día correspondiente es: ", dias_semana[3])
        elif numero_dia == 5:
            print("El día correspondiente es: ", dias_semana[4])
        elif numero_dia == 6:
            print("El día correspondiente es: ", dias_semana[5])
        elif numero_dia == 7:
            print("El día correspondiente es: ", dias_semana[6])
            
    else:
        print("No has introducido un número entre 1 y 7.")