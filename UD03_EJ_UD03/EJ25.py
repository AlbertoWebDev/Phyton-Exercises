try:
    cadena = input("introduce un carácter: ")
    
except ValueError:
    print("error al leer la entrada.")
    
else:
    
    if len(cadena) != 1:
        print("error: por favor, introduce solo un carácter.")
        
    elif cadena.isupper():
        print("el carácter '" + cadena + "' es una letra mayúscula.")
        
    else:
        print("el carácter '" + cadena + "' no es una letra mayúscula.")