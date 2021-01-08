# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
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
        icon.addFile(u":/logo/img/lockdown.png", QSize(), QIcon.Normal,
                     QIcon.Off)
        menu_window.setWindowIcon(icon)
        self.centralwidget_menu = QWidget(menu_window)
        self.centralwidget_menu.setObjectName(u"centralwidget_menu")
        self.centralwidget_menu.setStyleSheet(u"")
        self.listWidget = QListWidget(self.centralwidget_menu)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(249, 30, 541, 280))
        self.listWidget.setLayoutDirection(Qt.LeftToRight)
        self.listWidget.setStyleSheet(
            u"border: 2px dotted rgb(255, 178, 230);\n"
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
        self.fondo.setGeometry(QRect(0, 0, 801, 641))
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
        icon1.addFile(u":/copiar/img/copy.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.copiar.setIcon(icon1)
        self.tipo = QCheckBox(self.centralwidget_menu)
        self.tipo.setObjectName(u"tipo")
        self.tipo.setGeometry(QRect(35, 376, 101, 20))
        self.tipo.setStyleSheet(u"")
        self.tipo.setChecked(True)
        self.add = QPushButton(self.centralwidget_menu)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(10, 90, 220, 41))
        self.copyright = QLabel(self.centralwidget_menu)
        self.copyright.setObjectName(u"copyright")
        self.copyright.setGeometry(QRect(0, 2, 190, 21))
        font = QFont()
        font.setFamily(u"Nunito Sans")
        font.setPointSize(8)
        self.copyright.setFont(font)
        self.copyright.setStyleSheet(u"color:whitesmoke;")
        self.copyright.setAlignment(Qt.AlignCenter)
        self.refresh = QPushButton(self.centralwidget_menu)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setGeometry(QRect(759, 5, 20, 20))
        self.refresh.setStyleSheet(
            u"background-color: transparent;border-radius:0px;")
        icon2 = QIcon()
        icon2.addFile(u":/refresh/img/refresh.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.refresh.setIcon(icon2)
        self.morse_input = QTextEdit(self.centralwidget_menu)
        self.morse_input.setObjectName(u"morse_input")
        self.morse_input.setGeometry(QRect(70, 450, 721, 71))
        self.morse_input.setStyleSheet(
            u"border: 2px dotted rgb(255, 178, 230);\n"
            "background: rgba(167, 204, 237, 30);\n"
            "border-radius: 3px;")
        self.morse_input.setAcceptRichText(False)
        self.morse_output = QTextEdit(self.centralwidget_menu)
        self.morse_output.setObjectName(u"morse_output")
        self.morse_output.setGeometry(QRect(70, 530, 721, 71))
        self.morse_output.setStyleSheet(
            u"border: 2px dotted rgb(255, 178, 230);\n"
            "background: rgba(167, 204, 237, 30);\n"
            "border-radius: 3px;")
        self.morse_output.setReadOnly(True)
        self.convertir = QPushButton(self.centralwidget_menu)
        self.convertir.setObjectName(u"convertir")
        self.convertir.setGeometry(QRect(10, 450, 50, 70))
        icon3 = QIcon()
        icon3.addFile(u":/convertir/img/convertir.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.convertir.setIcon(icon3)
        self.copiar_morse = QPushButton(self.centralwidget_menu)
        self.copiar_morse.setObjectName(u"copiar_morse")
        self.copiar_morse.setGeometry(QRect(10, 530, 50, 70))
        self.copiar_morse.setIcon(icon1)
        self.drop_button = QPushButton(self.centralwidget_menu)
        self.drop_button.setObjectName(u"drop_button")
        self.drop_button.setGeometry(QRect(760, 377, 20, 20))
        self.drop_button.setStyleSheet(
            u"background-color: transparent;border-radius:0px;")
        icon4 = QIcon()
        icon4.addFile(u":/drop/img/drop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.drop_button.setIcon(icon4)
        self.drop_button.setIconSize(QSize(30, 30))
        self.descripcion_drop = QLabel(self.centralwidget_menu)
        self.descripcion_drop.setObjectName(u"descripcion_drop")
        self.descripcion_drop.setGeometry(QRect(10, 420, 261, 16))
        self.descripcion_drop.setStyleSheet(u"color:whitesmoke;")
        self.descripcion_drop.setFrameShape(QFrame.NoFrame)
        self.descripcion_drop.setFrameShadow(QFrame.Sunken)
        self.esconder_img = QPushButton(self.centralwidget_menu)
        self.esconder_img.setObjectName(u"esconder_img")
        self.esconder_img.setGeometry(QRect(10, 607, 120, 28))
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
        self.copyright.raise_()
        self.refresh.raise_()
        self.morse_input.raise_()
        self.morse_output.raise_()
        self.convertir.raise_()
        self.copiar_morse.raise_()
        self.drop_button.raise_()
        self.descripcion_drop.raise_()
        self.esconder_img.raise_()

        self.retranslateUi(menu_window)

        QMetaObject.connectSlotsByName(menu_window)

    # setupUi

    def retranslateUi(self, menu_window):
        menu_window.setWindowTitle(
            QCoreApplication.translate("menu_window", u"Lockdown", None))
        self.ver.setText(
            QCoreApplication.translate("menu_window", u"Ver registro", None))
        self.editar.setText(
            QCoreApplication.translate("menu_window", u"Editar registro",
                                       None))
        self.eliminar.setText(
            QCoreApplication.translate("menu_window", u"Eliminar registro",
                                       None))
        self.respaldo.setText(
            QCoreApplication.translate("menu_window", u"Repaldo / Backup",
                                       None))
        self.fondo.setText("")
        self.generar.setText(
            QCoreApplication.translate("menu_window", u"Generar", None))
        self.copiar.setText("")
        self.tipo.setText(
            QCoreApplication.translate("menu_window",
                                       u"!\"\u00b7$%&/()=?\u00bf\u00a1'",
                                       None))
        self.add.setText(
            QCoreApplication.translate("menu_window", u"A\u00f1adir registro",
                                       None))
        self.copyright.setText(
            QCoreApplication.translate("menu_window",
                                       u"\u00a9 Lockdown - Hector Espinoza",
                                       None))
        self.refresh.setText("")
        self.convertir.setText("")
        self.copiar_morse.setText("")
        self.drop_button.setText("")
        self.descripcion_drop.setText(
            QCoreApplication.translate(
                "menu_window", u"Traductor de codigo morse, no usar acentos.",
                None))
        self.esconder_img.setText(
            QCoreApplication.translate("menu_window", u"Esconder archivos",
                                       None))

    # retranslateUi
