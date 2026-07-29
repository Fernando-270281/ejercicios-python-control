# Parciales 40%, proyecto 30%, examen 30%
parciales = float(input("Calificación de parciales (0-100): "))
proyecto = float(input("Calificación del proyecto (0-100): "))
examen = float(input("Calificación del examen (0-100): "))

calificacion_final = (parciales * 0.40) + (proyecto * 0.30) + (examen * 0.30)
print(f"La calificación final es: {calificacion_final:.2f}")
