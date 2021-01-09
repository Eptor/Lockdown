# Modulos locales
from modules.crypto import encrypt, decrypt, decrypt_bkp, generador

# Ventanas
from windows.login import Ui_login_window
from windows.menu import Ui_menu_window
from windows.datos_popup import Ui_data_popup
from windows.add_data import Ui_add_data
from windows.run_install import Ui_popup_window
from windows.enc_files import Ui_encrypt_menu
from windows.dec_files import Ui_decrypt_menu

# Modulos vanila
import os
from time import sleep
from getpass import getpass
import sys
from webbrowser import open as webopen
from string import ascii_letters
from os import system, path
from pathlib import Path
from datetime import date
from zipfile import ZipFile, ZIP_DEFLATED

# Modulos externos (pip install)
import pyperclip
from PySide2.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QInputDialog, QFileDialog, QListWidgetItem)
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon

morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'Ñ': '--.--',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": ".----.",
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-....',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    '¿': '..-.-',
    '¡': '--...-'
}


class login_window_class(QMainWindow, Ui_login_window):
    """ Ventana de login """
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.login.clicked.connect(self.verify)
        self.actionOlvid_mi_contrase_a.triggered.connect(self.recovery_popup)
        self.actionRestaurar_base_de_datos.triggered.connect(self.backup_popup)

    def verify(self):
        global key  # Se define como global para usarla en todo el programa

        user = self.user_input.text()
        key = self.password_input.text()
        # Verificar las credenciales
        try:
            if key == decrypt(get_user_data(user), key):
                self.menu = menu_window_class()
                self.menu.show()
                self.close()
        except Exception as e:
            QMessageBox.warning(self, "Advertencia",
                                f"Las credenciales no coinciden ")
            print(e)

    def recovery_popup(self):
        """ Popup para solicitar la clave mnemotécnica """
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
        """ Solicita el archivo del backup """
        path = QFileDialog.getOpenFileName(self, "Archivo lockdown", None,
                                           "Lockdown (*.lockdown)")[0]

        clave, ok = QInputDialog.getText(
            self,
            "Clave",
            "Introuce la contraseña con la que se encriptó este backup",
        )  # Solicita la contraseña del usuario
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

        # Verifica los datos enviados desde el menú
        if not mode[0]:
            self.aceptar.clicked.connect(self.add)
        elif mode[0]:
            # Setea la variable con el nombre de la contraseña seleccionada
            self.registro = mode[1]
            # Aviso
            QMessageBox.information(
                self, "Atención",
                "Deja en blanco los campos que no deseas editar")

            # Setea los campos necesarios y conecta el botón
            self.label.setText("Nombre del registro a editar")
            self.nombre.setText(self.registro)
            self.nombre.setReadOnly(True)
            self.aceptar.clicked.connect(self.edit)

        self.cancelar.clicked.connect(lambda: self.close())

    def add(self):
        # Intenta insertar los datos nuevos ingresados por el usuario
        try:
            insert_data(self.nombre.text(), encrypt(self.email.text(), key),
                        encrypt(self.password.text(), key), self.link.text())
        except Exception as e:
            QMessageBox.warning(self, "Error",
                                f"Ocurrio el siguiente error:\n{e}")
        else:
            QMessageBox.information(
                self, "Completado",
                f"{self.nombre.text()} se ha añadido\n¡Refresca la tabla con el icono superior!"
            )
            self.close()

    def edit(self):
        try:
            data = get_password_data(self.registro)
        except IndexError:
            QMessageBox.warning(self, "Error",
                                "No existen registros con ese nombre")
        else:
            # Verifica si algun campo se dejó en blanco para dejarlo tal y como está
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
                # Intenta editar los datos con los campos rellenados
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
    """ Popup con los datos del registro """
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
        self.down_icon = QIcon()
        self.down_icon.addFile(u":/drop/img/drop.png", QSize(), QIcon.Normal,
                               QIcon.Off)
        self.up_icon = QIcon()
        self.up_icon.addFile(u":/drop/img/arrows-57.png", QSize(),
                             QIcon.Normal, QIcon.Off)

        self.tipo.stateChanged.connect(self.update_tipo)
        self.generar.clicked.connect(self.generar_password)
        self.copiar.clicked.connect(self.copiar_gen)
        self.add.clicked.connect(self.añadir_registro)
        self.ver.clicked.connect(self.ver_registro)
        self.editar.clicked.connect(self.editar_registro)
        self.eliminar.clicked.connect(self.eliminar_registro)
        self.respaldo.clicked.connect(self.generar_backup)
        self.refresh.clicked.connect(self.update)
        self.drop_button.clicked.connect(self.ver_abajo)
        self.convertir.clicked.connect(self.traducir_morse)
        self.copiar_morse.clicked.connect(self.morse_copiar)
        self.esconder_img.clicked.connect(self.show_enc_file)
        self.revelar_img.clicked.connect(self.show_rev_file)

    def update(self):
        """ actualiza los items en la lista """
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
        self.gen_tipo = state  # True / False

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
        # data = texto seleccionado en la lista
        data = get_password_data(str(self.listWidget.currentItem().text()))
        self.popup = datos_popup_class()
        self.popup.show()

    def añadir_registro(self):
        # Se setea en false para abrir el popup de añadir
        self.popup_data = add_data_class(mode=[False])
        if self.popup_data.show():
            self.popup.close()
            self.update()

    def editar_registro(self):
        # Si no hay nada seleccionado aplica un pass
        if str(self.listWidget.currentItem().text()) != "":
            # Se setea en False para abrir el popup de editar y se pasa el texto seleccionado
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

    def ver_abajo(self):
        """ Si la altura de la ventana es la predeterminada se baja para enseñar la seccion oculta """
        if self.height() == 407:
            self.setFixedHeight(641)
            self.drop_button.setIcon(self.up_icon)
            self.drop_button.setIconSize(QSize(30, 30))

        else:
            self.setFixedHeight(407)
            self.drop_button.setIcon(self.down_icon)
            self.drop_button.setIconSize(QSize(30, 30))

    def get_key(self, val):
        """ Regresa la llave del diccionario correspondiente al valor """
        for key, value in morse.items():
            if val == value:
                return key

        return f"La llave de {val} no existe"

    def traducir_morse(self):
        """ Traduce del abecedario a morse y viceversa """
        resultado = []

        if any(item in [x for x in ascii_letters]
               for item in [x for x in self.morse_input.toPlainText()]
               ):  # Si existe una letra en el input se traduce a morse
            palabras = self.morse_input.toPlainText().upper().split()
            for palabra in palabras:
                for letra in palabra:
                    resultado.append(morse[letra])
                    resultado.append(" ")

                # Se agregan espacios y el signo de espacio en clave morse
                resultado.append("/")
                resultado.append(" ")

            self.morse_input.setText("")
            # Se muestra el resultado ignorando el espacio del final
            self.morse_output.setText("".join(resultado[:-1]))

        # Si no se encuentra ninguna letra en el input se traduce al español
        else:
            # Se separa por espacios
            letras = self.morse_input.toPlainText().split(" ")
            # iteración sobre las letras en morse
            for letra in letras:
                resultado.append(
                    self.get_key(letra)
                )  # Se agrega la llave correspondiente al valor en morse

            resultado_ascii = "".join(resultado)  # Se crea el resultado
            self.morse_input.setText("")  # Se limpia el input
            self.morse_output.setText(resultado_ascii.capitalize(
            ))  # Se muestra el resultado empezando por mayuscula

    def morse_copiar(self):
        pyperclip.copy(self.morse_output.toPlainText())
        self.morse_output.setText("Se copió el resultado !")

    def show_enc_file(self):
        self.enc = esconder_archivos()
        self.enc.show()

    def show_rev_file(self):
        self.rev = revelar_archivos()
        self.rev.show()


