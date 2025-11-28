try:
    tiempo_minutos = float(input("Introduce la duración de la llamada en minutos (ej: 12.5): "))
    dia_semana = input("Introduce el día de la semana (ej: Lunes, Domingo): ").strip().lower()
    turno = ""

    if dia_semana != "domingo":
        turno = input("Introduce el turno (Mañana o Tarde): ").strip().lower()

except ValueError:
    print("Error: La duración de la llamada debe ser un número.")
else:
    if tiempo_minutos <= 0:
        print("La duración de la llamada debe ser un valor positivo.")
    elif dia_semana not in ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"]:
        print("Día de la semana no válido.")
    elif dia_semana != "domingo" and turno not in ["mañana", "tarde"]:
        print("Turno no válido. Debe ser Mañana o Tarde.")
    else:
        
        costo_base = 0.0
        tiempo_restante = tiempo_minutos

        if tiempo_restante >= 5:
            costo_base += 5 * 1.00
            tiempo_restante -= 5
        else:
            costo_base += tiempo_restante * 1.00
            tiempo_restante = 0

        if tiempo_restante > 0:
            if tiempo_restante >= 3:
                costo_base += 3 * 0.80
                tiempo_restante -= 3
            else:
                costo_base += tiempo_restante * 0.80
                tiempo_restante = 0

        if tiempo_restante > 0:
            if tiempo_restante >= 2:
                costo_base += 2 * 0.70
                tiempo_restante -= 2
            else:
                costo_base += tiempo_restante * 0.70
                tiempo_restante = 0

        if tiempo_restante > 0:
            costo_base += tiempo_restante * 0.50 

        tasa_impuesto = 0.0
        
        if dia_semana == "domingo":
            tasa_impuesto = 0.03
        else:
            if turno == "mañana":
                tasa_impuesto = 0.15
            elif turno == "tarde":
                tasa_impuesto = 0.10
                
        monto_impuesto = costo_base * tasa_impuesto
        costo_total = costo_base + monto_impuesto

        print("Duración:", f"{tiempo_minutos:.2f}", "minutos")
        print("Día y Turno:", dia_semana.capitalize(), "-", turno.capitalize() if turno else "")
        print("1. Costo Base por tiempo (antes de impuestos):", f"{costo_base:.2f} €")
        print("2. Tasa de Impuesto Aplicada:", f"{tasa_impuesto * 100:.0f}%")
        print("3. Monto del Impuesto a Pagar:", f"{monto_impuesto:.2f} €")
        print("4. Costo TOTAL Final:", f"{costo_total:.2f} €")