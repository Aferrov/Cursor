def suma(a, b):
    """Realiza la suma de dos números."""
    return a + b


def resta(a, b):
    """Realiza la resta de dos números."""
    return a - b


def multiplicacion(a, b):
    """Realiza la multiplicación de dos números."""
    return a * b


def division(a, b):
    """Realiza la división de dos números. Maneja división por cero."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b


# Diccionario de operaciones
operaciones = {
    "suma": suma,
    "resta": resta,
    "multiplicación": multiplicacion,
    "multiplicacion": multiplicacion,  # Alternativa sin tilde
    "división": division,
    "division": division,  # Alternativa sin tilde
}


def obtener_numero(mensaje):
    """Obtiene un número válido del usuario."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número válido.")


def main():
    """Función principal del programa."""
    print("=== Calculadora ===")
    print("Operaciones disponibles: suma, resta, multiplicación, división")
    print("Escribe 'salir' para terminar.\n")
    
    while True:
        # Solicitar operación
        operacion = input("Operación (suma/resta/multiplicación/división/salir): ").strip().lower()
        
        # Verificar si el usuario quiere salir
        if operacion == "salir":
            print("¡Adios!")
            break
        
        # Verificar que la operación sea válida
        if operacion not in operaciones:
            print(f"Operación '{operacion}' no válida. Por favor, elige una operación válida.\n")
            continue
        
        # Obtener los dos números
        num1 = obtener_numero("Primer número: ")
        num2 = obtener_numero("Segundo número: ")
        
        # Ejecutar la operación
        try:
            funcion_operacion = operaciones[operacion]
            resultado = funcion_operacion(num1, num2)
            print(f"Resultado: {resultado}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Error inesperado: {e}\n")


if __name__ == "__main__":
    main()

