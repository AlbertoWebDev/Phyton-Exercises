try:
    nota = float(input("introduce la nota (0-10): "))
    edad = int(input("introduce la edad: "))
    
    sexo = input("introduce el sexo ('f' o 'm'): ")
    
    if nota < 0 or nota > 10 or edad < 0:
        print("error: nota o edad fuera de rango válido.")
        nota = None
        
except ValueError:
    print("error: la nota debe ser un número y la edad un entero.")

else:
    if nota is not None:

        condicion_nota = nota >= 5.0
        condicion_edad = edad >= 18

        if condicion_nota and condicion_edad:
            
            if sexo.lower() == 'f':
                print("aceptada")
            elif sexo.lower() == 'm':
                print("posible")
            else:
                print("no aceptada (sexo no válido)")
                
        else:
            print("no aceptada")
            print("motivo: nota (" + str(condicion_nota) + ") o edad (" + str(condicion_edad) + ") insuficiente.")