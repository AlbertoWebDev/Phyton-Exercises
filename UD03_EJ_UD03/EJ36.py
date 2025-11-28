try:
    mes = int(input("Introduce el número del mes (1 = Enero, 12 = Diciembre): "))
    año = int(input("Introduce el año (ej. 2024) para la correcta validación de Febrero: "))
except ValueError:
    print("ERROR: Debes introducir números enteros para el mes y el año.")
else:
    if 1 <= mes <= 12:
        
        dias_en_mes = 0
        
        
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
        
        if dias_en_mes > 0:
            print("El mes número", mes, "del año", año, "tiene", dias_en_mes, "días.")
            
    else:
        print("Número incorrecto. Por favor, introduce un número entre 1 y 12.")