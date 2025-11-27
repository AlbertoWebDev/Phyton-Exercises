try:
    correctas = int(input("Introduce el número de respuestas correctas: "))
    incorrectas = int(input("Introduce el número de respuestas incorrectas: "))
    en_blanco = int(input("Introduce el número de respuestas en blanco: "))

    if correctas < 0 or incorrectas < 0 or en_blanco < 0:
        print("Error: El número de respuestas no puede ser negativo.")
        correctas = None
    
except ValueError:
    print("Error: Asegúrate de introducir números enteros válidos.")

else:
    if correctas is not None:
        puntos_correctas = correctas * 5

        puntos_incorrectas = incorrectas * -1

        puntos_blanco = en_blanco * 0
        
        nota_final = puntos_correctas + puntos_incorrectas + puntos_blanco

        print("Puntos por respuestas correctas: " + str(puntos_correctas))
        print("Puntos por respuestas incorrectas: " + str(puntos_incorrectas))
        print("Puntos por respuestas en blanco: " + str(puntos_blanco))
        print("La nota final obtenida por el estudiante es: " + str(nota_final) + " puntos.")

