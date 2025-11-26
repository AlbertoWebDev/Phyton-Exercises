respuestasCorrectas = int(input("En el test de 10 preguntas, ¿Cuántas has acertado?"))
respuestasIncorrectas = int(input("¿Cuántas has fallado?"))
respuestasEnBlanco = int(input("¿Cuántas has dejado en blanco?"))
if respuestasCorrectas + respuestasIncorrectas + respuestasEnBlanco != 10:
    print("El total de respuestas no es correcto. Debe sumar 10.")
if respuestasCorrectas < 0 or respuestasCorrectas > 10:
    print("Número de respuestas no válido. Debe estar entre 0 y 10.")