# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'run_install.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recursos


class Ui_popup_window(object):
    def setupUi(self, popup_window):
        if not popup_window.objectName():
            popup_window.setObjectName(u"popup_window")
        popup_window.resize(372, 117)
        icon = QIcon()
        icon.addFile(u":/logo/img/lockdown.png", QSize(), QIcon.Normal,
                     QIcon.Off)
        popup_window.setWindowIcon(icon)
        popup_window.setStyleSheet(
            u"background-image: url(:/background/img/blurred_background.jpg);")
        self.centralwidget = QWidget(popup_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 371, 21))
        self.label.setStyleSheet(u"color:whitesmoke;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 40, 371, 31))
        self.label_2.setStyleSheet(u"color:whitesmoke;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.ok = QPushButton(self.centralwidget)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(10, 80, 350, 30))
        self.ok.setStyleSheet(u"")
        popup_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(popup_window)

        QMetaObject.connectSlotsByName(popup_window)

    # setupUi

    def retranslateUi(self, popup_window):
        popup_window.setWindowTitle(
            QCoreApplication.translate("popup_window", u"Instalame !", None))
        self.label.setText(
            QCoreApplication.translate(
                "popup_window", u"NO SE ENCONTR\u00d3 UNA BASE DE DATOS !",
                None))
        self.label_2.setText(
            QCoreApplication.translate(
                "popup_window",
                u"Por favor, asegurate de instalar la base de datos ", None))
        self.ok.setText(QCoreApplication.translate("popup_window", u"OK",
                                                   None))
        #if QT_CONFIG(shortcut)
        self.ok.setShortcut(
            QCoreApplication.translate("popup_window", u"Return", None))


#endif // QT_CONFIG(shortcut)
# retranslateUi
