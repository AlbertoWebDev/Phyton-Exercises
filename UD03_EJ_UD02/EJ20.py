try:
    cantidad = int(input("Introduce un número múltiplo de 5:"))
except ValueError:
    print("ERROR: Debes introducir un número entero.")
else:
    if cantidad < 0 or cantidad % 5 != 0:
        print("ERROR: El número debe ser un múltiplo positivo de 5.")
    elif cantidad == 0:
        print("No se necesita ningún billete.")
    else:
        billetes = [500, 200, 100, 50, 20, 10, 5]
        restante = cantidad
        desglose = {}
        for b in billetes:
            cuenta = restante // b
            if cuenta > 0:
                desglose[b] = cuenta
                restante -= cuenta * b

        print("Desglose de billetes para " + str(cantidad) + "€:")
        for b in billetes:
            if b in desglose:
                c = desglose[b]
                if c == 1:
                    print("1 billete de " + str(b) + "€")
                else:
                    print(str(c) + " billetes de " + str(b) + "€")
