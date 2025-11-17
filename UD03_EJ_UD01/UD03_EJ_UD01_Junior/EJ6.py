precio = float(input("Introduce el precio del artículo: "))
precio_venta = float(input("Introduce el precio de venta real: "))
descuento = 100 - (precio_venta * 100) / precio
print("El porcentaje de descuento realizado es: ", descuento)