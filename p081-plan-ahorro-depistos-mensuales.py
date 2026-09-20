# p081-plan-ahorro-depistos-mensuales.py
# Simula un plan de ahorro con intereses compuestos mensualmente más depósito mensual fijo.

monto = float(input("Monto inicial de ahorro: "))
deposito = float(input("Depósito mensual: "))
tasa = float(input("Tasa de interés mensual (%): "))
meses = int(input("Número de meses a simular: "))

print("\nPlan de Ahorro Detallado")

# Iteramos mes a mes
for i in range(1, meses + 1):
    saldo_inicial = monto
    # El interés se calcula exclusivamente sobre el saldo inicial
    interes = saldo_inicial * (tasa / 100)
    # El saldo final de este mes acumula el depósito también
    saldo_final = saldo_inicial + interes + deposito

    print(f"Mes {i}: Saldo Inicial: ${saldo_inicial:.2f} | Interés: ${interes:.2f} | Saldo Final: ${saldo_final:.2f}")

    # Actualizamos el monto base para que el próximo mes arranque desde este saldo
    monto = saldo_final

print(f"\nAl final de {meses} meses, tendrás ${monto:.2f}")