def contar_vocales(frase):
    # Inicializar contadores para cada vocal
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0

    # Convertir la frase a minúsculas para facilitar el conteo
    frase = frase.lower()

    # Contar cada vocal en la frase
    for letra in frase:
        if letra == 'a':
            contador_a += 1
        elif letra == 'e':
            contador_e += 1
        elif letra == 'i':
            contador_i += 1
        elif letra == 'o':
            contador_o += 1
        elif letra == 'u':
            contador_u += 1

    # Mostrar el conteo de cada vocal
    print("Conteo de vocales:")
    print("a:", contador_a)
    print("e:", contador_e)
    print("i:", contador_i)
    print("o:", contador_o)
    print("u:", contador_u)