# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VenChocar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VenChocar(object):
    def setupUi(self, VenChocar):
        VenChocar.setObjectName("VenChocar")
        VenChocar.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(VenChocar)
        self.centralwidget.setObjectName("centralwidget")
        self.btnJugar = QtWidgets.QPushButton(self.centralwidget)
        self.btnJugar.setGeometry(QtCore.QRect(280, 230, 221, 71))
        self.btnJugar.setObjectName("btnJugar")
        VenChocar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VenChocar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        VenChocar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VenChocar)
        self.statusbar.setObjectName("statusbar")
        VenChocar.setStatusBar(self.statusbar)

        self.retranslateUi(VenChocar)
        QtCore.QMetaObject.connectSlotsByName(VenChocar)

    def retranslateUi(self, VenChocar):
        _translate = QtCore.QCoreApplication.translate
        VenChocar.setWindowTitle(_translate("VenChocar", "MainWindow"))
        self.btnJugar.setText(_translate("VenChocar", "Jugar"))