class esconder_archivos(QMainWindow, Ui_encrypt_menu):
    """ Esconde los archivos en una imagen """
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.file_paths = []
        self.filenames = []
        self.search_folder.clicked.connect(self.mostrar_archivos)
        self.search_image.clicked.connect(self.obtener_original)
        self.search_location.clicked.connect(self.obtener_destino)
        self.start.clicked.connect(self.zipall)

    def archivos_en_dir(self):
        """ Regresa una lista con los archivos en el directorio seleccionado """
        directory = QFileDialog.getExistingDirectory(self,
                                                     "Selecciona la carpeta")

        for root, _, files in os.walk(directory):
            for filename in files:
                # Une las dos strings para conseguir el path complet
                filepath = os.path.join(root, filename)
                self.filenames.append(filename)
                self.file_paths.append(filepath)

    def mostrar_archivos(self):
        self.archivos_en_dir()
        for x in self.filenames:
            self.files_list.addItem(x)

    def obtener_original(self):
        """ Obtiene el path de la foto que será utilizada para esconder los archivos """
        self.pic = QFileDialog.getOpenFileName(self, "Selecciona la imagen")[0]
        self.original_img.setText(self.pic)

    def obtener_destino(self):
        """ Obtiene el directorio donde se guardará el archivo con los secretos dentro """
        self.directory = str(
            QFileDialog.getExistingDirectory(self, "Selecciona un directorio"))
        self.new_location.setText(self.directory)

    def zipall(self):
        """ Genera un zip con los archivos seleccionados """
        # Fecha actual
        today = f"{date.today().strftime('%d')}_{date.today().strftime('%m')}_{date.today().strftime('%y')}"

        self.new_pic_location = Path(
            f"{self.new_location.text()}/{self.new_name.text()}.jpg")
        self.zip_name = Path(f"{self.new_location.text()}/{today}.zip")

        # Escribiendo el zip
        print(self.new_pic_location, self.zip_name)
        with ZipFile(self.zip_name, "w", ZIP_DEFLATED) as zip:
            for file in self.file_paths:
                zip.write(file, arcname=f"Hidden/{os.path.basename(file)}")

        QMessageBox.information(
            self, "Atencion",
            "Espera mientras se esconden tu archivos\nEs posible que la ventana se congele durante el proceso"
        )

        os.system(
            f'copy /b "{Path(self.pic)}" + {self.zip_name} "{self.new_pic_location}" && del {self.zip_name}'
        )

        self.file_paths.clear()


