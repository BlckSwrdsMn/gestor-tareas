import json
from tarea import Tarea

def guardar_tareas(tareas, archivo="tareas.json"):
    datos = [
        {
            "nombre": tarea.nombre,
            "descripcion": tarea.descripcion,
            "completada": tarea.completada
        } for tarea in tareas
    ]
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)
    print("Tareas guardadas correctamente.")

def cargar_tareas(archivo="tareas.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return [Tarea(d["nombre"], d["descripcion"], d["completada"]) for d in datos]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error al cargar el archivo. Formato inválido.")
        return []
