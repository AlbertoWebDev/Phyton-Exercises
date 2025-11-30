# Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.
cadena = input("Introduce una cadena de texto: ")
cadenaNueva = ""
vocales = "aeiouAEIOUÁÉÍÓÚáéíóú"
for c in cadena:
    if c in vocales:
        cadenaNueva = cadenaNueva + "*"
    else:
        cadenaNueva = cadenaNueva + c
print("La nueva cadena es: ", cadenaNueva)