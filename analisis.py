import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('datos.csv')

# Calcular estadísticas para cada columna
print("=== Estadísticas de las columnas ===\n")

for columna in df.columns:
    media = df[columna].mean()
    mediana = df[columna].median()
    desviacion = df[columna].std()
    
    print(f"Columna '{columna}':")
    print(f"  Media: {media:.2f}")
    print(f"  Mediana: {mediana:.2f}")
    print(f"  Desviación estándar: {desviacion:.2f}\n")

# Trazar un scatter plot de col1 vs col2
col1 = df.columns[0]
col2 = df.columns[1]

plt.figure(figsize=(8, 6))
plt.scatter(df[col1], df[col2], alpha=0.6, s=50)
plt.xlabel(col1)
plt.ylabel(col2)
plt.title(f'Gráfica de dispersión: {col1} vs {col2}')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

