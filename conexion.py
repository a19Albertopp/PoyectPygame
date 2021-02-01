from PyQt5 import QtWidgets, QtSql
from datetime import datetime
import var, puntuaciones


class Conexion():
    def db_connect(filename):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexion.\n' 'Haz Click para Cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión Establecida')
        return True

    def guardarPuntuacion():
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into marcador (puntos, nombre,fecha)'
            'VALUES (:puntos, :nombre,:fecha)')
        query.bindValue(':puntos', str(var.puntos))
        query.bindValue(':nombre', str(var.jugador))
        query.bindValue(':fecha', str(datetime.strftime(datetime.now(), "%d/%m/%Y")))

        if query.exec_():
            print("Guardado Correcto")
        else:
            print("Error Guardar Puntuacion: ", query.lastError().text())

    def puntuacionGlobal():
        query = QtSql.QSqlQuery()
        query.prepare('select nombre, puntos, fecha from marcador order by puntos DESC')
        i = 1
        var.contador_puntuacion_global = 0
        if query.exec_():
            y = var.window_height / 2-var.window_height/10
            x = var.window_width / 12
            while query.next():
                datos = [str(i), str(query.value(0)), str(query.value(1)), str(query.value(2))]
                puntuaciones.escribirPuntGlob(datos, x, y)
                y=y+var.window_height/25
                i += 1
                var.contador_puntuacion_global += 1

    def puntuacionPersonal():
        query = QtSql.QSqlQuery()
        query.prepare('select nombre, puntos, fecha from marcador where nombre=:nombre order by puntos DESC')
        query.bindValue(':nombre',str(var.jugador))
        i=1
        var.contador_puntuacion_personal=0
        if query.exec_():
            y = var.window_height / 2-var.window_height/10
            x = var.window_width / 1.73
            while query.next():
                datos = [str(i), str(query.value(0)), str(query.value(1)), str(query.value(2))]
                puntuaciones.escribirPuntPers(datos,x,y)
                y = y + var.window_height / 25
                i += 1
                var.contador_puntuacion_personal += 1
