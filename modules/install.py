""" ARCHIVO PENDIENTE DE LIPIEZA Y COMENTARIOS """


from crypto import mnemotecnica, encrypt

import sqlite3
from colorama import init, Fore
from time import sleep
from os import system, path
from getpass import getpass
import pyperclip

init(autoreset=True)  # Colorama init

if path.isfile("database/data.sqlite"):
    print("Ya existe una instalación.")
    quit()
else:
    pass
    system("cls")
    print(Fore.CYAN + "Bienvenido a la instalación de Lockdown!")
    print("\nVamos a comenzar\n")
    sleep(1)

    conn = sqlite3.connect("database/data.sqlite")
    cursor = conn.cursor()

    print("[+] Creando la tabla de usuarios.\n")
    cursor.execute(
        """
        CREATE TABLE "users" (
	    "user"	TEXT NOT NULL UNIQUE,
	    "password"	TEXT NOT NULL,
        "backup" TEXT
    )
    """
    )
    sleep(1)
    print(Fore.GREEN + "Listo!\n")
    sleep(1)
    print("[+] Creando la tabla de almacenamiento\n")
    cursor.execute(
        """
    CREATE TABLE "data" (
        "Nombre" TEXT NOT NULL,
        "Email" TEXT,
        "Contraseña" TEXT NOT NULL,
        "Link" TEXT
    )
    """
    )
    sleep(1)
    print(Fore.GREEN + "Listo!\n")
    sleep(2)

    print("Introduzca su nombre de usuario")
    usuario = input("> ")
    print(Fore.GREEN + f"\nBienvenido {Fore.RESET+usuario}!\n")
    sleep(1)
    while True:
        print("Ahora introduce tu contraseña")
        passwd = getpass("> ")
        print("Confirmala")
        passw2 = getpass("> ")
        if passwd != passw2:
            print("Las contraseñas no coinciden")
            system("cls")
            continue
        else:
            break
    print("Ahora vamos a crear tu clave mnemotécnica.")
    sleep(3)
    print(
        f"\nEsta servirá para recuperar tu cuenta en caso de que olvides tu contraseña, por lo que es de suma importancia que {Fore.RED+'NO LA PIERDAS'}."
    )
    sleep(4)
    print("\nTu clave es:\n")
    key = mnemotecnica()
    print(Fore.YELLOW + key)
    pyperclip.copy(key)
    print("\nPara tu comodidad, la hemos copiado a tu portapapeles.")
    input("\nCuando estés listo para continuar, presiona {ENTER}")
    print("\nAhora te añadiremos a la base de datos, aguarda un momento.")
    key = input("Introduce tu clave mnemotécnica:\n> ")
    cursor.execute(
        f"INSERT INTO users VALUES ('{usuario}', '{encrypt(passwd, passwd)}', '{encrypt(passwd, key)}')"
    )
    sleep(2)
    conn.commit()
    print(Fore.CYAN + "\nInstalación completada!")
