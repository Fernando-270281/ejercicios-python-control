# Programa para brindar informacion sobre artistas, peliculas y series
print("Opciones disponibles: 1. Taylor Swift | 2. Inception | 3. Breaking Bad | 4. Batman | 5. Arcane")
busqueda = input("Ingresa una opción (1 al 5): ").strip()

match busqueda:
    case "1":
        print("Taylor Swift: Cantautora estadounidense récord en ventas y tours.")
    case "2":
        print("Inception: Película de ciencia ficción dirigida por Christopher Nolan sobre el mundo de los sueños.")
    case "3":
        print("Breaking Bad: Serie sobre un profesor de química que ingresa al mundo del narcotráfico.")
    case "4":
        print("Batman: El superhéroe vigilante de Gotham de DC Comics.")
    case "5":
        print("Arcane: Aclamada serie animada ambientada en el universo de League of Legends.")
    case _:
        print("Opción no encontrada.")
        
