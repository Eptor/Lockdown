# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'install_menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recursos


class Ui_install_menu(object):
    def setupUi(self, install_menu):
        if not install_menu.objectName():
            install_menu.setObjectName(u"install_menu")
        install_menu.resize(372, 112)
        icon = QIcon()
        icon.addFile(u":/logo/img/lockdown.png", QSize(), QIcon.Normal,
                     QIcon.Off)
        install_menu.setWindowIcon(icon)
        install_menu.setStyleSheet(
            u"background-image: url(:/background/img/blurred_background.jpg);")
        self.centralwidget = QWidget(install_menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.instalar = QPushButton(self.centralwidget)
        self.instalar.setObjectName(u"instalar")
        self.instalar.setGeometry(QRect(20, 10, 340, 41))
        self.instalar.setStyleSheet(u"background-color: transparent;\n"
                                    "border: 1px solid white;\n"
                                    "border-radius: 10px;color:whitesmoke;")
        self.backup = QPushButton(self.centralwidget)
        self.backup.setObjectName(u"backup")
        self.backup.setGeometry(QRect(20, 60, 340, 41))
        self.backup.setStyleSheet(u"background-color: transparent;\n"
                                  "border: 1px solid white;\n"
                                  "border-radius: 10px;color:whitesmoke;")
        install_menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(install_menu)

        QMetaObject.connectSlotsByName(install_menu)

    # setupUi

    def retranslateUi(self, install_menu):
        install_menu.setWindowTitle(
            QCoreApplication.translate("install_menu", u"Instalaci\u00f3n",
                                       None))
        self.instalar.setText(
            QCoreApplication.translate("install_menu", u"INSTALAR", None))
        self.backup.setText(
            QCoreApplication.translate("install_menu", u"RESTAURAR BACKUP",
                                       None))

    # retranslateUi
