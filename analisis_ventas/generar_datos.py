import pandas as pd
from datetime import datetime, timedelta
import random

# Productos disponibles
productos = ['A', 'B', 'C', 'D', 'E']

# Fechas: últimos 6 meses aproximadamente
fecha_inicio = datetime(2024, 7, 1)
fecha_fin = datetime(2025, 1, 31)

# Generar datos sintéticos
datos = []

# Precios base por producto
precios_base = {'A': 10.0, 'B': 20.0, 'C': 15.0, 'D': 25.0, 'E': 30.0}

# Generar aproximadamente 150 registros de ventas
for _ in range(150):
    # Fecha aleatoria en el rango
    dias_aleatorios = random.randint(0, (fecha_fin - fecha_inicio).days)
    fecha = fecha_inicio + timedelta(days=dias_aleatorios)
    
    # Producto aleatorio
    producto = random.choice(productos)
    
    # Cantidad (entre 1 y 10)
    cantidad = random.randint(1, 10)
    
    # Precio con pequeña variación (±10%)
    precio_base = precios_base[producto]
    variacion = precio_base * random.uniform(-0.1, 0.1)
    precio = round(precio_base + variacion, 2)
    
    datos.append({
        'fecha': fecha.strftime('%Y-%m-%d'),
        'producto': producto,
        'cantidad': cantidad,
        'precio': precio
    })

# Crear DataFrame
df = pd.DataFrame(datos)

# Ordenar por fecha
df = df.sort_values('fecha').reset_index(drop=True)

# Guardar a CSV
df.to_csv('ventas.csv', index=False)

print(f"Archivo ventas.csv generado con {len(df)} registros de ventas")
print(f"Rango de fechas: {df['fecha'].min()} a {df['fecha'].max()}")
print(f"\nPrimeras 10 filas:")
print(df.head(10))
print(f"\nResumen:")
print(df.describe())

