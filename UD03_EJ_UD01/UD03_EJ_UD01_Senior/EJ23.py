valorCompra = float(input("Ingrese el valor de la compra: "))
pago = input("Ingrese el método de pago (efectivo/tarjeta): ").lower()
if pago == "efectivo":
    descuento = valorCompra * 0.05
    totalPagar = valorCompra - descuento
    print("El total a pagar con descuento es:", totalPagar)
elif pago == "tarjeta":
    print("El total a pagar es:", valorCompra)
else:
    print("Método de pago no válido.")