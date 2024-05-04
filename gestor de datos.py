import typing
class GestionGastos:
    def __init__(self):
        self.gastos = []
    def agregar_gasto(self, descripcion, monto):
        self.gastos.append({"descripcion": descripcion, "monto": monto})
    def calcular_presupuesto(self, presupuesto_total):
        total_gastos = sum(gasto["monto"] for gasto in self.gastos)
        presupuesto_disponible: int | typing.Any = presupuesto_total - total_gastos
        return presupuesto_disponible
gestor = GestionGastos()
gestor.agregar_gasto("Compras supermercado", 150)
gestor.agregar_gasto("Gasolina", 50)
gestor.agregar_gasto("Salida al cine", 30)
presupuesto_total = 7000
presupuesto_disponible = gestor.calcular_presupuesto(presupuesto_total)

print(f"Presupuesto total: {presupuesto_total} pesos")
print(f"Gastos realizados: {sum(gasto['monto'] for gasto in gestor.gastos)} pesos")
print(f"Presupuesto disponible: {presupuesto_disponible} pesos")
