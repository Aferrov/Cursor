import re
from collections import Counter


class ContadorDePalabras:
    def __init__(self):
        self.texto = ""
    
    def leer_archivo(self, ruta_archivo):
        """
        Lee el contenido de un archivo de texto.
        
        Args:
            ruta_archivo (str): Ruta del archivo a leer
            
        Returns:
            bool: True si se leyó correctamente, False en caso contrario
        """
        ruta_archivo = ruta_archivo.strip().strip('"').strip("'")
        
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                self.texto = f.read()
            return True
        except FileNotFoundError:
            print("El archivo especificado no existe.")
            return False
        except OSError as e:
            print(f"Error al abrir el archivo: {e}")
            return False
    
    def contar_palabras(self, top_n=10):
        """
        Cuenta las palabras en el texto y muestra estadísticas.
        
        Args:
            top_n (int): Número de palabras más frecuentes a mostrar (default: 10)
        """
        if not self.texto:
            print("No hay texto para procesar. Lee un archivo primero.")
            return
        
        # Separar el contenido en palabras
        palabras = re.findall(r"\w+", self.texto.lower())
        
        total_palabras = len(palabras)
        
        print(f"Total palabras: {total_palabras}")
        
        contador = Counter(palabras)
        
        mas_comunes = contador.most_common(top_n)
        
        print("Palabras más frecuentes:")
        
        for palabra, freq in mas_comunes:
            print(f"{palabra}: {freq}")


if __name__ == "__main__":
    archivo = input("Introduce la ruta del archivo de texto: ")
    
    contador = ContadorDePalabras()
    
    if contador.leer_archivo(archivo):
        contador.contar_palabras()
