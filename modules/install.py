# Modulos vanila
import sqlite3
from time import sleep
from getpass import getpass
from os import system, path

# Modulos externos (pip install)
from crypto import mnemotecnica, encrypt
from colorama import init, Fore
import pyperclip


init(autoreset=True)  # Colorama init

if path.isfile(
    "database/data.sqlite"
):  # Verificar si ya existe una instalación
    print("Ya existe una instalación.")
    quit()

else:
    system("cls")
    print(Fore.CYAN + "Bienvenido a la instalación de Lockdown!")
    print("\nVamos a comenzar\n")
    sleep(1)

    # Conexion de la base de datos
    conn = sqlite3.connect("database/data.sqlite")
    cursor = conn.cursor()

    # Creacion de la tabla usuarios
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

    # Creacion de la tabla data
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

    # Creacion del usuario
    print("Introduzca su nombre de usuario")
    usuario = input("> ")
    print(Fore.GREEN + f"\nBienvenido {Fore.RESET+usuario}!\n")
    sleep(1)

    while True:  # Loop para verificar que la contraseña esté bien escrita
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

    # Creacion de la clave mnemotecnica
    print("Ahora vamos a crear tu clave mnemotécnica.")
    sleep(3)
    print(
        f"\nEsta servirá para recuperar tu cuenta en caso de que olvides tu contraseña, por lo que es de suma importancia que {Fore.RED+'NO LA PIERDAS'}."
    )
    sleep(4)

    print("\nTu clave es:\n")
    key = (
        mnemotecnica()
    )  # Genera la clave mnemotecnica (ver funcion en archivo crypto.py)
    print(Fore.YELLOW + key)
    pyperclip.copy(key)  # Se copia la clave al portapapeles

    # Anucnio de importancia
    print("\nPara tu comodidad, la hemos copiado a tu portapapeles.")
    input("\nCuando estés listo para continuar, presiona {ENTER}")
    print("\nAhora te añadiremos a la base de datos, aguarda un momento.")

    # Creación del usuario en la base de datos
    key = input("Introduce tu clave mnemotécnica:\n> ")
    cursor.execute(
        f"INSERT INTO users VALUES ('{usuario}', '{encrypt(passwd, passwd)}', '{encrypt(passwd, key)}')"
    )
    sleep(2)
    conn.commit()

    print(Fore.CYAN + "\nInstalación completada!")
