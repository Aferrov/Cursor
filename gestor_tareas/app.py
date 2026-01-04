import json
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Lista global en memoria para almacenar las tareas
tareas = []
siguiente_id = 1


def cargar_datos():
    """Carga las tareas desde el archivo JSON."""
    global siguiente_id, tareas
    
    try:
        with open('tareas.json', 'r') as f:
            data = json.load(f)
            tareas = data['tareas']
            siguiente_id = data['siguiente_id']
    except FileNotFoundError:
        pass


def guardar_datos():
    """Guarda las tareas en el archivo JSON."""
    with open('tareas.json', 'w') as f:
        json.dump({'siguiente_id': siguiente_id, 'tareas': tareas}, f)


# Cargar datos al iniciar la aplicación
cargar_datos()


def agregar_tarea(texto):
    """Agrega una nueva tarea a la lista global.
    
    Args:
        texto (str): Texto de la tarea a agregar
        
    Returns:
        dict: La tarea creada, o None si el texto está vacío
    """
    global siguiente_id
    
    texto = texto.strip()
    if not texto:
        return None
    
    nueva_tarea = {
        'id': siguiente_id,
        'texto': texto,
        'hecho': False
    }
    tareas.append(nueva_tarea)
    siguiente_id += 1
    guardar_datos()
    
    return nueva_tarea


def completar_tarea(id):
    """Marca una tarea como completada.
    
    Args:
        id (int): ID de la tarea a completar
        
    Returns:
        bool: True si la tarea fue encontrada y completada, False en caso contrario
    """
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = True
            guardar_datos()
            return True
    return False


@app.route('/')
def index():
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)


@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')


@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
