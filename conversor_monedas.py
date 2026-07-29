# Programa para convertir pesos mexicanos a otras monedas

pesos = float(input("Ingresa la cantidad en pesos mexicanos (MXN): "))
print("Monedas disponibles: USD, EUR, THB, JPY, KRW, AUD, PEN, CAD, VES, ARS")
destino = input("A qué moneda deseas convertir: ").strip().upper()

match destino:
    case "USD":
        print(f"Total: {pesos * 0.055:.2f} USD")
    case "EUR":
        print(f"Total: {pesos * 0.050:.2f} EUR")
    case "THB":
        print(f"Total: {pesos * 2.00:.2f} THB")
    case "JPY":
        print(f"Total: {pesos * 8.50:.2f} JPY")
    case "KRW":
        print(f"Total: {pesos * 75.00:.2f} KRW")
    case "AUD":
        print(f"Total: {pesos * 0.084:.2f} AUD")
    case "PEN":
        print(f"Total: {pesos * 0.20:.2f} PEN")
    case "CAD":
        print(f"Total: {pesos * 0.075:.2f} CAD")
    case "VES":
        print(f"Total: {pesos * 2.00:.2f} VES")
    case "ARS":
        print(f"Total: {pesos * 50.00:.2f} ARS")
    case _:
        print("Moneda no reconocida")
        