class revelar_archivos(QMainWindow, Ui_decrypt_menu):
    """ Revela los archivos escondidos por Hides """
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.unzip_file_search.clicked.connect(self.file)
        self.output_dir_search.clicked.connect(self.get_output)
        self.start.clicked.connect(self.reveal)

    def file(self):
        self.pic = QFileDialog.getOpenFileName(self, "Selecciona la imagen")[0]

        self.unzip_file.setText(self.pic)

    def get_output(self):
        self.output = str(
            QFileDialog.getExistingDirectory(self, "Selecciona un directorio"))

        self.output_dir.setText(self.output)

    def unzip(self, path, file):
        with ZipFile(file, "r") as zip:
            zip.extractall(path=Path(f"{path}"))

    def reveal(self):
        try:
            QMessageBox.information(
                self, "Atencion",
                "Espera mientras se revelan tu archivos\nEs posible que la ventana se congele durante el proceso"
            )

            self.unzip(
                self.output,
                self.pic,
            )

        except Exception as e:
            QMessageBox.warning(self, "Error", f"El proceso falló\error:{e}")
        else:
            QMessageBox.information(self, "Completado",
                                    "Archivos revelados satisfactoriamente.")


class popup_class(QMainWindow, Ui_popup_window):
    """ Aviso de instalación """
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.ok.clicked.connect(lambda: self.close())


if __name__ == "__main__":
    # Si existe una base de datos se inicia el programa
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

    # Si no existe una base de datos se enseña el popup de aviso
    else:
        app = QApplication(sys.argv)
        app.setStyleSheet(open("style.css").read())

        popup = popup_class()
        popup.show()
        sys.exit(app.exec_())
