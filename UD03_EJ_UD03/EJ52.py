while True:
    try:
        num_trabajadores = int(input("Introduce el número de empleados (N) a procesar: "))
    except ValueError:
        print("Error, debes introducir un número entero.")
        continue
    
    if num_trabajadores > 0:
        break
    else:
        print("Error, el número de trabajadores debe ser mayor que cero.")


pago_total_empresa = 0.0
contador_empleados = 0


while contador_empleados < num_trabajadores:
    
    contador_empleados = contador_empleados + 1
    
    print("\nProcesando Empleado Número:", contador_empleados)
    
    while True:
        try:
            tarifa_por_hora = float(input("Introduce la tarifa de pago por hora (€/hora): "))
        except ValueError:
            print("Error, la tarifa debe ser un número válido.")
            continue
        
        if tarifa_por_hora >= 0:
            break
        else:
            print("Error, la tarifa debe ser un valor positivo o cero.")

    total_horas_empleado = 0.0
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("Introduce las horas trabajadas en la semana:")
    
    for dia in dias_semana:
        while True:
            try:
                horas_dia = float(input("Horas trabajadas el " + dia + ": "))
            except ValueError:
                print("Error, debes introducir un número válido para las horas.")
                continue
            
            if horas_dia >= 0:
                total_horas_empleado = total_horas_empleado + horas_dia
                break
            else:
                print("Error, la cantidad de horas debe ser un valor positivo o cero.")

    sueldo_semanal = total_horas_empleado * tarifa_por_hora

    pago_total_empresa = pago_total_empresa + sueldo_semanal

    print("\n--- Sueldo Semanal del Empleado", contador_empleados, "---")
    print("Horas Trabajadas:", f"{total_horas_empleado:.2f}")
    print("Sueldo Semanal:", f"{sueldo_semanal:.2f} €")

print("Número de empleados procesados:", num_trabajadores)
print("Pago TOTAL de la empresa a los N empleados:", f"{pago_total_empresa:.2f} €")