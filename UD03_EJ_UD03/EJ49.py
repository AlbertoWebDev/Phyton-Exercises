try:
    tarifa_por_hora = float(input("Introduce la tarifa de pago por hora (€/hora): "))
except ValueError:
    print("Error, la tarifa debe ser un número válido.")
    exit()
else:
    if tarifa_por_hora <= 0:
        print("Error, la tarifa por hora debe ser un valor positivo.")
        exit()

total_horas = 0.0
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

print("\nIntroduce las horas trabajadas para cada uno de los seis días:")

for dia in dias_semana:
    
    while True:
        try:
            horas_dia = float(input("Horas trabajadas el " + dia + ": "))
        except ValueError:
            print("ERROR: Debes introducir un número válido para las horas.")
            continue
        
        if horas_dia >= 0:
            total_horas = total_horas + horas_dia
            break
        else:
            print("ERROR: La cantidad de horas debe ser un valor positivo o cero.")

sueldo_semanal = total_horas * tarifa_por_hora

print("Tarifa de pago por hora:", f"{tarifa_por_hora:.2f} €")
print("Total de Horas Trabajadas en la Semana:", f"{total_horas:.2f}")
print("SUELDO TOTAL a recibir por las horas trabajadas:", f"{sueldo_semanal:.2f} €")