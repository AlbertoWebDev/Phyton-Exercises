while True:
    try:
        sueldo_base = float(input("Introduce el sueldo base mensual del vendedor (€): "))
    except ValueError:
        print("Error, el sueldo base debe ser un número válido.")
        continue
    
    if sueldo_base >= 0:
        break
    else:
        print("ERROR: El sueldo base debe ser un valor positivo o cero.")

total_ventas = 0.0

print("\nIntroduce el valor de las tres ventas realizadas en el mes:")

for i in range(1, 4):
    while True:
        try:
            venta = float(input(f"Valor de la Venta {i} (€): "))
        except ValueError:
            print("Error, el valor de la venta debe ser un número válido.")
            continue
        
        if venta >= 0:
            total_ventas = total_ventas + venta
            break
        else:
            print("Error, el valor de la venta debe ser positivo o cero.")

tasa_comision = 0.10
comisiones_obtenidas = total_ventas * tasa_comision

sueldo_total_mensual = sueldo_base + comisiones_obtenidas

print("Sueldo Base Mensual:", f"{sueldo_base:.2f} €")
print("Total vendido en el mes (3 ventas):", f"{total_ventas:.2f} €")
print("Comisiones (10 por ciento de las ventas):", f"{comisiones_obtenidas:.2f} €")
print("Total a recibir en el mes (Sueldo + Comisiones):", f"{sueldo_total_mensual:.2f} €")