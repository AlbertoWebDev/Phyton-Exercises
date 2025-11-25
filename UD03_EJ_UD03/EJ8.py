try:
    sueldo_base = float(input("Introduce el sueldo base mensual: "))
    
    venta1 = float(input("Introduce el monto de la Venta 1: "))
    venta2 = float(input("Introduce el monto de la Venta 2: "))
    venta3 = float(input("Introduce el monto de la Venta 3: "))

    if sueldo_base < 0 or venta1 < 0 or venta2 < 0 or venta3 < 0:
        print("Error: Todos los montos deben ser positivos.")
        sueldo_base = None 
    
except ValueError:
    print("Error: Introduce solo números válidos para los montos.")
else:
    if sueldo_base is not None:
        total_ventas = venta1 + venta2 + venta3

        comision = total_ventas * 0.10

        sueldo_total = sueldo_base + comision
        print("Monto total de las 3 ventas: " + str(total_ventas) + " unidades monetarias")
        print("Comisiones (10%): " + str(comision) + " unidades monetarias")
        print("Sueldo Base: " + str(sueldo_base) + " unidades monetarias")
        print("Sueldo Total a recibir: " + str(sueldo_total) + " unidades monetarias")