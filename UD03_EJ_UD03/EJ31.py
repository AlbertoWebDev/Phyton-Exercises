try:
    num_alumnos = int(input("Introduce el número de alumnos que viajarán: "))
except ValueError:
    print("Error: El número de alumnos debe ser un número entero.")
else:
    costo_por_alumno = 0.0
    pago_compania = 0.0

    if num_alumnos <= 0:
        print("El número de alumnos debe ser un entero positivo.")
    elif num_alumnos >= 100:
        costo_por_alumno = 65.0
        pago_compania = num_alumnos * costo_por_alumno
    elif num_alumnos >= 50: 
        costo_por_alumno = 70.0
        pago_compania = num_alumnos * costo_por_alumno
    elif num_alumnos >= 30:
        costo_por_alumno = 95.0
        pago_compania = num_alumnos * costo_por_alumno
    else: # Menos de 30 alumnos
        pago_compania = 4000.0
        costo_por_alumno = pago_compania / num_alumnos
        
    if num_alumnos > 0:
        print("Resultados del Viaje para", num_alumnos, "alumnos:")
        print("Costo que debe pagar cada alumno:", f"{costo_por_alumno:.2f} €")
        print("Pago total a la compañía de autobuses:", f"{pago_compania:.2f} €")