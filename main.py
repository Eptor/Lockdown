#! D:\Programacion\Lockdown\env\Scripts\python
#!!! Este ^^ es mi ambiente virtual, eres libre de eliminar estas lineas.

# Modulos locales
from modules.crypto import encrypt, decrypt, decrypt_bkp, generador
from modules.install import install

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
|_______| \______/   \______||__|\__\ |_______/ \______/      \__/  \__/     |__| \__| v1.5
    """
    )
    print(from_db_cursor(get_user_passwords()))  # Generador de la tabla
    print("\n1) - Ver registro")
    print("2) - Añadir registro")
    print("3) - Eliminar registro")
    print("4) - Modificar registro")
    print("5) - Generador")

    print("\nBKP) - Crear respaldo")
    print("\nCTRL + C) - Salir\n")


def main():
    from modules.data_handler import (
        get_user_data,
        get_user_passwords,
        insert_data,
        get_password_data,
        delete_data,
        recovery,
        edit_data,
    )

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

            elif (
                user == "help" and key == "backup"
            ):  # Usar nueva base de datos

                print(Fore.YELLOW + "Espera mientras leemos el archivo")

                with open(
                    "database/data_backup.lockdown", "rb"
                ) as data_read:  # Leer bytes del archivo para desencriptado
                    data = decrypt_bkp(
                        data_read.read(),
                        input(
                            "Clave mnemotécnica con la que se creó el backup\n> "
                        ),
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
                password = generador()
                print("\nTu contraseña es:", Fore.MAGENTA + password)
                sleep(1)
                pyperclip.copy(password)
                print(Fore.CYAN + "\nLa copiamos a tu portapapeles !")
                sleep(2)

            elif om == "BKP":  # Respaldo
                os.system("cls")
                print(Fore.YELLOW + "Espera a que realicemos el backup")

                with open(
                    "database/data.sqlite", "rb"
                ) as data_read:  # Leer los bytes del archivo para encriptarlos
                    data = encrypt(
                        data_read.read(),
                        input("Clave mnemotécnica\n> "),
                    )

                with open(
                    "database/data_backup.lockdown", "wb"
                ) as data_write:  # Escribe los bytes encriptados en un nuevo archivo
                    data_write.write(data.encode())

                print("Completado.")
                print(
                    Fore.RED
                    + "\nPara utilizar este backup, la cuenta en la que lo utilices debe tener la misma contraseña que tienes ahora,"
                )
                sleep(5)

            else:
                pass

    except KeyboardInterrupt:
        os.system("cls")
        print(Fore.CYAN + "Gracias por usar Lockdown!")
        sleep(1)
        print("\nSaliendo.")
        sleep(1)


if __name__ == "__main__":
    if os.path.isfile("database/data.sqlite"):
        main()
    else:
        install()
