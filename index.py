from BaseDeDatos.conexion import DAO
import funciones_equipos
import funciones_responsables
import funciones_ubicaciones


# Se crea un ciclo para que el programa se esté ejecutando hasta que el usuario quiera salir
while True:
    # Se muestran las opciones que el usuario puede elegir
    print("Opciones:")
    print("1. CRUD Ubicaciones")
    print("2. CRUD Responsables")
    print("3. CRUD Equipos")
    print("4. Salir del programa")

    # Solicitar la opción al usuario
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        funciones_ubicaciones.mostrar_menu_ubicaciones()

    elif opcion == 2:
        funciones_responsables.mostrar_menu_responsables()

    elif opcion == 3:
        funciones_equipos.mostrar_menu_equipos()
    elif opcion == 4:
        # Salir del programa
        print("-------------------------------------------------------------------------------")
        print("Gracias por utilizar el sistema de inventarios de Bioingeniería")
        print("-------------------------------------------------------------------------------")
        break

    else:
      print("-------------------------------------------------------------------------------")
      print("Has ingresado una opción no válida")
      print("-------------------------------------------------------------------------------")
