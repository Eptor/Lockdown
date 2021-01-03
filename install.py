# Modulos vanila
import sqlite3
from time import sleep
from getpass import getpass
from os import system, path
import sys

# Modulos locales
from modules.crypto import mnemotecnica, encrypt, decrypt_bkp
from windows.add_user import Ui_add_user
from windows.install_menu import Ui_install_menu

# Modulos externos (pip install)
from colorama import init, Fore
import pyperclip
from PySide2.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QInputDialog, QFileDialog, QListWidgetItem)


class add_user_class(QMainWindow, Ui_add_user):
    """ Ventana de login """
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        QMessageBox.warning(
            self, "IMPORTANTE",
            "La clave mnemotécnica servirá para recuperar tu cuenta en caso de que olvides tu contraseña, por lo que es de suma importancia que NO LA PIERDAS"
        )
        self.key_gen = mnemotecnica()
        self.clave.setText(self.key_gen)

        self.aceptar.clicked.connect(self.add_action)
        self.cancelar.clicked.connect(lambda: self.close())

    def add_action(self):
        if self.password.text() == self.password_2.text():
            system("mkdir database && fsutil file createnew data.sqlite 0")
            conn = sqlite3.connect("database/data.sqlite")
            cursor = conn.cursor()
            usuario = self.nombre.text()
            passwd = self.password.text()
            key = self.clave.text()

            # Tabla usuarios
            cursor.execute("""
                CREATE TABLE "users" (
                "user"	TEXT NOT NULL UNIQUE,
                "password"	TEXT NOT NULL,
                "backup" TEXT
            )
            """)

            # Tabla de almacenamiento
            cursor.execute("""
            CREATE TABLE "data" (
                "Nombre" TEXT NOT NULL,
                "Email" TEXT,
                "Contraseña" TEXT NOT NULL,
                "Link" TEXT
            )
            """)

            try:
                cursor.execute(
                    f"INSERT INTO users VALUES ('{usuario}', '{encrypt(passwd, passwd)}', '{encrypt(passwd, key)}')"
                )
                pyperclip.copy(self.key_gen)
            except Exception as e:
                QMessageBox.warning(self, "Error",
                                    f"Ocurrió el siguiente error:\n{e}")
            else:
                conn.commit()
                QMessageBox.information(
                    self, "Finalizado",
                    "La instalación se completó con exito\nTu clave mnemotécnica se copió a tu portapapeles, guardala en un lugar seguro"
                )
        else:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden")


class menu_class(QMainWindow, Ui_install_menu):
    """ Ventana de login """
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.instalar.clicked.connect(self.instalar_window)
        self.backup.clicked.connect(self.open_backup)

    def existe(self):
        """ Verificar si ya existe una instalación """
        if path.isfile("database/data.sqlite"):
            QMessageBox.information(
                self, "Atención",
                "Ya existe una instalación de la base de datos")
            sys.exit()

    def instalar_window(self):
        self.ventana = add_user_class()
        self.ventana.show()
        self.close()

    def open_backup(self):
        path = QFileDialog.getOpenFileName(self, "Archivo lockdown", None,
                                           "Lockdown (*.lockdown)")[0]

        clave, ok = QInputDialog.getText(
            self,
            "Clave",
            "Introuce la contraseña con la que se encriptó este backup",
        )
        if ok:
            with open(
                    path, "rb"
            ) as data_read:  # Leer bytes del archivo para desencriptado
                data = decrypt_bkp(
                    data_read.read(),
                    clave,
                )

            # Sobre-escribir la base de datos actual con la nueva
            with open("database/data.sqlite", "wb") as data_write:
                data_write.write(data)
            QMessageBox.information(self, "Completado",
                                    "La restauración se completó con exito")
            sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("style.css").read())
    menu = menu_class()
    menu.existe()
    menu.show()
    sys.exit(app.exec_())
