contrasena_correcta = "p217"
while True:
    contrasena = input("Ingrese la contraseña: ")
    if contrasena == contrasena_correcta:
        print("Bienvenido")
        break  # Salir del bucle cuando se ingresa la contraseña correcta
    else:
        print("Contraseña incorrecta. Inténtelo nuevamente.")