try:
    año = int(input("introduce un año: "))

except ValueError:
    print("error: asegúrate de introducir un número entero válido para el año.")

else:
   
    if año % 400 == 0:
        es_bisiesto = True
    
    elif año % 100 == 0:
        es_bisiesto = False
        
    elif año % 4 == 0:
        es_bisiesto = True
        
    else:
        es_bisiesto = False

    if es_bisiesto:
        print("el año " + str(año) + " es bisiesto.")
    else:
        print("el año " + str(año) + " no es bisiesto.")