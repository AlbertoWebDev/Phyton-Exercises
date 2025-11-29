opcion = None

while opcion != 4:
    print("1. Abrir Archivo")
    print("2. Guardar Datos")
    print("3. Configuración")
    print("4. Salir del Programa")    
    try:
        opcion = int(input("Introduce el número de tu opción (1-4): "))
    except ValueError:
        print("Error, introduce un número entero para seleccionar la opción.")
        continue
    
    if opcion == 1:
        print("Opción 1 seleccionada: Abriendo el archivo...")
    elif opcion == 2:
        print("Opción 2 seleccionada: Guardando datos en el sistema...")
    elif opcion == 3:
        print("Opción 3 seleccionada: Accediendo a la configuración avanzada...")
    elif opcion == 4:
        print("Opción 4 seleccionada. Saliendo del programa. ¡Hasta pronto!")
    else:
        print("Opción inválida. Por favor, selecciona un número entre 1 y 4.")