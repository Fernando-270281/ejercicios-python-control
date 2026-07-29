# Programa para calcular el precio final de un producto despues del descuento
precio = float(input("Ingresa el precio del producto: "))

if precio <= 100:
    descuento = 0.05  # 5%
elif precio <= 200:
    descuento = 0.10  # 10%
elif precio <= 500:
    descuento = 0.15  # 15%
else:
    descuento = 0.20  # 20%

total = precio * (1 - descuento)
print(f"Descuento aplicado: {int(descuento * 100)}%")
print(f"Total a pagar: ${total:.2f}")
