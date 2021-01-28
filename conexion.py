from PyQt5 import QtWidgets, QtSql
from datetime import datetime
import var
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
