# Modulos locales
from modules.crypto import encrypt, decrypt
from modules.data_handler import (
    get_user_data,
    get_user_passwords,
    insert_data,
    get_password_data,
    delete_data,
    recovery,
    edit_data,
)

# Modulos vanila
import os
from time import sleep
from getpass import getpass

# Modulos externos (pip install)
from colorama import init, Fore
from prettytable import PrettyTable, from_db_cursor
import pyperclip

init(autoreset=True)  # Colorama init


def menu():
    os.system("cls")
    print(
        Fore.CYAN
        + """
 __        ______     ______  __  ___  _______   ______   ____    __    ____ .__   __.
|  |      /  __  \   /      ||  |/  / |       \ /  __  \  \   \  /  \  /   / |  \ |  |
|  |     |  |  |  | |  ,----'|  '  /  |  .--.  |  |  |  |  \   \/    \/   /  |   \|  |
|  |     |  |  |  | |  |     |    <   |  |  |  |  |  |  |   \            /   |  . `  |
|  `----.|  `--'  | |  `----.|  .  \  |  '--'  |  `--'  |    \    /\    /    |  |\   |
|_______| \______/   \______||__|\__\ |_______/ \______/      \__/  \__/     |__| \__|
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
            print(Fore.GREEN + "\nLogin exitoso")
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
        if om == "1":
            table = PrettyTable()  # Creacion de la tabla
            os.system("cls")
            try:
                data = get_password_data(input("Nombre: "))  # Obtencion de datos
            except IndexError:
                print(Fore.RED + "\nNo existen registros con ese nombre !")
                sleep(2)
            else:
                table.field_names = ["Nombre", "Email", "Contraseña", "Link"]
                table.add_row(
                    [data[0], decrypt(data[1], key), decrypt(data[2], key), data[3]]
                )
                print()
                try:
                    print(table)
                    input(
                        "\nPresiona ENTER para regresar al menu\nPresiona CTRL + C para copiar la contraseña"
                    )
                except KeyboardInterrupt:
                    pyperclip.copy(decrypt(data[2], key))
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

        else:
            pass

except KeyboardInterrupt:
    os.system("cls")
    print(Fore.CYAN + "Gracias por usar Lockdown!")
    sleep(1)
    print("\nSaliendo.")
    sleep(1)
    quit()
