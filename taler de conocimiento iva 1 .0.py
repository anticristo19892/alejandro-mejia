def calcular_costo_total(productos):
    total_sin_iva = sum(productos)
    iva = total_sin_iva * 0.16  # Suponiendo un IVA del 16%
    total_con_iva = total_sin_iva + iva
    return total_sin_iva, total_con_iva