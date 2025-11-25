print("Notas finales de Algoritmos: ")
try:
    parcial1 = float(input("Introduce la calificación del primer parcial: "))
    parcial2 = float(input("Introduce la calificación del segundo parcial: "))
    parcial3 = float(input("Introduce la calificación del tercer parcial: "))

    examen = float(input("Introduce la nota del examen final: "))
    trabajo = float(input("Introduce la nota del trabajo final: "))
except ValueError:
    print("Alguna de las notas introducidas no son válidas.")
else:
    if not all(0 <= n <= 10 for n in (parcial1, parcial2, parcial3, examen, trabajo)):
        print("Las notas no están entre 0 y 10.")
    else:
        parciales = (parcial1 + parcial2 + parcial3) / 3
        notaParciales = parciales * 0.55
        notaExamen = examen * 0.30
        notaTrabajo = trabajo * 0.15
        notaFinal = notaParciales + notaExamen + notaTrabajo
        print("Nota final: " , notaFinal)

