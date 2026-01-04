import os
import argparse
from pathlib import Path

# Categorías de archivos con sus extensiones
categorias = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
}

categoria_predeterminada = "Otros"  # donde irá lo que no encaje en las anteriores

# Crear diccionario inverso: extensión -> categoría para búsqueda rápida
extension_a_categoria = {}
for categoria, exts in categorias.items():
    for ext in exts:
        extension_a_categoria[ext.lower()] = categoria


def organizar_archivos(carpeta_objetivo, sobrescribir=False):
    """
    Organiza los archivos de una carpeta en subcarpetas según su extensión.
    
    Args:
        carpeta_objetivo (Path): Carpeta donde se encuentran los archivos a organizar
        sobrescribir (bool): Si True, sobrescribe archivos duplicados. Si False, los omite.
    """
    if not carpeta_objetivo.exists():
        print(f"Error: La carpeta {carpeta_objetivo} no existe.")
        return
    
    if not carpeta_objetivo.is_dir():
        print(f"Error: {carpeta_objetivo} no es una carpeta.")
        return
    
    # Obtener lista de archivos (no directorios) en la carpeta objetivo
    archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]
    
    if not archivos:
        print("No se encontraron archivos para organizar.")
        return
    
    # Recorrer y organizar archivos
    movidos = 0
    omitidos = 0
    
    for archivo in archivos:
        # Excluir el script mismo si está en la carpeta
        if archivo.name == "organizar.py":
            continue
        
        ext = archivo.suffix.lower()
        categoria = extension_a_categoria.get(ext, "Otros")
        
        destino_dir = carpeta_objetivo / categoria
        destino_dir.mkdir(exist_ok=True)
        
        archivo_destino = destino_dir / archivo.name
        
        # Manejar archivos duplicados
        if archivo_destino.exists() and not sobrescribir:
            print(f"Omitido {archivo.name} (ya existe en {categoria}/)")
            omitidos += 1
            continue
        
        try:
            archivo.rename(archivo_destino)
            print(f"Movido {archivo.name} a {categoria}/")
            movidos += 1
        except Exception as e:
            print(f"Error al mover {archivo.name}: {e}")
    
    print(f"\nResumen: {movidos} archivos movidos, {omitidos} omitidos.")


def deshacer_organizacion(carpeta_objetivo, sobrescribir=False, eliminar_carpetas=True):
    """
    Deshace la organización moviendo los archivos de las subcarpetas de vuelta a la carpeta raíz.
    
    Args:
        carpeta_objetivo (Path): Carpeta donde están las subcarpetas organizadas
        sobrescribir (bool): Si True, sobrescribe archivos duplicados. Si False, los omite.
        eliminar_carpetas (bool): Si True, elimina las carpetas vacías después de mover los archivos.
    """
    if not carpeta_objetivo.exists():
        print(f"Error: La carpeta {carpeta_objetivo} no existe.")
        return
    
    if not carpeta_objetivo.is_dir():
        print(f"Error: {carpeta_objetivo} no es una carpeta.")
        return
    
    # Obtener todas las carpetas de categorías (incluyendo "Otros")
    todas_las_categorias = list(categorias.keys()) + [categoria_predeterminada]
    
    movidos = 0
    omitidos = 0
    errores = 0
    
    # Recorrer cada carpeta de categoría
    for categoria in todas_las_categorias:
        carpeta_categoria = carpeta_objetivo / categoria
        
        if not carpeta_categoria.exists() or not carpeta_categoria.is_dir():
            continue
        
        # Obtener todos los archivos en la carpeta de categoría
        archivos = [f for f in carpeta_categoria.iterdir() if f.is_file()]
        
        for archivo in archivos:
            archivo_destino = carpeta_objetivo / archivo.name
            
            # Manejar archivos duplicados
            if archivo_destino.exists() and not sobrescribir:
                print(f"Omitido {archivo.name} (ya existe en la carpeta raíz)")
                omitidos += 1
                continue
            
            try:
                archivo.rename(archivo_destino)
                print(f"Movido {archivo.name} de {categoria}/ a la carpeta raíz")
                movidos += 1
            except Exception as e:
                print(f"Error al mover {archivo.name}: {e}")
                errores += 1
        
        # Eliminar la carpeta si está vacía y eliminar_carpetas es True
        if eliminar_carpetas:
            try:
                # Verificar que la carpeta esté vacía (solo puede contener .gitkeep u otros archivos ocultos)
                contenido = list(carpeta_categoria.iterdir())
                if not contenido or all(item.name.startswith('.') for item in contenido):
                    carpeta_categoria.rmdir()
                    print(f"Carpeta {categoria}/ eliminada (vacía)")
            except Exception as e:
                # Si no se puede eliminar, no es crítico
                pass
    
    print(f"\nResumen: {movidos} archivos movidos, {omitidos} omitidos, {errores} errores.")


def main():
    parser = argparse.ArgumentParser(
        description="Organiza archivos en una carpeta según su extensión."
    )
    parser.add_argument(
        '--carpeta',
        type=str,
        default=str(Path.home() / "D:\Prueba"),
        help='Carpeta a organizar (por defecto: Downloads del usuario)'
    )
    parser.add_argument(
        '--sobrescribir',
        action='store_true',
        help='Sobrescribir archivos duplicados si ya existen en la carpeta destino'
    )
    parser.add_argument(
        '--deshacer',
        action='store_true',
        help='Deshacer la organización moviendo archivos de las subcarpetas de vuelta a la raíz'
    )
    
    args = parser.parse_args()
    
    # Convertir la ruta a Path
    carpeta_objetivo = Path(args.carpeta).resolve()
    
    if args.deshacer:
        print(f"Deshaciendo organización en: {carpeta_objetivo}")
        if args.sobrescribir:
            print("Modo: Sobrescribir archivos duplicados")
        else:
            print("Modo: Omitir archivos duplicados")
        print()
        deshacer_organizacion(carpeta_objetivo, args.sobrescribir)
    else:
        print(f"Organizando archivos en: {carpeta_objetivo}")
        if args.sobrescribir:
            print("Modo: Sobrescribir archivos duplicados")
        else:
            print("Modo: Omitir archivos duplicados")
        print()
        organizar_archivos(carpeta_objetivo, args.sobrescribir)


if __name__ == "__main__":
    main()
