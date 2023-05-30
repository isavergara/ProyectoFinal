from BaseDeDatos.conexion import DAO

# Función para agregar ubicacion
def agregar_ubicacion():
      dao = DAO()
      # Ciclo para pedir el código de la ubicación
      while True:
        try:
          codigo_ubicacion = int(input("Ingresa el código de la ubicación: "))
          print("- - - - - - - - - - - - - - - - -")
          break
        except ValueError:
          print("Error: Por favor, ingrese un número válido.")
          print("- - - - - - - - - - - - - - - - -")

      # Ciclo para pedir el nombre de la ubicación
      while True:
        nombre = input("Ingrese el nombre de la ubicacion: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(nombre) != 0:
          break
        print("Ingresa un nombre (no has ingresado nada)")

      # Ciclo para pedir el piso
      while True:
        try:
          piso = int(input("Ingresa el piso: "))
          print("- - - - - - - - - - - - - - - - -")
          break
        except ValueError:
          print("Error: Por favor, ingrese un número válido.")
          print("- - - - - - - - - - - - - - - - -")
      
      data_del_ubicacion = [codigo_ubicacion, nombre, piso]
      dao.registrarUbicacion(data_del_ubicacion)

# Función para modificar ubicacion
def modificar_ubicacion():
      dao = DAO()
      # Ciclo para pedir el código del ubicacion
      while True:
        try:
          codigo_ubicacion = int(input("Ingresa el código del ubicacion: "))
          print("- - - - - - - - - - - - - - - - -")
          ubicacion_encontrada = dao.encontrarUbicacionConCodigo(codigo_ubicacion)
          if(len(ubicacion_encontrada) == 0):
            print("No se ha encontrado ningún ubicacion con esa identificación")
            print("- - - - - - - - - - - - - - - - -")
          else:
            break
        except ValueError:
          print("Error: Por favor, ingrese un código válido.")
          print("- - - - - - - - - - - - - - - - -")

      # Ciclo para pedir el nombre de la ubicación
      while True:
        nombre = input("Ingrese el nombre de la ubicacion: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(nombre) != 0:
          break
        print("Ingresa un nombre (no has ingresado nada)")

      # Ciclo para pedir el piso
      while True:
        try:
          piso = int(input("Ingresa el piso: "))
          print("- - - - - - - - - - - - - - - - -")
          break
        except ValueError:
          print("Error: Por favor, ingrese un número válido.")
          print("- - - - - - - - - - - - - - - - -")
      
      data_de_la_ubicacion = [codigo_ubicacion, nombre, piso]
      dao.actualizarUbicacion(data_de_la_ubicacion)

#Función para eliminar ubicacions
def eliminar_ubicacion():
  dao = DAO()
  # Ciclo para pedir el código del ubicacion
  while True:
    try:
      codigo_ubicacion = int(input("Ingresa el código del ubicacion: "))
      print("- - - - - - - - - - - - - - - - -")
      ubicacion_encontrado = dao.encontrarUbicacionConCodigo(codigo_ubicacion)
      if(len(ubicacion_encontrado) == 0):
        print("No se ha encontrado ningún ubicacion con esa identificación")
        print("- - - - - - - - - - - - - - - - -")
      else:
        break
    except ValueError:
      print("Error: Por favor, ingrese un código válido.")
      print("- - - - - - - - - - - - - - - - -")
  
  dao.eliminarUbicacion(codigo_ubicacion)

# Función para buscar ubicacions
def buscar_ubicacion():
  dao = DAO()
  # Ciclo para pedir el código del ubicacion
  while True:
    try:
      codigo_ubicacion = int(input("Ingresa el código del ubicacion: "))
      print("- - - - - - - - - - - - - - - - -")
      ubicacion_encontrada = dao.encontrarUbicacionConCodigo(codigo_ubicacion)
      if(len(ubicacion_encontrada) == 0):
        print("No se ha encontrado ningún ubicacion con esa identificación")
        print("- - - - - - - - - - - - - - - - -")
        break
      else:
        datos = "Código: {0} | Nombre: '{1}' | Piso: {2}"
        print(datos.format(ubicacion_encontrada[0][0], ubicacion_encontrada[0][1], ubicacion_encontrada[0][2]))
        break
    except ValueError:
      print("Error: Por favor, ingrese un código válido.")
      print("- - - - - - - - - - - - - - - - -")

def mostrarUbicaciones():
    dao = DAO()
    print("\ Ubicaciones: \n")
    contador = 1
    ubicaciones = dao.listarUbicaciones()
    for ubicacion in ubicaciones:
        datos = "{0}. Código: {1} | Nombre: '{2}' | Piso: {3}"
        print(datos.format(contador, ubicacion[0], ubicacion[1], ubicacion[2]))
        contador = contador + 1
    print(" ")

# Función para mostrar menú de ubicacions
def mostrar_menu_ubicaciones():
  while True:
    # Se muestran las opciones que el usuario puede elegir
    print("Opciones (CRUD RESPONSABLES):")
    print("1. Ingresar Ubicación")
    print("2. Modificar Ubicación")
    print("3. Eliminar Ubicación")
    print("4. Buscar ubicación")
    print("5. Mostrar ubicaciones")
    print("6. Salir del Menú")

  # Solicitar la opción al usuario
    try:
      opcion = int(input("Seleccione una opción: "))
      print("-")
    except ValueError:
      print("Error: Por favor, ingrese un número entero válido.")
      print("- - - - - - - - - - - - - - - - -")
      continue
  
    if(opcion == 1):
      agregar_ubicacion()
      break
    elif(opcion == 2):
      modificar_ubicacion()
    elif(opcion == 3):
      eliminar_ubicacion()
    elif(opcion == 4):
      buscar_ubicacion()
    elif(opcion == 5):
      mostrarUbicaciones()
    elif(opcion == 6):
      break
    else:
      print("-------------------------------------------------------------------------------")
      print("Has ingresado una opción no válida")
      print("-------------------------------------------------------------------------------")

