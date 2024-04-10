def calcular_pago_anual(costo_total_servicios):
    return costo_total_servicios * 12  # Multiplicar por 12 para obtener el pago anual
def calcular_pago_mensual(costo_total_servicios):
    return costo_total_servicios  # El pago mensual es igual al costo total de servicios
costo_total_servicios = float(input("Ingrese el costo total de los servicios consumidos: "))
pago_anual = calcular_pago_anual(costo_total_servicios)
pago_mensual = calcular_pago_mensual(costo_total_servicios)
print(f"El monto pagado al año por servicios públicos es: {pago_anual} pesos.")
print(f"El monto pagado por mes por servicios públicos es: {pago_mensual} pesos.")