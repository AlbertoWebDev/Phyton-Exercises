print("Bienvenido a Tiendas Don Pepe!")
compra = float(input("Ingrese el monto de compra: "))
dia = input("Ingrese el día de la semana en la que va a realizar la compra: ").lower()
if dia == "martes" or dia ==  "jueves":
    descuento = compra * 0.15
    total = compra - descuento
    print("El total a pagar con descuento es:", total)