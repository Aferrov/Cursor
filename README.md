# Cursor - Proyectos de Python

Este repositorio contiene una colección de proyectos y ejercicios de Python desarrollados con Cursor. Incluye ejercicios clásicos de programación, utilidades prácticas y proyectos de análisis de datos.

## 📋 Proyectos Incluidos

### 🧮 Calculadora (`calculadora.py`)
Calculadora interactiva que permite realizar operaciones básicas (suma, resta, multiplicación, división) entre dos números. El programa se ejecuta en un bucle hasta que el usuario escribe "salir".

**Características:**
- Operaciones: suma, resta, multiplicación, división
- Manejo de división por cero
- Validación de entrada
- Interfaz amigable

**Uso:**
```bash
python calculadora.py
```

### 📊 Contador de Palabras (`contador.py`)
Utilidad para analizar archivos de texto. Cuenta el total de palabras y muestra las palabras más frecuentes.

**Características:**
- Lectura de archivos de texto
- Contador de palabras totales
- Top 10 palabras más frecuentes
- Programación orientada a objetos (clase `ContadorDePalabras`)

**Uso:**
```bash
python contador.py
```

### 🔢 FizzBuzz (`fizzbuzz.py`)
Implementación del clásico problema FizzBuzz: recorre números del 1 al 50 e imprime "Fizz" para múltiplos de 3, "Buzz" para múltiplos de 5, y "FizzBuzz" para múltiplos de ambos.

**Uso:**
```bash
python fizzbuzz.py
```

### 📈 Análisis de Datos (`analisis.py`)
Script de análisis de datos que lee un archivo CSV y genera estadísticas descriptivas y visualizaciones.

**Características:**
- Lectura de archivos CSV con pandas
- Cálculo de estadísticas: media, mediana, desviación estándar
- Gráfica de dispersión con matplotlib

**Uso:**
```bash
python analisis.py
```

**Requisitos:**
- pandas
- matplotlib

### 📄 Procesamiento de PDFs (`main.py`)
Proyecto base para procesamiento de archivos PDF usando PyPDF2.

**Requisitos:**
- PyPDF2

### 📝 Ejercicios Adicionales
- `example.py`: Ejemplo básico de Python
- `ejercicio_autocompletar.py`: Función para generar cuadrados de números naturales
- `datos.csv`: Dataset de ejemplo para análisis

## 🚀 Requisitos

### Dependencias Básicas
- Python 3.x

### Dependencias Opcionales
Para ejecutar todos los proyectos, instala las siguientes librerías:

```bash
pip install pandas matplotlib PyPDF2
```

O instala todas a la vez:

```bash
pip install -r requirements.txt
```

## 📦 Estructura del Repositorio

```
Cursor/
├── README.md
├── analisis.py          # Análisis de datos con pandas y matplotlib
├── calculadora.py       # Calculadora interactiva
├── contador.py          # Contador de palabras en archivos
├── datos.csv            # Dataset de ejemplo
├── ejercicio_autocompletar.py  # Ejercicio de listas por comprensión
├── example.py           # Ejemplos básicos
├── fizzbuzz.py          # Problema clásico FizzBuzz
└── main.py              # Procesamiento de PDFs
```

## 🛠️ Instalación y Configuración

1. Clona el repositorio:
```bash
git clone https://github.com/Aferrov/Cursor.git
cd Cursor
```

2. (Opcional) Crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install pandas matplotlib PyPDF2
```

## 💡 Notas

- Los scripts están diseñados para ser ejecutados de forma independiente
- Algunos proyectos requieren archivos de entrada (como `contador.py` que necesita un archivo de texto)
- El archivo `datos.csv` es necesario para ejecutar `analisis.py`

## 📚 Recursos

- [Documentación de Python](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)


