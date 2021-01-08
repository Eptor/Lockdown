# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enc_files.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recursos


class Ui_encrypt_menu(object):
    def setupUi(self, encrypt_menu):
        if not encrypt_menu.objectName():
            encrypt_menu.setObjectName(u"encrypt_menu")
        encrypt_menu.setEnabled(True)
        encrypt_menu.resize(665, 271)
        icon = QIcon()
        icon.addFile(u"../Icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        encrypt_menu.setWindowIcon(icon)
        self.centralwidget = QWidget(encrypt_menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.files_list = QListWidget(self.centralwidget)
        self.files_list.setObjectName(u"files_list")
        self.files_list.setGeometry(QRect(10, 10, 321, 211))
        self.files_list.setStyleSheet(
            u"border: 2px dotted rgb(255, 178, 230);\n"
            "background: rgba(167, 204, 237, 30);\n"
            "border-radius: 10px;")
        self.search_folder = QPushButton(self.centralwidget)
        self.search_folder.setObjectName(u"search_folder")
        self.search_folder.setGeometry(QRect(10, 230, 321, 31))
        icon1 = QIcon()
        icon1.addFile(u":/files/img/folder.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.search_folder.setIcon(icon1)
        self.original_img = QLineEdit(self.centralwidget)
        self.original_img.setObjectName(u"original_img")
        self.original_img.setEnabled(True)
        self.original_img.setGeometry(QRect(350, 40, 220, 20))
        self.original_img.setStyleSheet(
            u"border: 2px dotted rgb(255, 178, 230);\n"
            "background: rgba(167, 204, 237, 30);\n"
            "border-radius: 3px;")
        self.original_img.setReadOnly(True)
        self.original_img_label = QLabel(self.centralwidget)
        self.original_img_label.setObjectName(u"original_img_label")
        self.original_img_label.setGeometry(QRect(350, 10, 221, 16))
        self.search_image = QPushButton(self.centralwidget)
        self.search_image.setObjectName(u"search_image")
        self.search_image.setGeometry(QRect(580, 20, 80, 60))
        icon2 = QIcon()
        icon2.addFile(u":/files/img/imagen.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.search_image.setIcon(icon2)
        self.search_image.setIconSize(QSize(30, 30))
        self.new_name_label = QLabel(self.centralwidget)
        self.new_name_label.setObjectName(u"new_name_label")
        self.new_name_label.setGeometry(QRect(350, 170, 251, 16))
        self.new_name = QLineEdit(self.centralwidget)
        self.new_name.setObjectName(u"new_name")
        self.new_name.setEnabled(True)
        self.new_name.setGeometry(QRect(350, 190, 301, 21))
        self.new_name.setStyleSheet(u"border: 2px dotted rgb(255, 178, 230);\n"
                                    "background: rgba(167, 204, 237, 30);\n"
                                    "border-radius: 3px;")
        self.new_name.setReadOnly(False)
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(350, 220, 301, 40))
        self.start.setLayoutDirection(Qt.RightToLeft)
        icon3 = QIcon()
        icon3.addFile(u":/files/img/esconder.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.start.setIcon(icon3)
        self.new_location_label = QLabel(self.centralwidget)
        self.new_location_label.setObjectName(u"new_location_label")
        self.new_location_label.setGeometry(QRect(350, 90, 221, 16))
        self.new_location = QLineEdit(self.centralwidget)
        self.new_location.setObjectName(u"new_location")
        self.new_location.setEnabled(True)
        self.new_location.setGeometry(QRect(353, 120, 220, 21))
        self.new_location.setStyleSheet(
            u"border: 2px dotted rgb(255, 178, 230);\n"
            "background: rgba(167, 204, 237, 30);\n"
            "border-radius: 3px;")
        self.new_location.setReadOnly(True)
        self.search_location = QPushButton(self.centralwidget)
        self.search_location.setObjectName(u"search_location")
        self.search_location.setGeometry(QRect(580, 100, 75, 60))
        icon4 = QIcon()
        icon4.addFile(u":/files/img/guardar.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.search_location.setIcon(icon4)
        self.search_location.setIconSize(QSize(30, 30))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 670, 271))
        self.label.setStyleSheet(
            u"background-image: url(:/background/img/blurred_background.jpg);")
        encrypt_menu.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.files_list.raise_()
        self.search_folder.raise_()
        self.original_img.raise_()
        self.original_img_label.raise_()
        self.search_image.raise_()
        self.new_name_label.raise_()
        self.new_name.raise_()
        self.start.raise_()
        self.new_location_label.raise_()
        self.new_location.raise_()
        self.search_location.raise_()

        self.retranslateUi(encrypt_menu)

        QMetaObject.connectSlotsByName(encrypt_menu)

    # setupUi

    def retranslateUi(self, encrypt_menu):
        encrypt_menu.setWindowTitle(
            QCoreApplication.translate("encrypt_menu",
                                       u"Hides - El ocultador de archivos",
                                       None))
        self.search_folder.setText("")
        self.original_img_label.setText(
            QCoreApplication.translate("encrypt_menu", u"Foto original", None))
        self.search_image.setText("")
        self.new_name_label.setText(
            QCoreApplication.translate(
                "encrypt_menu", u"Nombre del nuevo archivo (sin extension)",
                None))
        self.new_name.setPlaceholderText(
            QCoreApplication.translate("encrypt_menu", u"Ej: Archivo_oculto",
                                       None))
        self.start.setText(
            QCoreApplication.translate("encrypt_menu", u"Esconder archivos   ",
                                       None))
        self.new_location_label.setText(
            QCoreApplication.translate("encrypt_menu",
                                       u"Directorio de destino", None))
        self.search_location.setText("")
        self.label.setText("")

    # retranslateUi
