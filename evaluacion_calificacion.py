#programa para evaluar calificaciones por letras
nota = float(input("Ingresa tu calificación (0-100): "))

if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
elif nota >= 0:
    letra = "F"
else:
    letra = "Calificación inválida"

print(f"Tu calificación en letra es: {letra}")
