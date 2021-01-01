# Modulos locales
from modules.crypto import encrypt, decrypt

# Modulos externos (pip install)
import sqlite3
from colorama import Fore, init

# Conexion a la base de datos
conn = sqlite3.connect("database/data.sqlite")
cursor = conn.cursor()

init(autoreset=True)  # Colorama init


def get_user_data(entry):
    """ Consigue la contraseña del usuario especificado """

    cursor.execute(f"SELECT password FROM users WHERE user = '{entry}'")
    user = cursor.fetchone()[0]
    return user


def get_user_passwords():
    """ Consigue los nombres de contraseñas disponibles """

    cursor.execute("SELECT Nombre FROM data")
    return cursor.fetchall()


def insert_data(nombre, email, contraseña, link):
    """ Agrega registros a la base de datos """

    cursor.execute(
        f"INSERT INTO data VALUES ('{nombre}','{email}','{contraseña}','{link}')"
    )
    conn.commit()


def get_password_data(nombre):
    """ Consigue los datos de la contraseña seleccionada """

    cursor.execute(f"SELECT * FROM data WHERE Nombre = '{nombre}'")
    data = cursor.fetchall()[0]
    return data


def delete_data(nombre):
    """ Elimina la contraseña seleccionada """

    cursor.execute(f"DELETE FROM data WHERE Nombre = '{nombre}'")
    conn.commit()


def recovery(entry):
    """ Funcion para recuperar la contraseña con la clave mnemotécnica """

    cursor.execute(f"SELECT backup FROM users WHERE user = '{entry}'")
    user = cursor.fetchone()[0]
    return user


def edit_data(nombre, email, contraseña, link, entry):
    """ Cambia los datos de una contraseña por unos nuevos """

    cursor.execute(
        f"UPDATE data SET Nombre = '{nombre}', Email = '{email}', Contraseña = '{contraseña}', Link = '{link}' WHERE Nombre = '{entry}'"
    )
    conn.commit()
