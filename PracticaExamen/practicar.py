try:
    altura = int(input("Introduce la altura de la figura: "))
    if altura < 0:
        print("Numero negativo no válido")
except ValueError:
    print("Introduce un número entero positivo.")
    exit()
else:
    espacio = " "
    asterisco = "*"
    print(asterisco*(altura))
    for i in range(1, altura//2):
        print((espacio*(altura)) + asterisco + (espacio*(altura//2)))
    print(asterisco*(altura*2))
    for i in range(1, altura//2):
        print((espacio*altura) + asterisco + (espacio*(altura//2)))