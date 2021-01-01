#! D:\Programacion\Lockdown\venv\Scripts\python
#!!! Este ^^ es mi ambiente virtual, eres libre de eliminar estas lineas.

# Modulos locales
from modules.crypto import encrypt, decrypt, decrypt_bkp, generador
from modules.install import install

# Ventanas
from windows.login import Ui_login_window
from windows.menu import Ui_menu_window
from windows.datos_popup import Ui_data_popup
from windows.add_data import Ui_add_data

# Modulos vanila
import os
from time import sleep
from getpass import getpass
import sys

# Modulos externos (pip install)
import pyperclip
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QInputDialog,
    QFileDialog,
    QListWidgetItem
)
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
            QMessageBox.warning(
                self, "Advertencia", f"Ocurrió el siguiente error:\n{e}"
            )

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
                    self, "Recovery", f"Tu contraseña es: {decrypt(recovery(user), clave)}")
        else:
            QMessageBox.warning(self, "Error", "Primero introduce tu usuario")

    def backup_popup(self):
        path = QFileDialog.getOpenFileName(
            self, "Archivo lockdown", None, "Lockdown (*.lockdown)"
        )[0]

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


class add_data_class(QMainWindow, Ui_add_data):
    def __init__(self, mode, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        if mode == 1:
            self.aceptar.clicked.connect(self.add)
        elif mode == 2:
            QMessageBox.information(
                self, "Atención", "Deja en blanco los campos que no deseas editar")
            self.label.setText("Nombre del registro a editar")
            self.aceptar.clicked.connect(self.edit)

        self.cancelar.clicked.connect(lambda: self.close())

    def add(self):
        try:
            insert_data(self.nombre.text(), encrypt(self.email.text(), key), encrypt(
                self.password.text(), key), self.link.text())
        except Exception as e:
            QMessageBox.warning(
                self, "Error", f"Ocurrio el siguiente error:\n{e}")
        else:
            QMessageBox.information(
                self, "Completado", f"{self.nombre.text()} se ha añadido")

        menu_window_class().update()

    def edit(self):
        registro = self.nombre.text()
        try:
            data = get_password_data(registro)
        except IndexError:
            QMessageBox.warning(
                self, "Error", "No existen registros con ese nombre")
        else:
            if self.nombre.text() == "":
                nombre = data[0]
            else:
                nombre = self.nombre.text()

            if self.email.text() == "":
                email = data[1]
            else:
                email = encrypt(self.email.text(), key)

            if self.password == "":
                contraseña = data[2]
            else:
                contraseña = encrypt(self.password.text(), key)

            if self.link.text() == "":
                link = data[3]
            else:
                link = self.link.text()

            try:
                edit_data(nombre, email, contraseña, link, registro)
            except Exception as e:
                QMessageBox.warning(
                    self, "Error", f"Ocurrió el siguiente error:\n{e}")
            else:
                QMessageBox.information(
                    self, "Completado", f"{registro} se editó correctamente")
                self.close()


class datos_popup_class(QMainWindow, Ui_data_popup):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.show_data()

        self.ok.clicked.connect(lambda: self.close())
        self.copiar_c.clicked.connect(self.copiar_contraseña)
        self.copiar_l.clicked.connect(self.copiar_link)

    def copiar_contraseña(self):
        self.dinamica.setText("Contraseña copiada!")
        pyperclip.copy(decrypt(data[2], key))

    def copiar_link(self):
        self.dinamica.setText("Link copiado!")
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
        self.popup_data = add_data_class(mode=1)
        self.popup_data.show()

    def editar_registro(self):
        self.popup_edit = add_data_class(mode=2)
        self.popup_edit.show()

    def eliminar_registro(self):
        registro = str(self.listWidget.currentItem().text())
        try:
            delete_data(registro)
        except Exception as e:
            QMessageBox.warning(
                self, "Error", f"Ocurrió el siguiente error:\n{e}")
        else:
            QMessageBox.information(self, "Compeltado",
                                    f"{registro} se eliminó de la base de datos")

            self.update()


def main():
    # Login
    while True:
        os.system("cls")
        try:
            user = input("Usuario: ")
            key = getpass("Contraseña: ")

            if user == "help" and key == "":  # Recuperar contraseña
                user = input("Introduce tu usuario: ")
                mn = input("> Introduce tu clave mnemotécnica:\n> ")
                os.system("cls")
                print(
                    Fore.YELLOW
                    + f"Tu contraseña es: {decrypt(recovery(user), mn)}"
                )
                input("Presiona enter para continuar")

            elif user == "backup" and key == "":  # Usar nueva base de datos

                print(Fore.YELLOW + "Espera mientras leemos el archivo")

                with open(
                    "database/data_backup.lockdown", "rb"
                ) as data_read:  # Leer bytes del archivo para desencriptado
                    data = decrypt_bkp(
                        data_read.read(),
                        input("Clave con la que se creó el backup\n> "),
                    )

                with open(
                    "database/data.sqlite", "wb"
                ) as data_write:  # Sobre-escribir la base de datos actual con la nueva
                    data_write.write(data)

                print(Fore.CYAN + "Base de datos restaurada")
                sleep(2)

            elif key == decrypt(get_user_data(user), key):  # Login exitoso
                print(Fore.GREEN + "\nLogin exitoso")
                sleep(1)
                print(Fore.CYAN + "Bienvenido a Lockdown")
                sleep(1)
                break

            else:
                continue

        except Exception:
            print(Fore.RED + "\nDatos erroneos.")
            sleep(1)

    # Main loop
    try:
        while True:
            menu()
            om = input("> ")
            if om == "1":  # Ver datos
                table = PrettyTable()  # Creacion de la tabla
                os.system("cls")
                try:
                    data = get_password_data(
                        input("Nombre: ")
                    )  # Obtencion de datos
                except IndexError:
                    print(Fore.RED + "\nNo existen registros con ese nombre !")
                    sleep(2)

                except:
                    print(
                        Fore.RED
                        + "La contraseña con la que se encriptaron los datos es otra."
                    )

                else:
                    table.field_names = [
                        "Nombre",
                        "Email",
                        "Contraseña",
                        "Link",
                    ]
                    table.add_row(
                        [
                            data[0],
                            decrypt(data[1], key),
                            decrypt(data[2], key),
                            data[3],
                        ]
                    )
                    print()
                    try:
                        print(table)
                        input(
                            "\nPresiona ENTER para regresar al menu\nPresiona CTRL + C para copiar la contraseña"
                        )
                    except KeyboardInterrupt:
                        pyperclip.copy(decrypt(data[2], key))
                        print(
                            Fore.MAGENTA
                            + "\nContraseña copiada al portapapeles !"
                        )
                        sleep(1)
                    else:
                        del table

            elif om == "2":
                os.system("cls")
                try:
                    insert_data(key)  # Añadir registro
                except Exception as e:
                    print(Fore.RED + "Error al añadir")
                    print(e)
                else:
                    print(Fore.GREEN + "\nAñadido con exito.")
                sleep(2)

            elif om == "3":
                os.system("cls")
                if delete_data():  # Elimianr registro
                    print(Fore.GREEN + "\nEliminado con exito.")
                    sleep(2)

                else:
                    print(Fore.RED + "\nNo ha sido eliminado.")
                    sleep(2)

            elif om == "4":
                os.system("cls")
                cambiar = input("Editar: ")  # Cambiar datos de registro

                if cambiar != "":
                    if edit_data(cambiar, key):
                        print(Fore.GREEN + "\nEditado con exito!")
                        sleep(2)

                    else:
                        print(Fore.RED + "\nNo fue editado.")
                        sleep(2)
                else:
                    print(Fore.YELLOW + "Volviendo al menu.")
                    sleep(1)

            elif om == "5":  # Generador de contraseñas
                os.system("cls")
                print(Fore.YELLOW + "Vamos a generarte una contraseña nueva !")
                sleep(1)
                tipo = int(input("1) - Con simbolos\n2) - Sin simbolos\n> "))
                try:
                    longitud = int(input("Longitud (12 - default)\n> "))
                except ValueError:
                    print(Fore.YELLOW + "Usando 12 como valor.")
                    sleep(0.5)
                    longitud = 12
                password = generador(tipo, longitud)
                if password is not False:
                    print("\nTu contraseña es:", Fore.MAGENTA + password)
                    sleep(1)
                    pyperclip.copy(password)
                    print(Fore.CYAN + "\nLa copiamos a tu portapapeles !")
                    sleep(2)
                else:
                    print("\nLa opcion introducida no es correcta.")
                    sleep(1)

            elif om.lower() == "bkp":  # Respaldo
                os.system("cls")
                print(Fore.YELLOW + "Espera a que realicemos el backup")

                sleep(1)

                with open(
                    "database/data.sqlite", "rb"
                ) as data_read:  # Leer los bytes del archivo para encriptarlos
                    data = encrypt(
                        data_read.read(),
                        key,
                    )

                with open(
                    "database/data_backup.lockdown", "wb"
                ) as data_write:  # Escribe los bytes encriptados en un nuevo archivo
                    data_write.write(data.encode())

                print("\nCompletado.")
                print(Fore.RED + "\nEl backup se encriptó con tu contraseña.")
                sleep(3)

            else:
                pass

    except KeyboardInterrupt:
        os.system("cls")
        print(Fore.CYAN + "Gracias por usar Lockdown!")
        sleep(1)
        print("\nSaliendo.")
        sleep(1)

    except Exception as e:
        os.system("cls")
        print(Fore.RED + "Ocurrio un error inesperado!")
        sleep(1)
        print(
            "Por favor abre un issue en nuestro repositorio de Github",
            Fore.CYAN + "(https://github.com/Eptor/Lockdown)",
        )
        sleep(1)
        print("\nEl error es:")
        print("\n\n", e)


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
        print("No se ha encontrado una base de datos!")
        print(Fore.CYAN + "Empezando la instalación")
        os.system("cls")
        install()
