
#4.
def calcular_pago_matricula(notas):
  n1, n2, n3, n4 = notas
  #Calcular el promedio
  promedio = (n1 + n2 + n3 + n4) / 4
  #Determinar el rendimiento
  rendimiento = "Deficiente"
  if promedio >= 4:
    rendimiento = "Excelente"
  elif promedio >= 3:
    rendimiento = "Bien"
  #Calcular el descuento
  descuento = 0
  if rendimiento == "Excelente":
    descuento = 0.2
  #Calcular el pago de la matrícula
  costo_total = 100000  # Ingresar el valor real del costo total de la matrícula
  pago = (1 - descuento) * costo_total
  #Mostrar resultados
  return promedio, rendimiento, descuento, pago

#Ejemplo de uso
notas = [4.5, 4.0, 3.5, 4.0]
promedio, rendimiento, descuento, pago = calcular_pago_matricula(notas)

print(f"Promedio: {promedio}")
print(f"Rendimiento: {rendimiento}")
print(f"Descuento: {descuento:.2%}")
print(f"Pago de la matrícula: {pago}")
