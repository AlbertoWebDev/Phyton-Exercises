try: 
    nombre = str(input("Introduce tu nombre: "))
    apellido1 = str(input("Introduce tu primer apellido: "))
    apellido2 = str(input("Introduce tu segundo apellido: "))
except ValueError:
    print("Introduce letras.")
else:
    arrNombre = [nombre]
    arrApellido1 = [apellido1]
    arrApellido2 = [apellido2]
    try:
        inicialNombre = arrNombre.pop(0)
        inicialApellido1 = arrApellido1.pop(0)
        inicialApellido2 = arrApellido2.pop(0)
        print("Tus iniciales son: " + inicialNombre[0].upper() + inicialApellido1[0].upper() + inicialApellido2[0].upper())
    except IndexError:
        print("Error al obtener las iniciales.")
