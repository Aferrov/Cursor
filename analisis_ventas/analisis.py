import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 1. Cargar datos del CSV
df = pd.read_csv('ventas.csv')
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.to_period('M')

# 2. Calcular ventas totales por mes
ventas_por_mes = df.groupby('mes').apply(lambda d: (d['cantidad'] * d['precio']).sum())
ventas_por_mes = ventas_por_mes.sort_index()

print("Ventas por mes:")
print(ventas_por_mes)
print()

# 3. Determinar producto más vendido y con mayor ingresos
df['ingreso'] = df['cantidad'] * df['precio']

ventas_prod = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingreso': 'sum'
})

mas_vendido = ventas_prod['cantidad'].idxmax()
mayor_ingreso = ventas_prod['ingreso'].idxmax()

print(f"Producto más vendido en unidades: {mas_vendido} (total {ventas_prod.loc[mas_vendido, 'cantidad']})")
print(f"Producto con mayores ingresos: {mayor_ingreso} (total  S/.{ventas_prod.loc[mayor_ingreso, 'ingreso']:.2f})")
print()

# 4. Graficar ventas por mes
# Si ventas_por_mes es index Period, convertir a str para mejor manejo
ventas_por_mes.index = ventas_por_mes.index.astype(str)

plt.figure(figsize=(6, 4))
ventas_por_mes.plot(kind='bar')
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas (S/.)")
plt.tight_layout()
plt.savefig("ventas_por_mes.png")
plt.show()

# 5. Graficar top 5 productos por ingresos
top5 = ventas_prod.nlargest(5, 'ingreso')

plt.figure(figsize=(6, 4))
plt.bar(top5.index, top5['ingreso'])
plt.title("Top 5 Productos por Ingresos")
plt.ylabel("Ingresos (S/.)")
plt.xlabel("Producto")
plt.tight_layout()
plt.savefig("top5_productos.png")
plt.show()
