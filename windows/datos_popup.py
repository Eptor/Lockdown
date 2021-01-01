# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'datos_popup.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recursos


class Ui_data_popup(object):
    def setupUi(self, data_popup):
        if not data_popup.objectName():
            data_popup.setObjectName(u"data_popup")
        data_popup.resize(392, 286)
        icon = QIcon()
        icon.addFile(u":/logo/img/lockdown.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        data_popup.setWindowIcon(icon)
        data_popup.setStyleSheet(u"")
        self.nombre = QLabel(data_popup)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(20, 20, 360, 30))
        self.nombre.setStyleSheet(u"color: whitesmoke;")
        self.email = QLabel(data_popup)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(20, 70, 360, 30))
        self.email.setStyleSheet(u"color: whitesmoke;")
        self.password = QLabel(data_popup)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 120, 360, 30))
        self.password.setStyleSheet(u"color: whitesmoke;")
        self.link = QLabel(data_popup)
        self.link.setObjectName(u"link")
        self.link.setGeometry(QRect(20, 170, 361, 30))
        self.link.setStyleSheet(u"color: whitesmoke;")
        self.ok = QPushButton(data_popup)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(10, 250, 110, 28))
        self.copiar_c = QPushButton(data_popup)
        self.copiar_c.setObjectName(u"copiar_c")
        self.copiar_c.setGeometry(QRect(130, 250, 120, 28))
        self.copiar_l = QPushButton(data_popup)
        self.copiar_l.setObjectName(u"copiar_l")
        self.copiar_l.setGeometry(QRect(260, 250, 120, 28))
        self.label = QLabel(data_popup)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 410, 290))
        self.label.setStyleSheet(
            u"background-image: url(:/background/img/blurred_background.jpg);")
        self.dinamica = QLabel(data_popup)
        self.dinamica.setObjectName(u"dinamica")
        self.dinamica.setGeometry(QRect(10, 210, 370, 30))
        self.dinamica.setStyleSheet(u"color: whitesmoke;")
        self.dinamica.setAlignment(Qt.AlignCenter)
        self.label.raise_()
        self.nombre.raise_()
        self.email.raise_()
        self.password.raise_()
        self.link.raise_()
        self.ok.raise_()
        self.copiar_c.raise_()
        self.copiar_l.raise_()
        self.dinamica.raise_()

        self.retranslateUi(data_popup)

        QMetaObject.connectSlotsByName(data_popup)
    # setupUi

    def retranslateUi(self, data_popup):
        data_popup.setWindowTitle(
            QCoreApplication.translate("data_popup", u"Datos", None))
        self.nombre.setText(QCoreApplication.translate(
            "data_popup", u"Nombre:", None))
        self.email.setText(QCoreApplication.translate(
            "data_popup", u"Nombre:", None))
        self.password.setText(QCoreApplication.translate(
            "data_popup", u"Nombre:", None))
        self.link.setText(QCoreApplication.translate(
            "data_popup", u"Nombre:", None))
        self.ok.setText(QCoreApplication.translate("data_popup", u"OK", None))
        self.copiar_c.setText(QCoreApplication.translate(
            "data_popup", u"Copiar contrase\u00f1a", None))
        self.copiar_l.setText(QCoreApplication.translate(
            "data_popup", u"Copiar link", None))
        self.label.setText("")
        self.dinamica.setText("")
    # retranslateUi
