# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dec_files.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recursos


class Ui_decrypt_menu(object):
    def setupUi(self, decrypt_menu):
        if not decrypt_menu.objectName():
            decrypt_menu.setObjectName(u"decrypt_menu")
        decrypt_menu.resize(641, 133)
        icon = QIcon()
        icon.addFile(u":/logo/img/Hides.ico", QSize(), QIcon.Normal, QIcon.Off)
        decrypt_menu.setWindowIcon(icon)
        self.centralwidget = QWidget(decrypt_menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.unzip_file_search = QPushButton(self.centralwidget)
        self.unzip_file_search.setObjectName(u"unzip_file_search")
        self.unzip_file_search.setGeometry(QRect(534, 10, 101, 23))
        icon1 = QIcon()
        icon1.addFile(u":/files/img/esconder.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.unzip_file_search.setIcon(icon1)
        self.unzip_file_search.setIconSize(QSize(15, 15))
        self.unzip_file = QLineEdit(self.centralwidget)
        self.unzip_file.setObjectName(u"unzip_file")
        self.unzip_file.setGeometry(QRect(10, 10, 511, 21))
        self.unzip_file.setStyleSheet(
            u"border: 2px dotted rgb(255, 178, 230);\n"
            "background: rgba(167, 204, 237, 30);\n"
            "border-radius: 3px;\n"
            "color:white;")
        self.unzip_file.setReadOnly(True)
        self.output_dir_search = QPushButton(self.centralwidget)
        self.output_dir_search.setObjectName(u"output_dir_search")
        self.output_dir_search.setGeometry(QRect(534, 50, 101, 23))
        icon2 = QIcon()
        icon2.addFile(u":/files/img/folder.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.output_dir_search.setIcon(icon2)
        self.output_dir_search.setIconSize(QSize(15, 15))
        self.output_dir = QLineEdit(self.centralwidget)
        self.output_dir.setObjectName(u"output_dir")
        self.output_dir.setGeometry(QRect(10, 50, 511, 21))
        self.output_dir.setStyleSheet(
            u"border: 2px dotted rgb(255, 178, 230);\n"
            "background: rgba(167, 204, 237, 30);\n"
            "border-radius: 3px;\n"
            "color:white;")
        self.output_dir.setReadOnly(True)
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(10, 80, 620, 41))
        self.start.setLayoutDirection(Qt.RightToLeft)
        icon3 = QIcon()
        icon3.addFile(u":/files/img/guardar.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.start.setIcon(icon3)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-50, -20, 760, 180))
        self.label.setStyleSheet(
            u"background-image: url(:/background/img/blurred_background.jpg);")
        decrypt_menu.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.unzip_file_search.raise_()
        self.unzip_file.raise_()
        self.output_dir_search.raise_()
        self.output_dir.raise_()
        self.start.raise_()

        self.retranslateUi(decrypt_menu)

        QMetaObject.connectSlotsByName(decrypt_menu)

    # setupUi

    def retranslateUi(self, decrypt_menu):
        decrypt_menu.setWindowTitle(
            QCoreApplication.translate("decrypt_menu",
                                       u"Hides - El ocultador de archivos",
                                       None))
        self.unzip_file_search.setText("")
        self.unzip_file.setPlaceholderText(
            QCoreApplication.translate("decrypt_menu", u"Archivo secreto",
                                       None))
        self.output_dir_search.setText("")
        self.output_dir.setPlaceholderText(
            QCoreApplication.translate("decrypt_menu",
                                       u"Directorio de destino", None))
        self.start.setText(
            QCoreApplication.translate("decrypt_menu", u"Revelar archivos  ",
                                       None))
        self.label.setText("")

    # retranslateUi
