def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
numero = 5
factorial_numero = calcular_factorial(numero)
print(f"El factorial de {numero} es: {factorial_numero}")