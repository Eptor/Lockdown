# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'menu.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recursos


class Ui_menu_window(object):
    def setupUi(self, menu_window):
        if not menu_window.objectName():
            menu_window.setObjectName(u"menu_window")
        menu_window.resize(800, 407)
        icon = QIcon()
        icon.addFile(u":/logo/img/lockdown.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        menu_window.setWindowIcon(icon)
        self.centralwidget_menu = QWidget(menu_window)
        self.centralwidget_menu.setObjectName(u"centralwidget_menu")
        self.centralwidget_menu.setStyleSheet(u"")
        self.listWidget = QListWidget(self.centralwidget_menu)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(249, 30, 541, 280))
        self.listWidget.setLayoutDirection(Qt.LeftToRight)
        self.listWidget.setStyleSheet(u"border: 2px dotted rgb(255, 178, 230);\n"
                                      "background: rgba(167, 204, 237, 30);\n"
                                      "border-radius: 10px;")
        self.listWidget.setFrameShape(QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QFrame.Sunken)
        self.ver = QPushButton(self.centralwidget_menu)
        self.ver.setObjectName(u"ver")
        self.ver.setGeometry(QRect(11, 30, 220, 41))
        self.editar = QPushButton(self.centralwidget_menu)
        self.editar.setObjectName(u"editar")
        self.editar.setGeometry(QRect(11, 150, 220, 41))
        self.eliminar = QPushButton(self.centralwidget_menu)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(11, 210, 220, 41))
        self.respaldo = QPushButton(self.centralwidget_menu)
        self.respaldo.setObjectName(u"respaldo")
        self.respaldo.setGeometry(QRect(11, 270, 220, 41))
        self.fondo = QLabel(self.centralwidget_menu)
        self.fondo.setObjectName(u"fondo")
        self.fondo.setGeometry(QRect(0, -2, 801, 460))
        self.fondo.setStyleSheet(
            u"background-image: url(:/background/img/blurred_background.jpg);")
        self.generar = QPushButton(self.centralwidget_menu)
        self.generar.setObjectName(u"generar")
        self.generar.setGeometry(QRect(10, 339, 150, 30))
        self.generar.setStyleSheet(u"")
        self.gen_text = QLineEdit(self.centralwidget_menu)
        self.gen_text.setObjectName(u"gen_text")
        self.gen_text.setGeometry(QRect(170, 339, 610, 30))
        self.gen_text.setStyleSheet(u"border: 2px dotted rgb(255, 178, 230);\n"
                                    "background: rgba(167, 204, 237, 30);\n"
                                    "border-radius: 3px;")
        self.gen_text.setAlignment(Qt.AlignCenter)
        self.copiar = QPushButton(self.centralwidget_menu)
        self.copiar.setObjectName(u"copiar")
        self.copiar.setGeometry(QRect(744, 340, 30, 28))
        self.copiar.setStyleSheet(
            u"background-color: transparent;border-radius:0px;")
        icon1 = QIcon()
        icon1.addFile(u":/copiar/img/copy.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.copiar.setIcon(icon1)
        self.tipo = QCheckBox(self.centralwidget_menu)
        self.tipo.setObjectName(u"tipo")
        self.tipo.setGeometry(QRect(35, 376, 101, 20))
        self.tipo.setStyleSheet(u"")
        self.tipo.setChecked(True)
        self.add = QPushButton(self.centralwidget_menu)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(10, 90, 220, 41))
        self.label = QLabel(self.centralwidget_menu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(610, 385, 190, 21))
        font = QFont()
        font.setFamily(u"Nunito Sans")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        menu_window.setCentralWidget(self.centralwidget_menu)
        self.fondo.raise_()
        self.listWidget.raise_()
        self.ver.raise_()
        self.editar.raise_()
        self.eliminar.raise_()
        self.respaldo.raise_()
        self.generar.raise_()
        self.gen_text.raise_()
        self.copiar.raise_()
        self.tipo.raise_()
        self.add.raise_()
        self.label.raise_()

        self.retranslateUi(menu_window)

        QMetaObject.connectSlotsByName(menu_window)
    # setupUi

    def retranslateUi(self, menu_window):
        menu_window.setWindowTitle(QCoreApplication.translate(
            "menu_window", u"Lockdown", None))
        self.ver.setText(QCoreApplication.translate(
            "menu_window", u"Ver registro", None))
        self.editar.setText(QCoreApplication.translate(
            "menu_window", u"Editar registro", None))
        self.eliminar.setText(QCoreApplication.translate(
            "menu_window", u"Eliminar registro", None))
        self.respaldo.setText(QCoreApplication.translate(
            "menu_window", u"Repaldo / Backup", None))
        self.fondo.setText("")
        self.generar.setText(QCoreApplication.translate(
            "menu_window", u"Generar", None))
        self.copiar.setText("")
        self.tipo.setText(QCoreApplication.translate(
            "menu_window", u"!\"\u00b7$%&/()=?\u00bf\u00a1'", None))
        self.add.setText(QCoreApplication.translate(
            "menu_window", u"A\u00f1adir registro", None))
        self.label.setText(QCoreApplication.translate(
            "menu_window", u"\u00a9 Lockdown - Hector Espinoza", None))
    # retranslateUi
