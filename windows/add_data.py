# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_data.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recursos

class Ui_add_data(object):
    def setupUi(self, add_data):
        if not add_data.objectName():
            add_data.setObjectName(u"add_data")
        add_data.resize(402, 299)
        icon = QIcon()
        icon.addFile(u":/logo/img/lockdown.png", QSize(), QIcon.Normal, QIcon.Off)
        add_data.setWindowIcon(icon)
        self.horizontalLayoutWidget = QWidget(add_data)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 260, 380, 30))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.aceptar = QPushButton(self.horizontalLayoutWidget)
        self.aceptar.setObjectName(u"aceptar")

        self.horizontalLayout.addWidget(self.aceptar)

        self.cancelar = QPushButton(self.horizontalLayoutWidget)
        self.cancelar.setObjectName(u"cancelar")

        self.horizontalLayout.addWidget(self.cancelar)

        self.nombre = QLineEdit(add_data)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(10, 40, 381, 30))
        self.nombre.setStyleSheet(u"background-color: transparent;\n"
"border: 1px solid white;\n"
"border-radius: 10px;color:whitesmoke;")
        self.nombre.setAlignment(Qt.AlignCenter)
        self.email = QLineEdit(add_data)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(10, 100, 381, 30))
        self.email.setStyleSheet(u"background-color: transparent;\n"
"border: 1px solid white;\n"
"border-radius: 10px;color:whitesmoke;")
        self.email.setAlignment(Qt.AlignCenter)
        self.password = QLineEdit(add_data)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(10, 160, 381, 30))
        self.password.setStyleSheet(u"background-color: transparent;\n"
"border: 1px solid white;\n"
"border-radius: 10px;color:whitesmoke;")
        self.password.setAlignment(Qt.AlignCenter)
        self.link = QLineEdit(add_data)
        self.link.setObjectName(u"link")
        self.link.setGeometry(QRect(10, 220, 381, 30))
        self.link.setStyleSheet(u"background-color: transparent;\n"
"border: 1px solid white;\n"
"border-radius: 10px;color:whitesmoke;")
        self.link.setAlignment(Qt.AlignCenter)
        self.label = QLabel(add_data)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 380, 16))
        self.label.setStyleSheet(u"color: whitesmoke;")
        self.label_2 = QLabel(add_data)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 380, 16))
        self.label_2.setStyleSheet(u"color: whitesmoke;")
        self.label_3 = QLabel(add_data)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 140, 70, 16))
        self.label_3.setStyleSheet(u"color: whitesmoke;")
        self.label_4 = QLabel(add_data)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 200, 70, 16))
        self.label_4.setStyleSheet(u"color: whitesmoke;")
        self.label_5 = QLabel(add_data)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 401, 301))
        self.label_5.setStyleSheet(u"background-image: url(:/background/img/blurred_background.jpg);")
        self.label_5.raise_()
        self.horizontalLayoutWidget.raise_()
        self.nombre.raise_()
        self.email.raise_()
        self.password.raise_()
        self.link.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(add_data)

        QMetaObject.connectSlotsByName(add_data)
    # setupUi

    def retranslateUi(self, add_data):
        add_data.setWindowTitle(QCoreApplication.translate("add_data", u"A\u00f1adir", None))
        self.aceptar.setText(QCoreApplication.translate("add_data", u"OK", None))
#if QT_CONFIG(shortcut)
        self.aceptar.setShortcut(QCoreApplication.translate("add_data", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.cancelar.setText(QCoreApplication.translate("add_data", u"Cancelar", None))
        self.label.setText(QCoreApplication.translate("add_data", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("add_data", u"Email", None))
        self.label_3.setText(QCoreApplication.translate("add_data", u"Contrase\u00f1a", None))
        self.label_4.setText(QCoreApplication.translate("add_data", u"Link", None))
        self.label_5.setText("")
    # retranslateUi

