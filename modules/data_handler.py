import sqlite3
from modules.crypto import encrypt, decrypt

conn = sqlite3.connect("database/data.sqlite")
cursor = conn.cursor()


def get_user_data(input):
    cursor.execute(f"SELECT password FROM users WHERE user = '{input}'")
    user = cursor.fetchone()[0]
    return user


def get_user_passwords():
    return cursor.execute("SELECT Nombre FROM data")


def insert_data(key):
    print("Vamos a agregar un registro nuevo!")
    nombre = input("Nombre: ")
    email = encrypt(input("E-mail: "), key)
    contraseña = encrypt(input("Contraseña: "), key)
    link = input("Link: ")
    cursor.execute(
        f"INSERT INTO data VALUES ('{nombre}','{email}','{contraseña}','{link}')"
    )
    conn.commit()


def get_password_data(nombre):
    cursor.execute(f"SELECT * FROM data WHERE Nombre = '{nombre}'")
    data = cursor.fetchall()[0]
    return data


def delete_data():
    nombre = input("Nombre: ")
    confirmacion = input(
        f"Seguro que quires eliminar {nombre} de tus registros? (y/o)\n> "
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
    cursor.execute(f"SELECT backup FROM users WHERE user = '{entry}'")
    user = cursor.fetchone()[0]
    return user


def edit_data(entry, key):
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
