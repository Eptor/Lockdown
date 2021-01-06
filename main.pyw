# Modulos locales
from modules.crypto import encrypt, decrypt, decrypt_bkp, generador

# Ventanas
from windows.login import Ui_login_window
from windows.menu import Ui_menu_window
from windows.datos_popup import Ui_data_popup
from windows.add_data import Ui_add_data
from windows.run_install import Ui_popup_window

# Modulos vanila
import os
from time import sleep
from getpass import getpass
import sys
from webbrowser import open as webopen

# Modulos externos (pip install)
import pyperclip
from PySide2.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QInputDialog, QFileDialog, QListWidgetItem)
from PySide2.QtCore import Qt


class login_window_class(QMainWindow, Ui_login_window):
    """ Ventana de login """
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.login.clicked.connect(self.verify)
        self.actionOlvid_mi_contrase_a.triggered.connect(self.recovery_popup)
        self.actionRestaurar_base_de_datos.triggered.connect(self.backup_popup)

    def verify(self):
        global key

        user = self.user_input.text()
        key = self.password_input.text()
        try:
            if key == decrypt(get_user_data(user), key):
                self.menu = menu_window_class()
                self.menu.show()
                self.close()
        except Exception as e:
            QMessageBox.warning(self, "Advertencia",
                                f"Ocurrió el siguiente error:\n{e}")

    def recovery_popup(self):
        user = self.user_input.text()
        if user != "":
            clave, ok = QInputDialog.getText(
                self,
                "Clave",
                "Introuce tu clave mnemotécnica",
            )

            if ok:
                QMessageBox.information(
                    self, "Recovery",
                    f"Tu contraseña es: {decrypt(recovery(user), clave)}")
        else:
            QMessageBox.warning(self, "Error", "Primero introduce tu usuario")

    def backup_popup(self):
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


