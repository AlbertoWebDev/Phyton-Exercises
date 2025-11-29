ahorro_total_anual = 0.0
registro_mensual = []

print("A continuación, introduce la cantidad depositada al final de cada uno de los 12 meses.")
for mes in range(1, 13):
    
    while True:
        try:
            deposito_mes = float(input("Cantidad depositada en el Mes " + str(mes) + " (euros): "))
        except ValueError:
            print("ERROR: Debes introducir un número válido para el depósito.")
            continue
        
        if deposito_mes >= 0:
            break
        else:
            print("ERROR: La cantidad depositada debe ser un valor positivo o cero.")


    ahorro_total_anual = ahorro_total_anual + deposito_mes
    
    registro_mensual.append({
        "mes": mes,
        "deposito": deposito_mes,
        "acumulado": ahorro_total_anual
    })

for item in registro_mensual:
    print("Mes", item["mes"], ": Depósito de", f"{item['deposito']:.2f} €", 
          "| Ahorro acumulado:", f"{item['acumulado']:.2f} €")
    
print("AHORRO TOTAL AL FINAL DEL AÑO:", f"{ahorro_total_anual:.2f} €")