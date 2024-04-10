import random
from typing import List


def generar_carton_bingo():
    numeros_carton = random.sample(range(1, 91), 15)  # Seleccionar 15 números aleatorios del 1 al 90
    carton: list[list[int]] = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    for i in range(3):
    for j in range(5):
    carton[i][j] = numeros_carton.pop()
    return carton
def mostrar_carton(carton):
    print("Tu cartón de bingo:")
    for fila in carton:
    print(fila)

def marcar_numero_sorteado(carton, numero_sorteado):
    for i in range(3):
    for j in range(5):
    if carton[i][j] == numero_sorteado:
    carton[i][j] = 'X'

     def verificar_linea_completa(carton):
    # Verificar líneas horizontales
    for fila in carton:
    if fila.count('X') == 5:
    return True
for j in range(5):
    if carton[0][j] == carton[1][j] == carton[2][j] == 'X':
        return True
 if carton[0][0] == carton[1][1] == carton[2][2] == 'X' or carton[0][4] == carton[1][3] == carton[2][2] == 'X':
    return True
    return False
def jugar_bingo():
    carton_jugador = generar_carton_bingo()
    mostrar_carton(carton_jugador)
 numeros_sorteo = list(range(1, 91))
    random.shuffle(numeros_sorteo)
    for numero_sorteado in numeros_sorteo:
        input("Presiona Enter para sortear el siguiente número...")
        print(f"Número sorteado: {numero_sorteado}")
        marcar_numero_sorteado(carton_jugador, numero_sorteado)
        mostrar_carton(carton_jugador)
if verificar_linea_completa(carton_jugador):
            print("¡Felicidades! Completaste una línea en tu cartón.")
            break
print("¡Bienvenido al juego de Bingo Digital!")
jugar_bingo()