class add_data_class(QMainWindow, Ui_add_data):
    def __init__(self, mode, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        if not mode[0]:
            self.aceptar.clicked.connect(self.add)
        elif mode[0]:
            self.registro = mode[1]
            QMessageBox.information(
                self, "Atención",
                "Deja en blanco los campos que no deseas editar")
            self.label.setText("Nombre del registro a editar")
            self.nombre.setText(self.registro)
            self.nombre.setReadOnly(True)
            self.aceptar.clicked.connect(self.edit)

        self.cancelar.clicked.connect(lambda: self.close())

    def add(self):
        try:
            insert_data(self.nombre.text(), encrypt(self.email.text(), key),
                        encrypt(self.password.text(), key), self.link.text())
        except Exception as e:
            QMessageBox.warning(self, "Error",
                                f"Ocurrio el siguiente error:\n{e}")
        else:
            QMessageBox.information(
                self, "Completado",
                f"{self.nombre.text()} se ha añadido\nRefresca la tabla con el icono superior"
            )
            self.close()

    def edit(self):
        try:
            data = get_password_data(self.registro)
        except IndexError:
            QMessageBox.warning(self, "Error",
                                "No existen registros con ese nombre")
        else:
            if self.nombre.text() == "":
                nombre = data[0]
            else:
                nombre = self.nombre.text()

            if self.email.text() == "":
                email = data[1]
            else:
                email = encrypt(self.email.text(), key)

            if self.password.text() == "":
                contraseña = data[2]
            else:
                contraseña = encrypt(self.password.text(), key)

            if self.link.text() == "":
                link = data[3]
            else:
                link = self.link.text()

            try:
                edit_data(nombre, email, contraseña, link, self.registro)
            except Exception as e:
                QMessageBox.warning(self, "Error",
                                    f"Ocurrió el siguiente error:\n{e}")
            else:
                QMessageBox.information(
                    self, "Completado",
                    f"{self.registro} se editó correctamente")
                self.close()


class datos_popup_class(QMainWindow, Ui_data_popup):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.show_data()

        self.ok.clicked.connect(lambda: self.close())
        self.copiar_c.clicked.connect(self.copiar_contraseña)
        self.abrir_l.clicked.connect(self.abrir_link)

    def copiar_contraseña(self):
        self.dinamica.setText("Contraseña copiada!")
        pyperclip.copy(decrypt(data[2], key))

    def abrir_link(self):
        self.dinamica.setText("Link abierto!")
        webopen(data[3], new=2)
        pyperclip.copy(data[3])

    def show_data(self):
        self.nombre.setText(f"Nombre: {data[0]}")
        self.email.setText(f"Correo: {decrypt(data[1], key)}")
        self.password.setText(f"Contraseña: {decrypt(data[2], key)}")
        self.link.setText(f"Link: {data[3]}")


class menu_window_class(QMainWindow, Ui_menu_window):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.gen_tipo = None
        self.update()

        self.tipo.stateChanged.connect(self.update_tipo)
        self.generar.clicked.connect(self.generar_password)
        self.copiar.clicked.connect(self.copiar_gen)
        self.add.clicked.connect(self.añadir_registro)
        self.ver.clicked.connect(self.ver_registro)
        self.editar.clicked.connect(self.editar_registro)
        self.eliminar.clicked.connect(self.eliminar_registro)
        self.respaldo.clicked.connect(self.generar_backup)
        self.refresh.clicked.connect(self.update)

    def update(self):
        self.listWidget.clear()
        self.listWidget.addItem("")
        for x in get_user_passwords():
            y = QListWidgetItem(x[0])
            y.setTextAlignment(Qt.AlignHCenter)
            self.listWidget.addItem(y)

        self.listWidget.addItem("")

    def copiar_gen(self):
        pyperclip.copy(self.gen_text.text())
        self.gen_text.setText("Contraseña copiada!")

    def update_tipo(self, state):
        self.gen_tipo = state

    def generar_password(self):
        self.gen_text.clear()
        if Qt.Checked == self.gen_tipo:
            temp = generador(1)
        else:
            temp = generador(2)
        self.gen_text.setText(temp)
        del temp

    def ver_registro(self):
        global data
        data = get_password_data(str(self.listWidget.currentItem().text()))
        self.popup = datos_popup_class()
        self.popup.show()

    def añadir_registro(self):
        self.popup_data = add_data_class(mode=[False])
        if self.popup_data.show():
            print("True")
            self.popup.close()
            self.update()

    def editar_registro(self):
        # Verificación
        if str(self.listWidget.currentItem().text()) != "":
            self.popup_edit = add_data_class(
                mode=[True, str(self.listWidget.currentItem().text())])
            self.popup_edit.show()
        else:
            pass

    def eliminar_registro(self):
        registro = str(self.listWidget.currentItem().text())
        try:
            delete_data(registro)
        except Exception as e:
            QMessageBox.warning(self, "Error",
                                f"Ocurrió el siguiente error:\n{e}")
        else:
            QMessageBox.information(
                self, "Compeltado",
                f"{registro} se eliminó de la base de datos")

            self.update()

    def generar_backup(self):
        # Leer los bytes del archivo para encriptarlos
        with open("database/data.sqlite", "rb") as data_read:
            data = encrypt(data_read.read(), key)

        # Escribe los bytes encriptados en un nuevo archivo
        with open("database/data_backup.lockdown", "wb") as data_write:
            data_write.write(data.encode())

        QMessageBox.information(
            self, "Completado",
            "El respaldo se generó con exito en:\ndatbase/data_backup.lockdown"
        )


class popup_class(QMainWindow, Ui_popup_window):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.ok.clicked.connect(lambda: self.close())


if __name__ == "__main__":
    if os.path.isfile("database/data.sqlite"):
        from modules.data_handler import (
            get_user_data,
            get_user_passwords,
            insert_data,
            get_password_data,
            delete_data,
            recovery,
            edit_data,
        )  # Evita que se cree la base de datos antes de instalar

        app = QApplication(sys.argv)
        app.setStyleSheet(open("style.css").read())

        login = login_window_class()
        login.show()
        sys.exit(app.exec_())
    else:
        app = QApplication(sys.argv)
        app.setStyleSheet(open("style.css").read())

        popup = popup_class()
        popup.show()
        sys.exit(app.exec_())
