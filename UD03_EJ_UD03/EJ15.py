try:   
    A = int(input("Introduce la primera variable numérica: "))
    B = int(input("Introduce la segunda variable numérica: "))
except ValueError:
    print("No has introducido variables numéricas.")
else:
    if (A == B):
        print("Ambas variables son iguales.")
    else:
        primerValor = A
        segundoValor = B
        A = segundoValor
        B = primerValor
        primerValor = B
        segundoValor = A
        print("Las variables intercambiadas son A: ", A, " y B: ", B)