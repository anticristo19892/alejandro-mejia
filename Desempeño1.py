"""# 1 A.  (5+5)*5 """

# Inicializar una variable con el valor 5
resultado = 5

# Sumar 5 a la variable existente
resultado = resultado + 5

# Multiplicar el resultado por 5
resultado = resultado * 5

# Imprimir el resultado
print(resultado)

""" B.5+(5*5) """

# Inicializar una variable con el valor 5

resultado = 5

# Multiplicar 5 por 5
resultado_multiplicacion = 5 * 5

# Sumar el resultado de la multiplicación a la variable existente
resultado = resultado + resultado_multiplicacion

# Imprimir el resultado
print(resultado)

"""C.5 Modulo 2 """

# Inicializar una variable con el valor 5
resultado = 5

# Inicializar una variable con el valor 2 (el divisor)
divisor = 2

# Calcular el módulo y almacenar el resultado en la variable resultado
resultado = resultado % divisor

# Imprimir el resultado
print(resultado)

"""D. (5-(6/3))*2"""

# Inicializar una variable con el valor 5
resultado = 5

# Dividir 6 por 3 y restar el resultado a la variable existente
resultado = resultado - (6 / 3)

# Multiplicar el resultado por 2
resultado = resultado * 2

# Imprimir el resultado
print(resultado)


""" #2 . Si a=7 y b=3, ¿Cuál es el resultado de cada una de las siguientes comparaciones?
A. a != b"""


# Definir las variables a y b con los valores dados
a = 7
b = 3

# Realizar la comparación a != b
if a != b:
    print("Verdadero")
else:
    print("Falso")

"""B. a = b"""


    # Definir las variables a y b con los valores dados
a = 7
b = 3

    # Realizar la comparación a = b
if a == b:
    print("Verdadero")
else:
    print("Falso")


        """C. . a > b"""

    # Definir las variables a y b con los valores dados
a = 7
b = 3

    # Realizar la comparación a > b
if a > b:
    print("Verdadero")
else:
    print("Falso")


    """D. (a+b) < 2"""

    
    # Definir las variables a y b con los valores dados
a = 7
b = 3

    # Calcular la suma de a y b
suma = a + b

    # Realizar la comparación (a + b) < 2
if suma < 2:
    print("Verdadero")
else:
    print("Falso")

    """E. (a>7) Y (b=3)"""


    # Definir las variables a y b con los valores dados
a = 7
b = 3

    # Realizar las comparaciones
condicion = (a > 7) and (b == 3)

    # Imprimir el resultado
if condicion:
    print("Verdadero")
else:
    print("Falso")

    """F.(a<7) O (b=3)"""

    # Definir las variables a y b con los valores dados
a = 7
b = 3

# Evaluar la expresión lógica
resultado = (a > 7) and (b == 3)

# Imprimir el resultado
if resultado:
    print("Verdadero")
else:
    print("Falso")

    """D. (a<7) O (b=3)"""


# Definir las variables a y b con los valores dados
a = 7
b = 3

# Evaluar la expresión lógica
resultado = (a < 7) or (b == 3)

# Imprimir el resultado
if resultado:
    print("Verdadero")
else:
    print("Falso")

    """G. (a<7) O (b!=3)"""

    # Definir las variables a y b con los valores dados
    a = 7
    b = 3

    # Evaluar la expresión lógica
    resultado = (a < 7) or (b != 3)

    # Imprimir el resultado
    if resultado:
        print("Verdadero")
    else:
        print("Falso")


        """4."""

        # Leer las notas de cada componente desde el teclado
        taller1 = float(input("Ingrese la nota del Taller 1 (entre 1 y 5): "))
        taller2 = float(input("Ingrese la nota del Taller 2 (entre 1 y 5): "))
        cuestionario1 = float(input("Ingrese la nota del Cuestionario 1 (entre 1 y 5): "))
        cuestionario2 = float(input("Ingrese la nota del Cuestionario 2 (entre 1 y 5): "))
        proyecto_final = float(input("Ingrese la nota del Proyecto Final (entre 1 y 5): "))

        # Verificar que todas las notas estén en el rango válido
        if 1 <= taller1 <= 5 and 1 <= taller2 <= 5 and 1 <= cuestionario1 <= 5 and 1 <= cuestionario2 <= 5 and 1 <= proyecto_final <= 5:
            # Calcular la nota final
            nota_final = (taller1 * 0.20) + (taller2 * 0.15) + (cuestionario1 * 0.22) + (cuestionario2 * 0.10) + (
                        proyecto_final * 0.33)

            # Mostrar la nota final
            print(f"La nota final del curso es: {nota_final}")
        else:
            print("Por favor, asegúrate de ingresar notas válidas (entre 1 y 5).")

