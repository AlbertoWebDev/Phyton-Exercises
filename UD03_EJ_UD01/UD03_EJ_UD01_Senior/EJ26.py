import random

# Lanzar tres dados
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

# Contar cuántos dados son seis
cantidad_seis = 0
if dado1 == 6:
    cantidad_seis += 1
if dado2 == 6:
    cantidad_seis += 1
if dado3 == 6:
    cantidad_seis += 1

# Switch con diccionario según cantidad de seis
mensajes = {
    3: "Excelente",
    2: "Muy bien",
    1: "Regular",
    0: "Pésimo"
}

# Obtener mensaje del switch
mensaje = mensajes.get(cantidad_seis, "Error")

# Mostrar resultados
print("--- Resultados del Lanzamiento de Dados ---")
print(f"Dado 1: {dado1}")
print(f"Dado 2: {dado2}")
print(f"Dado 3: {dado3}")
print(f"Cantidad de seis: {cantidad_seis}")
print(f"\nMensaje: {mensaje}")