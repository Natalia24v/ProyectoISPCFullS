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
    def insertarValores(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                insertar="INSERT INTO usuario(id_usuario,nombres,apellido,edad,genero,interes,bio_personal,limite_distancia,id_locacion,rango_edad) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                data=("0001","John","Osbourne","35","M","Sin especificar","músico y compositor británico","20KM","5000","30-40")
                cursor.executed(insertar,data)
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
                for fila in cursor:
                    print(fila)
                conexion.close()
            except:
                print("Error en la conexion")
##Buscar contactos match1
    def buscarObjeto(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                select="SELECT id_usuario from match1"
                cursor.execute(select)
                for fila in cursor:
                    print(fila)
                conexion.close()

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
