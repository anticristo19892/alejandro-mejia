"""#2"""

# Leer tres valores distintos desde el teclado
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Verificar que los tres valores son distintos
if num1 != num2 and num2 != num3 and num1 != num3:
    # Encontrar el mayor de los tres números
    if num1 > num2 and num1 > num3:
        print(f"{num1} es el mayor.")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} es el mayor.")
    else:
        print(f"{num3} es el mayor.")
else:
    print("Por favor, asegúrate de introducir tres valores distintos.")


    """#3"""

    # Leer tres números enteros desde el teclado
    num2 = int(input("Introduce el segundo número entero: "))
    num3 = int(input("Introduce el tercer número entero: "))

    # Encontrar el menor de los tres números
    menor_numero = min(num1, num2, num3)

    # Calcular la suma de los tres números
    suma_numeros = num1 + num2 + num3

    # Mostrar el resultado
    print(f"El menor de los tres números es: {menor_numero}")
    print(f"La suma de los tres números es: {suma_numeros}")


    """4"""

    # Leer las horas trabajadas y la tarifa por hora desde el teclado
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))

    # Verificar si hay horas extras (más de 40 horas)
    if horas_trabajadas > 40:
        horas_extra = horas_trabajadas - 40
        salario = (40 * tarifa_por_hora) + (horas_extra * 1.5 * tarifa_por_hora)
    else:
        salario = horas_trabajadas * tarifa_por_hora

    # Mostrar el salario total
    print(f"El salario total del trabajador es: {salario}")


    """#5"""

    # Leer la cantidad de camisas compradas y el precio por camisa desde el teclado
    cantidad_camisas = int(input("Ingrese la cantidad de camisas compradas: "))
    precio_por_camisa = float(input("Ingrese el precio por camisa: "))

    # Calcular el total sin descuento
    total_sin_descuento = cantidad_camisas * precio_por_camisa

    # Aplicar descuento según la cantidad de camisas compradas
    if cantidad_camisas >= 3:
        descuento = 0.2  # Descuento del 20% si se compran tres camisas o más
    else:
        descuento = 0.1  # Descuento del 10% si se compran menos de tres camisas

    # Calcular el total a pagar con descuento
    total_con_descuento = total_sin_descuento - (total_sin_descuento * descuento)

    # Mostrar el total a pagar
    print(f"El total a pagar por la compra de camisas es: {total_con_descuento}")


    """6"""

    # Leer el sueldo del trabajador desde el teclado
    sueldo = float(input("Ingrese el sueldo del trabajador: "))

    # Calcular el descuento según las condiciones dadas
    if sueldo <= 1000:
        descuento = sueldo * 0.1  # Descuento del 10% si el sueldo es menor o igual a 1000
    elif sueldo <= 2000:
        descuento = sueldo * 0.05  # Descuento del 5% del adicional si el sueldo está entre 1000 y 2000
    else:
        descuento = sueldo * 0.03  # Descuento del 3% del adicional si el sueldo es mayor a 2000

    # Calcular el sueldo neto después del descuento
    sueldo_neto = sueldo - descuento

    # Mostrar el descuento y el sueldo neto
    print(f"El descuento aplicado es: {descuento}")
    print(f"El sueldo neto que recibe el trabajador es: {sueldo_neto}")

    """#7"""

    # Leer las cinco calificaciones del alumno desde el teclado
    calificacion1 = float(input("Ingrese la calificación 1: "))
    calificacion2 = float(input("Ingrese la calificación 2: "))
    calificacion3 = float(input("Ingrese la calificación 3: "))
    calificacion4 = float(input("Ingrese la calificación 4: "))
    calificacion5 = float(input("Ingrese la calificación 5: "))

    # Calcular el promedio de las calificaciones
    promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

    # Determinar si el alumno aprueba o reprueba
    if promedio >= 5:
        resultado = "Aprobado"
    else:
        resultado = "Reprobado"

    # Mostrar el resultado
    print(f"El alumno está {resultado} con un promedio de {promedio}")

    """#8"""

    # Leer la marca y el precio de la motocicleta desde el teclado
    marca = input("Ingrese la marca de la motocicleta (Honda, Yamaha, Suzuki u otra): ")
    precio = float(input("Ingrese el precio de la motocicleta: "))

    # Determinar el descuento según la marca
    if marca.lower() == "honda":
        descuento = 0.05  # Descuento del 5% para motos Honda
    elif marca.lower() == "yamaha":
        descuento = 0.08  # Descuento del 8% para motos Yamaha
    elif marca.lower() == "suzuki":
        descuento = 0.1  # Descuento del 10% para motos Suzuki
    else:
        descuento = 0.02  # Descuento del 2% para otras marcas

    # Calcular el precio con descuento
    precio_con_descuento = precio - (precio * descuento)

    # Mostrar el precio de la moto, el descuento y el precio a pagar
    print(f"Precio de la motocicleta: {precio}")
    print(f"Descuento aplicado ({marca}): {descuento * 100}%")
    print(f"Precio a pagar: {precio_con_descuento}")


    """9#"""

    # Leer un valor numérico desde el teclado
    numero = int(input("Ingrese un valor numérico: "))

    # Determinar si el número es par o no
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"

    # Mostrar el resultado
    print(f"El número {numero} es {resultado}.")


    """#10"""

    # Importar la biblioteca datetime para trabajar con fechas
    import datetime

    # Obtener el día de la semana actual
    dia_actual = datetime.datetime.now().strftime("%A").lower()

    # Leer el precio de la moto desde el teclado
    precio_moto = float(input("Ingrese el precio de la moto: "))

    # Inicializar variables de descuento
    descuento_martes = 0.12
    descuento_sabado = 0.18
    descuento_feriado = 0.25

    # Inicializar el descuento según el día de la semana
    if dia_actual == "tuesday":  # Martes
        descuento = descuento_martes
    elif dia_actual == "saturday":  # Sábado
        descuento = descuento_sabado
    else:
        # Verificar si es feriado (puedes ajustar las fechas de acuerdo a los feriados de tu país)
        es_feriado = input("¿Es feriado? (Sí/No): ").lower()
        descuento = descuento_feriado if es_feriado == "sí" or es_feriado == "si" else 0

    # Calcular el precio con descuento
    precio_con_descuento = precio_moto - (precio_moto * descuento)

    # Mostrar el resultado
    print(f"El precio original de la moto es: {precio_moto}")
    print(f"Descuento aplicado el {dia_actual.capitalize()}: {descuento * 100}%")
    print(f"Precio a pagar: {precio_con_descuento}")





