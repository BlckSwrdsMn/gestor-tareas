
from tarea import Tarea  

class GestorTareas:
    def __init__(self):
        self.tareas = []  # Lista para guardar objetos Tarea

    def agregar_tarea(self, nombre, descripcion):
        nueva_tarea = Tarea(nombre, descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{nombre}' agregada correctamente.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada.nombre}' eliminada.")
        else:
            print("Índice inválido. No se pudo eliminar la tarea.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return

        for idx, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{idx}. {tarea.nombre} - {estado} - {tarea.descripcion}")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
            print(f"Tarea '{self.tareas[indice].nombre}' marcada como completada.")
        else:
            print("Índice inválido. No se pudo completar la tarea.")
