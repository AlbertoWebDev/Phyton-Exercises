pago_mes_actual = 10.0
pago_total_acumulado = 0.0
meses_a_pagar = 20

print("\nInicio de la progresión: Primer pago =", pago_mes_actual, "€")

for mes in range(1, meses_a_pagar + 1):

    print("Mes", mes, ": Pagar", f"{pago_mes_actual:.2f} €")

    pago_total_acumulado = pago_total_acumulado + pago_mes_actual
    
    pago_mes_actual = pago_mes_actual * 2

print("Total de meses de pago:", meses_a_pagar)
print("TOTAL PAGADO después de los 20 meses:", f"{pago_total_acumulado:.2f} €")