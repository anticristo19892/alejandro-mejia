def palabras_comienzan_con_letra(lista_palabras, letra):
    palabras_filtradas = [palabra for palabra in lista_palabras if palabra.lower().startswith(letra.lower())]
    return palabras_filtradas