# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recursos

class Ui_login_window(object):
    def setupUi(self, login_window):
        if not login_window.objectName():
            login_window.setObjectName(u"login_window")
        login_window.resize(374, 483)
        icon1 = QIcon()
        icon1.addFile(u":/logo/img/lockdown.png", QSize(), QIcon.Normal, QIcon.Off)
        login_window.setWindowIcon(icon1)
        self.actionOlvid_mi_contrase_a = QAction(login_window)
        self.actionOlvid_mi_contrase_a.setObjectName(u"actionOlvid_mi_contrase_a")
        self.actionRestaurar_base_de_datos = QAction(login_window)
        self.actionRestaurar_base_de_datos.setObjectName(u"actionRestaurar_base_de_datos")
        self.centralwidget_login = QWidget(login_window)
        self.centralwidget_login.setObjectName(u"centralwidget_login")
        self.centralwidget_login.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget_login.setStyleSheet(u"")
        self.user_input = QLineEdit(self.centralwidget_login)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setGeometry(QRect(10, 280, 351, 30))
        self.user_input.setLayoutDirection(Qt.LeftToRight)
        self.user_input.setStyleSheet(u"background-color: transparent;\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"")
        self.user_input.setAlignment(Qt.AlignCenter)
        self.password_input = QLineEdit(self.centralwidget_login)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(10, 340, 351, 30))
        self.password_input.setStyleSheet(u"background-color: transparent;\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setAlignment(Qt.AlignCenter)
        self.login = QPushButton(self.centralwidget_login)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(10, 389, 351, 41))
        self.login.setStyleSheet(u"background-color: rgba(243, 201, 139,90);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"")
        self.icon = QLabel(self.centralwidget_login)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(93, 40, 191, 191))
        self.icon.setStyleSheet(u"background-image: url(:/logo/img/lockdown.png);")
        self.user = QLabel(self.centralwidget_login)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(160, 260, 55, 16))
        self.user.setStyleSheet(u"color:white;")
        self.user.setAlignment(Qt.AlignCenter)
        self.password = QLabel(self.centralwidget_login)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(148, 320, 81, 16))
        self.password.setStyleSheet(u"color:white;")
        self.password.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget_login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 381, 461))
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.502, y1:0, x2:0.512, y2:1, stop:0 rgba(84, 94, 117, 255), stop:1 rgba(167, 204, 237, 255));")
        login_window.setCentralWidget(self.centralwidget_login)
        self.label.raise_()
        self.user_input.raise_()
        self.password_input.raise_()
        self.login.raise_()
        self.icon.raise_()
        self.user.raise_()
        self.password.raise_()
        self.menuBar = QMenuBar(login_window)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 374, 26))
        self.menuBar.setStyleSheet(u"background-color: rgb(84, 94, 117);")
        self.opciones = QMenu(self.menuBar)
        self.opciones.setObjectName(u"opciones")
        login_window.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.opciones.menuAction())
        self.opciones.addAction(self.actionOlvid_mi_contrase_a)
        self.opciones.addAction(self.actionRestaurar_base_de_datos)

        self.retranslateUi(login_window)

        QMetaObject.connectSlotsByName(login_window)
    # setupUi

    def retranslateUi(self, login_window):
        login_window.setWindowTitle(QCoreApplication.translate("login_window", u"Lockdown", None))
        self.actionOlvid_mi_contrase_a.setText(QCoreApplication.translate("login_window", u"Olvid\u00e9 mi contrase\u00f1a", None))
        self.actionRestaurar_base_de_datos.setText(QCoreApplication.translate("login_window", u"Restaurar base de datos", None))
        self.user_input.setPlaceholderText("")
        self.login.setText(QCoreApplication.translate("login_window", u"Iniciar sesi\u00f3n", None))
#if QT_CONFIG(shortcut)
        self.login.setShortcut(QCoreApplication.translate("login_window", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.icon.setText("")
        self.user.setText(QCoreApplication.translate("login_window", u"Usuario", None))
        self.password.setText(QCoreApplication.translate("login_window", u"Contrase\u00f1a", None))
        self.label.setText("")
        self.opciones.setTitle(QCoreApplication.translate("login_window", u"Opciones", None))
    # retranslateUi

