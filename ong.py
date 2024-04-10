vacunas_disponibles = 1000
para cada dia
cantidad_entregada = solicitar_cantidad_entregada()  # Supongamos que hay una función para esto
vacunas_disponibles = vacunas_disponibles - cantidad_entregada
si vacunas_disponibles < 200 entonces
mostrar "¡Alerta! El inventario de vacunas es menor a 200 unidades."