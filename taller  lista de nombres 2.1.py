def ordenar_nombres(lista_nombres):
    lista_nombres.sort()  # Ordenar la lista alfabéticamente
    return lista_nombres

# Pedir al usuario ingresar una lista de nombres separados por comas
entrada = input("carlos, mateo, andres, michell, alehjandro : ")

# Separar la entrada en una lista de nombres
nombres = entrada.split(',')
nombres = [nombre.strip() for nombre in nombres]
nombres_ordenados = ordenar_nombres(nombres)
print("Lista de nombres en orden alfabético:")
for nombre in nombres_ordenados:
    print(nombre)