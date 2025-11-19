postulante = input("Ingresa el nombre del postulante: ")
facultad = input("Ingresa la facultad: ").lower()

# Switch con diccionario para categorizar matrículas
facultades = {
    "ing de sistemas": {"importe": 350, "mensualidad": 650},
    "derecho": {"importe": 300, "mensualidad": 500},
    "ing naviera": {"importe": 300, "mensualidad": 1000},
    "ing pesquera": {"importe": 310, "mensualidad": 460},
    "contabilidad": {"importe": 280, "mensualidad": 520},
    "administracion": {"importe": 360, "mensualidad": 520}
}

if facultad in facultades:
    importe = facultades[facultad]["importe"]
    mensualidad = facultades[facultad]["mensualidad"]
    
    # Calcular IGV 18%
    subtotal = importe + mensualidad
    igv = subtotal * 0.18
    monto_final = subtotal + igv
    
    # Mostrar resultados
    print("\n--- Resumen de Matrícula ---")
    print("Postulante:" + postulante)
    print(f"Facultad: {facultad.capitalize()}")
    print(f"Importe: {importe:.2f}")
    print(f"Mensualidad: {mensualidad:.2f}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"IGV 18%: {igv:.2f}")
    print(f"Monto Final a Pagar: {monto_final:.2f}")
else:
    print("Facultad no encontrada. Verifique el nombre.")
