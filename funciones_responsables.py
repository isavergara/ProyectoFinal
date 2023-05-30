from BaseDeDatos.conexion import DAO

# Función para agregar responsable
def agregar_responsable():
      dao = DAO()
      # Ciclo para pedir el código del responsable
      while True:
        try:
          codigo_responsable = int(input("Ingresa el código del responsable: "))
          print("- - - - - - - - - - - - - - - - -")
          break
        except ValueError:
          print("Error: Por favor, ingrese un número válido.")
          print("- - - - - - - - - - - - - - - - -")

      # Ciclo para pedir el nombre del responsable
      while True:
        nombre = input("Ingrese el nombre del responsable: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(nombre) != 0:
          break
        print("Ingresa un nombre (no has ingresado nada)")

      # Ciclo para pedir el nombre del responsable
      while True:
        apellido = input("Ingrese el apellido del responsable: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(nombre) != 0:
          break
        print("Ingresa un apellido (no has ingresado nada)")

      # Ciclo para pedir el código del responsable
      while True:
        try:
          numero_documento = int(input("Ingresa el número de identidad del responsable: "))
          print("- - - - - - - - - - - - - - - - -")
          break
        except ValueError:
          print("Error: Por favor, ingrese un número de identidad válido.")
          print("- - - - - - - - - - - - - - - - -")

      # Ciclo para pedir el nombre del responsable
      while True:
        cargo = input("Ingrese el cargo del responsable: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(nombre) != 0:
          break
        print("Ingresa un cargo (no has ingresado nada)")
      
      data_del_responsable = [codigo_responsable, nombre, apellido, numero_documento, cargo]
      dao.registrarResponsable(data_del_responsable)

# Función para modificar responsable
def modificar_responsable():
      dao = DAO()
      # Ciclo para pedir el código del responsable
      while True:
        try:
          codigo_responsable = int(input("Ingresa el código del responsable: "))
          print("- - - - - - - - - - - - - - - - -")
          responsable_encontrado = dao.encontrarResponsableConCodigo(codigo_responsable)
          if(len(responsable_encontrado) == 0):
            print("No se ha encontrado ningún responsable con esa identificación")
            print("- - - - - - - - - - - - - - - - -")
          else:
            break
        except ValueError:
          print("Error: Por favor, ingrese un código válido.")
          print("- - - - - - - - - - - - - - - - -")

      # Ciclo para pedir el nombre del responsable
      while True:
        nombre = input("Ingrese el nombre del responsable: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(nombre) != 0:
          break
        print("Ingresa un nombre (no has ingresado nada)")

      # Ciclo para pedir el nombre del responsable
      while True:
        apellido = input("Ingrese el apellido del responsable: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(nombre) != 0:
          break
        print("Ingresa un apellido (no has ingresado nada)")

      # Ciclo para pedir el código del responsable
      while True:
        try:
          numero_documento = int(input("Ingresa el número de identidad del responsable: "))
          print("- - - - - - - - - - - - - - - - -")
          break
        except ValueError:
          print("Error: Por favor, ingrese un número de identidad válido.")
          print("- - - - - - - - - - - - - - - - -")

      # Ciclo para pedir el nombre del responsable
      while True:
        cargo = input("Ingrese el cargo del responsable: ")
        print("- - - - - - - - - - - - - - - - -")
        if len(nombre) != 0:
          break
        print("Ingresa un cargo (no has ingresado nada)")
      
      data_del_responsable = [codigo_responsable, nombre, apellido, numero_documento, cargo]
      dao.actualizarResponsable(data_del_responsable)

#Función para eliminar responsables
def eliminar_responsable():
  dao = DAO()
  # Ciclo para pedir el código del responsable
  while True:
    try:
      codigo_responsable = int(input("Ingresa el código del responsable: "))
      print("- - - - - - - - - - - - - - - - -")
      responsable_encontrado = dao.encontrarResponsableConCodigo(codigo_responsable)
      if(len(responsable_encontrado) == 0):
        print("No se ha encontrado ningún responsable con esa identificación")
        print("- - - - - - - - - - - - - - - - -")
      else:
        break
    except ValueError:
      print("Error: Por favor, ingrese un código válido.")
      print("- - - - - - - - - - - - - - - - -")
  
  dao.eliminarResponsable(codigo_responsable)

# Función para buscar responsables
def buscar_responsable():
  dao = DAO()
  # Ciclo para pedir el código del responsable
  while True:
    try:
      codigo_responsable = int(input("Ingresa el código del responsable: "))
      print("- - - - - - - - - - - - - - - - -")
      responsable_encontrado = dao.encontrarResponsableConCodigo(codigo_responsable)
      if(len(responsable_encontrado) == 0):
        print("No se ha encontrado ningún responsable con esa identificación")
        print("- - - - - - - - - - - - - - - - -")
        break
      else:
        datos = "Código: {0} | Nombre: '{1}' | Apellido: '{2}' | Documento: {3} | Cargo: {4}"
        print(datos.format(responsable_encontrado[0][0], responsable_encontrado[0][1], responsable_encontrado[0][2], responsable_encontrado[0][3], responsable_encontrado[0][4]))
        break
    except ValueError:
      print("Error: Por favor, ingrese un código válido.")
      print("- - - - - - - - - - - - - - - - -")

def mostrarResponsables():
    dao = DAO()
    print("\Responsables: \n")
    contador = 1
    responsables = dao.listarResponsables()
    if(len(responsables)==0):
      print("--------------")
      print("No hay responsables registrados")
      print("--------------")
    else:
      for responsable in responsables:
        datos = "{0}. Código: {1} | Nombre: '{2}' | Apellido: '{3}' | Documento: {4} | Cargo: {5}"
        print(datos.format(contador, responsable[0], responsable[1], responsable[2], responsable[3], responsable[4]))
        contador = contador + 1
    print(" ")

# Función para mostrar menú de responsables
def mostrar_menu_responsables():
  while True:
    # Se muestran las opciones que el usuario puede elegir
    print("Opciones (CRUD RESPONSABLES):")
    print("1. Ingresar Responsable")
    print("2. Modificar Responsable")
    print("3. Eliminar Responsable")
    print("4. Buscar responsable")
    print("5. Mostrar responsables")
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
      agregar_responsable()
      break
    elif(opcion == 2):
      modificar_responsable()
    elif(opcion == 3):
      eliminar_responsable()
    elif(opcion == 4):
      buscar_responsable()
    elif(opcion == 5):
      mostrarResponsables()
    elif(opcion == 6):
      break
    else:
      print("-------------------------------------------------------------------------------")
      print("Has ingresado una opción no válida")
      print("-------------------------------------------------------------------------------")

