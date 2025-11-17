num = float(input("Ingrese una calificación numérica entre 0 y 10: "))
if 0 <= num <= 10:
    if num < 3:
        print("Calificación: Muy Deficiente")
    if 3 <= num < 5:
        print("Calificación: Insuficiente")
    if 5 <= num < 6:
        print("Calificación: Suficiente")
    if 6 <= num < 7:
        print("Calificación: Bien")
    if 7 <= num < 9:
        print("Calificación: Notable")
    if 9 <= num <= 10:
        print("Calificación: Sobresaliente")
else:
    print("Error: La calificación debe estar entre 0 y 10.")