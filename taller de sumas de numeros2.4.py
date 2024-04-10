def suma_numeros_pares(lista_numeros):
    suma_pares = sum(num for num in lista_numeros if num % 2 == 0)
    return suma_pares
entrada = input("1,2,3,4,: ")
numeros = [int(num) for num in entrada.split(',')]
suma_pares = suma_numeros_pares(numeros)
print("Suma de los números pares:", suma_pares)