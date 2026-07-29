# Programa para convertir grados a celsius a farenheit o kelvin
celsius = float(input("Ingresa la temperatura en Celsius: "))
print("Opciones a convertir: 1. Fahrenheit | 2. Kelvin")
opcion = input("Elige una opción (1 o 2): ").strip()

match opcion:
    case "1":
        f = (celsius * 9/5) + 32
        print(f"{celsius}°C equivalen a {f:.2f}°F")
    case "2":
        k = celsius + 273.15
        print(f"{celsius}°C equivalen a {k:.2f} K")
    case _:
        print("Opción no válida")
        