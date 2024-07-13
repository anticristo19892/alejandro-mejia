import pymysql

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             database='estudiante')

with connection.cursor() as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            edad INT,
            grado VARCHAR(50)
        )
    """)


def agregar_estudiante(nombre, edad, grado):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO estudiantes (nombre, edad, grado) VALUES (%s, %s, %s)", (nombre, edad, grado))
    connection.commit()


def consultar_estudiantes():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM estudiantes")
        result = cursor.fetchall()
        for row in result:
            print(row)


def actualizar_estudiante(id_estudiante, nombre, edad, grado):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE estudiantes SET nombre = %s, edad = %s, grado = %s WHERE id = %s",
                       (nombre, edad, grado, id_estudiante))
    connection.commit()


def eliminar_estudiante(id_estudiante):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM estudiantes WHERE id = %s", (id_estudiante,))
    connection.commit()


while True:
    print("1. Agregar estudiante")
    print("2. Consultar todos los estudiantes")
    print("3. Actualizar información de un estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        nombre = input("Ingresa el nombre del estudiante: ")
        edad = int(input("Ingresa la edad del estudiante: "))
        grado = input("Ingresa el grado del estudiante: ")
        agregar_estudiante(nombre, edad, grado)

    elif opcion == '2':
        consultar_estudiantes()

    elif opcion == '3':
        id_estudiante = int(input("Ingresa el ID del estudiante a actualizar: "))
        nombre = input("Ingresa el nuevo nombre del estudiante: ")
        edad = int(input("Ingresa la nueva edad del estudiante: "))
        grado = input("Ingresa el nuevo grado del estudiante: ")
        actualizar_estudiante(id_estudiante, nombre, edad, grado)

    elif opcion == '4':
        id_estudiante = int(input("Ingresa el ID del estudiante a eliminar: "))
        eliminar_estudiante(id_estudiante)

    elif opcion == '5':
        break

connection.close()