# Modulos locales
from modules.crypto import encrypt, decrypt
from modules.data_handler import *

# Modulos vanila
import os
from time import sleep
from getpass import getpass

# Modulos externos (pip install)
from colorama import init, Fore
from prettytable import PrettyTable, from_db_cursor

init(autoreset=True)  # Colorama init


def menu():
    os.system("cls")
    print(
        """
  _                _       _                     
 | |              | |     | |                    
 | |     ___   ___| | ____| | _____      ___ __  
 | |    / _ \ / __| |/ / _` |/ _ \ \ /\ / / '_ \ 
 | |___| (_) | (__|   < (_| | (_) \ V  V /| | | |
 |______\___/ \___|_|\_\__,_|\___/ \_/\_/ |_| |_| 
    """
    )
    print(from_db_cursor(get_user_passwords()))
    print("\n1) - Ver registro")
    print("2) - Añadir registro")
    print("3) - Eliminar registro")
    print("4) - Modificar registro")
    print("\nCTRL + C) - Salir\n")


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
            print(Fore.YELLOW + f"Tu contraseña es: {decrypt(recovery(user), mn)}")
            input("Presiona enter para continuar")

        elif key == decrypt(get_user_data(user), key):  # Login exitoso
            break

        else:
            continue
    except Exception:
        print(Fore.RED + "Datos erroneos.")
        sleep(1)


# Main loop
try:
    while True:
        menu()
        om = input("> ")
        if om == "1":
            table = PrettyTable()  # Creacion de la tabla
            os.system("cls")
            data = get_password_data(input("Nombre: "))  # Obtencion de datos
            table.field_names = ["Nombre", "Email", "Contraseña", "Link"]
            table.add_row(
                [data[0], decrypt(data[1], key), decrypt(data[2], key), data[3]]
            )
            print(table)
            input("\nPresiona enter para regresar al menu")
            del table

        elif om == "2":
            os.system("cls")
            insert_data(key)  # Añadir registro

        elif om == "3":
            os.system("cls")
            if delete_data():  # Elimianr registro
                print(Fore.GREEN + "Eliminado con exito.")
                sleep(2)

            else:
                print(Fore.RED + "No ha sido eliminado.")
                sleep(2)

        elif om == "4":
            os.system("cls")
            cambiar = input("Editar: ")  # Cambiar datos de registro

            if edit_data(cambiar, key):
                print(Fore.GREEN + "Editado con exito!")
                sleep(2)

            else:
                print(Fore.RED + "No fue editado.")
                sleep(2)
        else:
            pass
except KeyboardInterrupt:
    os.system("cls")
    print("Gracias por usar Lockdown!")
    sleep(1)
    print("Saliendo.")
    sleep(1)
    quit()
