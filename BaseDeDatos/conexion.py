import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='informatica1',
                password='bio123',
                db='informatica1'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def encontrarResponsableConCodigo(self, codigo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "select * from responsables where CodigoResponsable = {0}"
                cursor.execute(sql.format(codigo))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def encontrarUbicacionConCodigo(self, codigo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "select * from ubicaciones where CodigoUbicacion = {0}"
                cursor.execute(sql.format(codigo))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Función para encontrar equipo con código
    def encontrarEquipoConCodigo(self, NumeroActivo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "select * from equipos where NumeroActivo = {0}"
                cursor.execute(sql.format(NumeroActivo))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Función para obtener todos los responsables
    def listarResponsables(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM responsables")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Función para obtener todas las ubicaciones
    def listarUbicaciones(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM ubicaciones")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Función para obtener todas los equipos
    def listarEquipos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM equipos")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Función para registrar al responsable
    def registrarResponsable(self, responsable):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO responsables (codigoResponsable, Nombre, Apellido, NumeroDocumento, Cargo) VALUES ({0}, '{1}', '{2}',{3},'{4}')"
                cursor.execute(sql.format(responsable[0], responsable[1], responsable[2],responsable[3],responsable[4]))
                self.conexion.commit()
                print("¡Responsable registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Función para registrar al responsable
    def registrarEquipo(self, equipo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO equipos (serial, NumeroActivo, NombreEquipo, Marca, CodigoUbicacion, CodigoResponsable) VALUES ('{0}',{1}, '{2}','{3}',{4},{5})"
                cursor.execute(sql.format(equipo[0], equipo[1], equipo[2],equipo[3],equipo[4], equipo[5]))
                self.conexion.commit()
                print("¡Responsable registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    #Función para registrar la ubicación
    def registrarUbicacion(self, responsable):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO ubicaciones (codigoUbicacion, NombreUbicacion, piso) VALUES ({0}, '{1}', {2})"
                cursor.execute(sql.format(responsable[0], responsable[1], responsable[2]))
                self.conexion.commit()
                print("¡Ubicación registrada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarResponsable(self, responsable):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE responsables SET Nombre = '{0}', Apellido = '{1}', NumeroDocumento = {2}, Cargo = '{3}' WHERE CodigoResponsable = '{4}'"
                cursor.execute(sql.format(responsable[1], responsable[2], responsable[3], responsable[4], responsable[0]))
                self.conexion.commit()
                print("¡Responsable actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarUbicacion(self, ubicacion):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE ubicaciones SET NombreUbicacion = '{0}', Piso = {1} WHERE CodigoUbicacion = '{2}'"
                cursor.execute(sql.format(ubicacion[1], ubicacion[2], ubicacion[0]))
                self.conexion.commit()
                print("¡Ubicación actualizada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def actualizarEquipo(self, equipo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE equipos SET serial = '{0}', NombreEquipo = '{1}', Marca='{2}', CodigoUbicacion={3}, CodigoResponsable={4} WHERE NumeroActivo = {5}"
                cursor.execute(sql.format(equipo[0], equipo[2], equipo[3],equipo[4],equipo[5],equipo[1]))
                self.conexion.commit()
                print("¡Ubicación actualizada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarResponsable(self, codigoResponsableEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM responsables WHERE CodigoResponsable = '{0}'"
                cursor.execute(sql.format(codigoResponsableEliminar))
                self.conexion.commit()
                print("¡Responsable eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarUbicacion(self, codigoUbicacionEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM ubicaciones WHERE CodigoUbicacion = '{0}'"
                cursor.execute(sql.format(codigoUbicacionEliminar))
                self.conexion.commit()
                print("¡Ubicación eliminada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarEquipo(self, codigoUbicacionEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM equipos WHERE NumeroActivo = '{0}'"
                cursor.execute(sql.format(codigoUbicacionEliminar))
                self.conexion.commit()
                print("Equipo eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
