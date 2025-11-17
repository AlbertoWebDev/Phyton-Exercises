trabajador = input("Nombre del trabajador: ")
horas = float(input("Horas trabajadas en la semana: "))
tarifa = float(input("Tarifa horaria normal (€/hora): "))

if horas <= 35:
    salario_bruto = horas * tarifa
else:
    horas_normales = 35
    horas_extras = horas - 35
    salario_bruto = (horas_normales * tarifa) + (horas_extras * tarifa * 1.5)

impuesto = 0
salario_restante = salario_bruto

if salario_restante > 500:
    salario_restante -= 500
else:
    salario_restante = 0

if salario_restante > 0:
    tramo_400 = min(salario_restante, 400)
    impuesto += tramo_400 * 0.25
    salario_restante -= tramo_400

if salario_restante > 0:
    impuesto += salario_restante * 0.45

salario_neto = salario_bruto - impuesto

print("\nNómina Semanal del Trabajador")
print("Trabajador: " + trabajador)
print("Horas trabajadas:" + str(horas))
print("Tarifa normal: " + str(tarifa) + "€/hora")
print("Salario bruto: " + str(salario_bruto) + "€")
print("Impuestos: " + str(impuesto) + "€")
print("Salario neto: " + str(salario_neto) + "€")


