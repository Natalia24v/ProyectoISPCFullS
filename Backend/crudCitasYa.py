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

    def listarTablas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM unmatch")
                resultados = cursor.fetchall()
                print(resultados)
                return resultados
            except:
                print("Error en la conexion")

    def select(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                msql_selectec = "SELECT * FROM unmatch"
                cursor.execute(msql_selectec)
                rows = cursor.fetchall()
                print(rows)
                cursor.close()
            except:
                print("Error en la conexion")

    def insertarValores(self,superlike,usuario,superlikeado):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                insertar="INSERT INTO superlike VALUES(%s,%s,%s)"
                data=(superlike,usuario,superlikeado)
                cursor._executed(insertar,data)
                self.conexion.commit()
                self.conexion.close()
            except:
                print("Error en la conexion")

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

    