def calcular_promedio_sueldos(lista_sueldos):
    if not lista_sueldos:
        return 0  # Retornar 0 si la lista de sueldos está vacía
    else:
        total_sueldos = sum(lista_sueldos)
        promedio = total_sueldos / len(lista_sueldos)
        return promedio
    sueldos = []
    while True:
        sueldo = input("Ingrese el sueldo del empleado (escriba 'fin' para terminar): ")
        if sueldo.lower() == 'fin':
        sueldos.append(float(sueldo))
sueldo_promedio = calcular_promedio_sueldos(sueldos)
print("El sueldo promedio del grupo de empleados es:", sueldo_promedio)
