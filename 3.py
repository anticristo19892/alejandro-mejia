def costo_de_llamada(destino , duracion):

   costos_por_minuto= {
    "estaos unidos": 900,
    "canada": 800,
    "europa": 950,
    "resto del mundo": 1250,
   }

   # Descuento por Duracion
   descuento = 0.2 if duracion > 1 else 0

   # calcular el costo total
   costo_total = duracion * costos_por_minuto[destinio] * (1 - descuento)

   return costo_total

# ejemplo
destino = "europa"
duracion = int(input("ingrese la duracion e la llamada:"))

costo_total = costo_llamada(destino, duracion)

print(f"el costo total de la llamada es: {costo_total:.2f}pesos")






