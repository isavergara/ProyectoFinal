from BaseDeDatos.conexion import DAO

# Función para agregar equipo
def agregar_equipo():
      dao = DAO()
       # Ciclo para pedir el serial del equipo
      while True:
        serial = input("Ingrese el serial del equipo: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(serial) != 0:
          break
        print("Ingresa un serial (no has ingresado nada)")

        # Ciclo para pedir el número de activo
      while True:
        try:
          numero_activo = int(input("Ingresa el número de activo del equipo: "))
          print("- - - - - - - - - - - - - - - - -")
          break
        except ValueError:
          print("Error: Por favor, ingrese un número de activo válido.")
          print("- - - - - - - - - - - - - - - - -")

      # Ciclo para pedir el nombre del equipo
      while True:
        nombre = input("Ingrese el nombre del equipo: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(nombre) != 0:
          break
        print("Ingresa un nombre para el equipo (no has ingresado nada)")

      # Ciclo para pedir la marca del equipo
      while True:
        marca = input("Ingrese la marca del equipo: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(marca) != 0:
          break
        print("Ingresa una marca para el equipo (no has ingresado nada)")

      # Ciclo para pedir el código del responsable
      while True:
        try:
          codigo_responsable = int(input("Ingresa el código del responsable: "))
          print("- - - - - - - - - - - - - - - - -")
          responsable_encontrado = dao.encontrarResponsableConCodigo(codigo_responsable)
          print(len(responsable_encontrado))
          if(len(responsable_encontrado) == 0):
            print("No se ha encontrado ningún equipo con ese código")
            print("- - - - - - - - - - - - - - - - -")
          else:
            break
        except ValueError:
          print("Error: Por favor, ingrese un código válido.")
          print("- - - - - - - - - - - - - - - - -")

      # Ciclo para pedir el código de la ubicación
      while True:
        try:
          codigo_ubicacion = int(input("Ingresa el código de la ubicación: "))
          print("- - - - - - - - - - - - - - - - -")
          ubicacion_encontrada = dao.encontrarUbicacionConCodigo(codigo_responsable)
          if(len(ubicacion_encontrada) == 0):
            print("No se ha encontrado ninguna ubicación con ese código")
            print("- - - - - - - - - - - - - - - - -")
          else:
            break
        except ValueError:
          print("Error: Por favor, ingrese un código válido.")
          print("- - - - - - - - - - - - - - - - -")
        
      data_del_equipo = [serial, numero_activo, nombre, marca, codigo_responsable, codigo_ubicacion]
      dao.registrarEquipo(data_del_equipo)

# Función para modificar equipo
def modificar_equipo():
      dao = DAO()
      # Ciclo para pedir el código del equipo
      while True:
        try:
          numero_activo = int(input("Ingresa el número de activo del equipo: "))
          print("- - - - - - - - - - - - - - - - -")
          equipo_encontrado = dao.encontrarEquipoConCodigo(numero_activo)
          if(len(equipo_encontrado) == 0):
            print("No se ha encontrado ningún equipo con esa identificación")
            print("- - - - - - - - - - - - - - - - -")
          else:
            break
        except ValueError:
          print("Error: Por favor, ingrese un código válido.")
          print("- - - - - - - - - - - - - - - - -")

      # Ciclo para pedir el serial del equipo
      while True:
        serial = input("Ingrese el serial del equipo: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(serial) != 0:
          break
        print("Ingresa un serial (no has ingresado nada)")

      # Ciclo para pedir el nombre del equipo
      while True:
        nombre = input("Ingrese el nombre del equipo: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(nombre) != 0:
          break
        print("Ingresa un nombre para el equipo (no has ingresado nada)")

      # Ciclo para pedir la marca del equipo
      while True:
        marca = input("Ingrese la marca del equipo: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(marca) != 0:
          break
        print("Ingresa una marca para el equipo (no has ingresado nada)")

      # Ciclo para pedir el código del responsable
      while True:
        try:
          codigo_responsable = int(input("Ingresa el código del responsable: "))
          print("- - - - - - - - - - - - - - - - -")
          responsable_encontrado = dao.encontrarResponsableConCodigo(codigo_responsable)
          print(len(responsable_encontrado))
          if(len(responsable_encontrado) == 0):
            print("No se ha encontrado ningún equipo con ese código")
            print("- - - - - - - - - - - - - - - - -")
          else:
            break
        except ValueError:
          print("Error: Por favor, ingrese un código válido.")
          print("- - - - - - - - - - - - - - - - -")

      # Ciclo para pedir el código de la ubicación
      while True:
        try:
          codigo_ubicacion = int(input("Ingresa el código de la ubicación: "))
          print("- - - - - - - - - - - - - - - - -")
          ubicacion_encontrada = dao.encontrarUbicacionConCodigo(codigo_responsable)
          if(len(ubicacion_encontrada) == 0):
            print("No se ha encontrado ninguna ubicación con ese código")
            print("- - - - - - - - - - - - - - - - -")
          else:
            break
        except ValueError:
          print("Error: Por favor, ingrese un código válido.")
          print("- - - - - - - - - - - - - - - - -")
        
      data_del_equipo = [serial, numero_activo, nombre, marca, codigo_responsable, codigo_ubicacion]
      dao.actualizarEquipo(data_del_equipo)

#Función para eliminar equipos
def eliminar_equipo():
  dao = DAO()
  # Ciclo para pedir el código del equipo
  while True:
    try:
      codigo_equipo = int(input("Ingresa el código del equipo: "))
      print("- - - - - - - - - - - - - - - - -")
      equipo_encontrado = dao.encontrarEquipoConCodigo(codigo_equipo)
      if(len(equipo_encontrado) == 0):
        print("No se ha encontrado ningún equipo con esa identificación")
        print("- - - - - - - - - - - - - - - - -")
      else:
        break
    except ValueError:
      print("Error: Por favor, ingrese un código válido.")
      print("- - - - - - - - - - - - - - - - -")
  
  dao.eliminarEquipo(codigo_equipo)

# Función para buscar equipos
def buscar_equipo():
  dao = DAO()
  # Ciclo para pedir el código del equipo
  while True:
    try:
      codigo_equipo = int(input("Ingresa el código del equipo: "))
      print("- - - - - - - - - - - - - - - - -")
      equipo_encontrado = dao.encontrarEquipoConCodigo(codigo_equipo)
      if(len(equipo_encontrado) == 0):
        print("No se ha encontrado ningún equipo con esa identificación")
        print("- - - - - - - - - - - - - - - - -")
        break
      else:
        datos = "Código: {0} | Nombre: '{1}' | Apellido: '{2}' | Documento: {3} | Cargo: {4}"
        print(datos.format(equipo_encontrado[0][0], equipo_encontrado[0][1], equipo_encontrado[0][2], equipo_encontrado[0][3], equipo_encontrado[0][4]))
        break
    except ValueError:
      print("Error: Por favor, ingrese un código válido.")
      print("- - - - - - - - - - - - - - - - -")

def mostrarEquipos():
    dao = DAO()
    print("\equipos: \n")
    contador = 1
    equipos = dao.listarEquipos()
    for equipo in equipos:
        datos = "{0}. Serial: '{1}' | NumeroActivo: {2} | NombreEquipo: '{3}' | Marca: '{4}' | CodigoUbicación: {5} | CodigoResponsable: {6}"
        print(datos.format(contador, equipo[0], equipo[1], equipo[2], equipo[3], equipo[4], equipo[5]))
        contador = contador + 1
    print(" ")

# Función para mostrar menú de equipos
def mostrar_menu_equipos():
  while True:
    # Se muestran las opciones que el usuario puede elegir
    print("Opciones (CRUD equipos):")
    print("1. Ingresar equipo")
    print("2. Modificar equipo")
    print("3. Eliminar equipo")
    print("4. Buscar equipo")
    print("5. Mostrar equipos")
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
      agregar_equipo()
    elif(opcion == 2):
      modificar_equipo()
    elif(opcion == 3):
      eliminar_equipo()
    elif(opcion == 4):
      buscar_equipo()
    elif(opcion == 5):
      mostrarEquipos()
    elif(opcion == 6):
      break
    else:
      print("-------------------------------------------------------------------------------")
      print("Has ingresado una opción no válida")
      print("-------------------------------------------------------------------------------")

