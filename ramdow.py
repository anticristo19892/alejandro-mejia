import random
numero1 = random.randint(0, 100)
numero2 = random.randint(0, 100)
suma_correcta = numero1 + numero2
while True:
    respuesta = int(input(f"¿Cuánto es {numero1} + {numero2}? "))
    if respuesta == suma_correcta:
        print("¡Respuesta correcta!")
        break  # Salir del bucle si la respuesta es correcta
    else:
        print("Respuesta incorrecta. Inténtelo nuevamente.")

print(f"La suma de {numero1} + {numero2} es: {suma_correcta}")