num_empleados = 20
incremento_porcentual = 2.5 / 100  # Convertir el incremento del 2.5% a decimal
salarios = []
for i in range(num_empleados):
    salario = float(input(f"Ingrese el salario del empleado {i+1} en pesos: "))
    salarios.append(salario)
promedio_salarios = sum(salarios) / num_empleados
salarios_incrementados = [salario * (1 + incremento_porcentual) for salario in salarios]
print(f"El promedio de salarios es: {promedio_salarios:.2f} pesos")

print("\nSalario de cada empleado después del incremento del 2.5%:")
for i in range(num_empleados):
    print(f"Empleado {i+1}: {salarios_incrementados[i]:.2f} pesos")