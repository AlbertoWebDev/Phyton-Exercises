print("Introduce caracteres uno por uno. El programa terminará cuando introduzcas un espacio (' ').")
while True:
    
    caracter = input("Introduce un carácter: ").strip()

    if caracter == ' ':
        print("\n¡Espacio introducido! Fin del programa.")
        break

    if len(caracter) != 1:
        print("Por favor, introduce solo UN carácter a la vez.")
        continue # Vuelve a pedir un carácter
        
    caracter_minuscula = caracter.lower()
    
    vocales = 'aáeéiíoóuú'
    
    if caracter_minuscula in vocales:
        print("El carácter", caracter, "es: VOCAL")
    else:
        print("El carácter", caracter, "es: NO VOCAL")