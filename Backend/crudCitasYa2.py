import mysql.connector
from mysql.connector import Error


class conexion():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host="127.0.0.1",
                port=3307,
                user="root",
                password="root",
                db="citasya"
            )
        except:
            print("Error en la conexion")

    ## Insertar informacion personal para login
    def insertarValores(self,id_usuario,nombres,apellido,edad,genero,interes,bio_personal,limite_distancia,id_locacion,rango_edad):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                insertar="INSERT INTO Usuario VALUES('0001','John','Osbourne','40','M','Sin definir','Sin Bio','15Km','5001','35-45')"
                data=(id_usuario,nombres,apellido,edad,genero,interes,bio_personal,limite_distancia,id_locacion,rango_edad)
                cursor._executed(insertar,data)
                self.conexion.commit()
                self.conexion.close()
            except:
                print("Error en la conexion")

    ##Ver contactos unmatch
    def listarUnmatch(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM unmatch")
                resultados = cursor.fetchall()
                print(resultados)
                return resultados
            except:
                print("Error en la conexion")
##Buscar contactos match1
    def buscarObjeto(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                select="SELECT * from unmatch"
                cursor.execute(select)
                resultado=cursor.fetchall()
                self.conexion.close()
                return resultado

            except:
                print("Error en la conexion")
    ## Eliminar Contacto con match
    def eliminarContacto(self):
        if self.conexion.is_connected():
            try:
                borrar="DELETE FROM match1 WHERE id_match='001';"
                cursor=self.conexion.cursor()
                
                cursor.execute(borrar)
                self.conexion.commit()
                print(cursor.rowcount, "registro(s) borrado") 

            except:
                print("Error en la conexion")