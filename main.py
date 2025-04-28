# main.py

from gestor import GestorTareas
import persistencia

def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Crear tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Exportar tareas a archivo")
    print("6. Importar tareas desde archivo")
    print("7. Salir")

def main():
    gestor = GestorTareas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            gestor.agregar_tarea(nombre, descripcion)

        elif opcion == "2":
            gestor.mostrar_tareas()

        elif opcion == "3":
            gestor.mostrar_tareas()
            try:
                indice = int(input("Índice de la tarea a completar: "))
                gestor.marcar_completada(indice)
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "4":
            gestor.mostrar_tareas()
            try:
                indice = int(input("Índice de la tarea a eliminar: "))
                gestor.eliminar_tarea(indice)
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "5":
            persistencia.guardar_tareas(gestor.tareas)

        elif opcion == "6":
            gestor.tareas = persistencia.cargar_tareas()
            print("Tareas importadas correctamente.")

        elif opcion == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
