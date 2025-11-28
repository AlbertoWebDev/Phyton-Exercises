try:
    dia = int(input("Introduce el día (ej. 15): "))
    mes = int(input("Introduce el mes (ej. 10): "))
    año = int(input("Introduce el año (ej. 2024): "))
except ValueError:
    print("Error: Los valores para la fecha deben ser números enteros.")
else:
    
    fecha_correcta = True
    dias_en_mes = 0
    
    if año < 1 or mes < 1 or mes > 12 or dia < 1:
        fecha_correcta = False
    
    if fecha_correcta:
        
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dias_en_mes = 31
        
        elif mes in [4, 6, 9, 11]:
            dias_en_mes = 30
            
        elif mes == 2:
            
            es_bisiesto = False
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                es_bisiesto = True

            if es_bisiesto:
                dias_en_mes = 29
            else:
                dias_en_mes = 28
        
        if dia > dias_en_mes:
            fecha_correcta = False

    if fecha_correcta:
        print("La fecha", dia, "/", mes, "/", año, "es CORRECTA.")
    else:
        print("La fecha", dia, "/", mes, "/", año, "es INCORRECTA.")