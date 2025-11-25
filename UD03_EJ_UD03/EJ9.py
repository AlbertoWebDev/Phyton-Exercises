compra = int(input("Ingrese el costo total de la compra: ") )
if compra <=0:
    print("El valor ingresado no es válido.")
else:
    descuento = compra * 0.15
    precio = compra - descuento
    print("El precio final con el descuento aplicado es: ", precio)