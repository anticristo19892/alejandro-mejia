def calcular_promedio_edad(datos_estudiantes):
    # Inicializar contadores y sumas para hombres y mujeres
    num_hombres = 0
    sum_edad_hombres = 0
    num_mujeres = 0
    sum_edad_mujeres = 0
    for estudiante in datos_estudiantes:
        edad = estudiante['edad']
        if estudiante['genero'] == 'hombre':
            num_hombres += 1
            sum_edad_hombres += edad
        elif estudiante['genero'] == 'mujer':
            num_mujeres += 1
            sum_edad_mujeres += edad
            f
            num_hombres > 0:
            promedio_edad_hombres = sum_edad_hombres / num_hombres
        else:
            promedio_edad_hombres = 0

        if num_mujeres > 0:
            promedio_edad_mujeres = sum_edad_mujeres / num_mujeres
        else:
            promedio_edad_mujeres = 0
            return promedio_edad_hombres, promedio_edad_mujeres
        datos_estudiantes = [
            {'nombre': 'Juan', 'edad': 25, 'genero': 'hombre'},
            {'nombre': 'María', 'edad': 30, 'genero': 'mujer'},
            {'nombre': 'Pedro', 'edad': 22, 'genero': 'hombre'},
            {'nombre': 'Ana', 'edad': 28, 'genero': 'mujer'},
            {'nombre': 'Luis', 'edad': 35, 'genero': 'hombre'}
            promedio_edad_hombres, promedio_edad_mujeres = calcular_promedio_edad(datos_estudiantes)
        print(f"Promedio de edad de hombres: {promedio_edad_hombres:.2f} años")
        print(f"Promedio de edad de mujeres: {promedio_edad_mujeres:.2f} años")
