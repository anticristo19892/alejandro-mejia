def generar_tablas_de_multiplicar(numero):
    for i in range(1, 101):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")