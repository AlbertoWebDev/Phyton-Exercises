# Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo).
cadena1 = input("Escribe la primera cadena de texto: ")
cadena2 = input("Escribe la segunda cadena de tedxto: ")
cadenaFinal = ""
for c in cadena1:
    cadenaFinal = cadenaFinal + c
for v in cadena2:
    cadenaFinal = cadenaFinal + v
print("La cadena final es: ", cadenaFinal)