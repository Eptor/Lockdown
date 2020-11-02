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
