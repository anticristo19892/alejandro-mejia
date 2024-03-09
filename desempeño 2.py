

"""Desmpeño 2 """


def calificar_ejercicio(numero_ejercicio):
    """
    Función para calificar cada ejercicio según el número proporcionado.
    """
    nota = 0  # Inicializar la nota en 0 por defecto

    # Utilizar match case para calificar cada ejercicio
    match numero_ejercicio:
        case 1:
            print("Calificar ejercicio: Hola mundo")
            # Aquí se podrían agregar instrucciones específicas para calificar este ejercicio
            nota = float(input("Ingrese la nota para el ejercicio 'Hola mundo': "))
        case 2:
            print("Calificar ejercicio: Suma de números")
            nota = float(input("Ingrese la nota para el ejercicio 'Suma de números': "))
        case 3:
            print("Calificar ejercicio: Calcular la edad")
            nota = float(input("Ingrese la nota para el ejercicio 'Calcular la edad': "))
        case 4:
            print("Calificar ejercicio: IMC")
            nota = float(input("Ingrese la nota para el ejercicio 'IMC': "))
        case 5:
            print("Calificar ejercicio: Hallar el número para he impar de un número.")
            nota = float(input("Ingrese la nota para el ejercicio 'Hallar el número para he impar de un número.': "))
        case 6:
            print("Calificar ejercicio: Hallar el área de un cuadrado")
            nota = float(input("Ingrese la nota para el ejercicio 'Hallar el área de un cuadrado': "))
        case 7:
            print("Calificar ejercicio: Hallar el área de un triángulo")
            nota = float(input("Ingrese la nota para el ejercicio 'Hallar el área de un triángulo': "))
        case _:
            print("Ejercicio no válido. Por favor, ingrese un número de ejercicio válido.")

    return nota


def main():
    """
    Función principal que muestra el menú y permite calificar los ejercicios.
    """
    while True:
        # Mostrar menú
        print("\nCalificador de programas - Menú:")
        print("1. Hola mundo")
        print("2. Suma de números")
        print("3. Calcular la edad")
        print("4. IMC")
        print("5. Hallar el número para he impar de un número.")
        print("6. Hallar el área de un cuadrado")
        print("7. Hallar el área de un triángulo")
        print("0. Salir")

        # Solicitar la elección del usuario
        opcion = int(input("Ingrese el número del ejercicio que desea calificar (o 0 para salir): "))

        # Salir del programa si se ingresa 0
        if opcion == 0:
            break

        # Calificar el ejercicio según la opción proporcionada
        nota = calificar_ejercicio(opcion)
        print(f"Nota para el ejercicio {opcion}: {nota}")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()