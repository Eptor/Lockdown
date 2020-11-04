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

    return cursor.execute("SELECT Nombre FROM data")


def insert_data(key):

    """ Agrega registros a la base de datos """

    print(Fore.YELLOW + "Vamos a agregar un registro nuevo!\n")
    nombre = input("Nombre: ")
    email = encrypt(input("E-mail: "), key)
    contraseña = encrypt(input("Contraseña: "), key)
    link = input("Link: ")
    cursor.execute(
        f"INSERT INTO data VALUES ('{nombre}','{email}','{contraseña}','{link}')"
    )
    conn.commit()


def get_password_data(nombre):

    """ Consigue los datos de la contraseña seleccionada """

    cursor.execute(f"SELECT * FROM data WHERE Nombre = '{nombre}'")
    data = cursor.fetchall()[0]
    return data


def delete_data():

    """ Elimina la contraseña seleccionada """

    nombre = input("Nombre: ")
    confirmacion = input(
        f"Seguro que quires eliminar {nombre} de tus registros? (y/n)\n> "
    )
    try:
        if confirmacion.lower() == "y":
            cursor.execute(f"DELETE FROM data WHERE Nombre = '{nombre}'")
    except Exception as e:
        print(e)
        return False
    else:
        conn.commit()
        return True


def recovery(entry):

    """ Funcion para recuperar la contraseña con la clave mnemotécnica """

    cursor.execute(f"SELECT backup FROM users WHERE user = '{entry}'")
    user = cursor.fetchone()[0]
    return user


def edit_data(entry, key):

    """ Cambia los datos de una contraseña por unos nuevos """

    try:
        nombre = input("Nombre: ")
        email = encrypt(input("E-mail: "), key)
        contraseña = encrypt(input("Contraseña: "), key)
        link = input("Link: ")
        cursor.execute(
            f"UPDATE data SET Nombre = '{nombre}', Email = '{email}', Contraseña = '{contraseña}', Link = '{link}' WHERE Nombre = '{entry}'"
        )
    except Exception:
        return False
    else:
        conn.commit()
        return True
