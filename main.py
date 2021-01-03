from random import randint
from PyQt5 import QtPrintSupport
from VenChocar import *
from Ven_Nombre import *
import pygame, var, sys, eventos, juego


class main(QtWidgets.QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        var.ui = Ui_VenChocar()
        var.ui.setupUi(self)
        QtWidgets.QAction(self).triggered.connect(self.close)
        var.ui.btnJugar.clicked.connect(eventos.eventosVentanas.abrirNombre)
        var.dlgNombre = DialogNombre()


class DialogNombre(QtWidgets.QDialog):
    def __init__(self):
        super(DialogNombre, self).__init__()
        var.dlgNombre = Ui_VenNombre()
        var.dlgNombre.setupUi(self)
        var.dlgNombre.btnBoxNombre.button(QtWidgets.QDialogButtonBox.Cancel).setText('CANCELAR')
        var.dlgNombre.btnBoxNombre.button(QtWidgets.QDialogButtonBox.Ok).setText('JUGAR')
        var.dlgNombre.btnBoxNombre.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(eventos.eventosVentanas.cerrarNombre)
        var.dlgNombre.btnBoxNombre.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(eventos.eventosVentanas.ValidarNombre)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    var.window = main()
    var.window.showMaximized()
    sys.exit(app.exec())
