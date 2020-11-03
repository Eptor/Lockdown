from modules.crypto import encrypt, decrypt
from modules.data_handler import *
import os
from getpass import getpass
from prettytable import PrettyTable, from_db_cursor
from time import sleep
from colorama import init, Fore

init(autoreset=True)


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


while True:
    user = input("Usuario: ")
    key = getpass("Contraseña: ")

    if user == "help" and key == "":
        user = input("Introduce tu usuario: ")
        mn = input("> Introduce tu clave mnemotécnica:\n> ")
        print(f"Tu contraseña es: {decrypt(recovery(user), mn)}")

    elif key == decrypt(get_user_data(user), key):
        break

    else:
        continue

while True:
    menu()
    om = input("> ")
    if om == "1":
        table = PrettyTable()
        os.system("cls")
        data = get_password_data(input("Nombre: "))
        table.field_names = ["Nombre", "Email", "Contraseña", "Link"]
        table.add_row([data[0], decrypt(data[1], key), decrypt(data[2], key), data[3]])
        print(table)
        input()
        del table
    elif om == "2":
        os.system("cls")
        insert_data(key)
    elif om == "3":
        os.system("cls")
        if delete_data():
            print(Fore.GREEN + "Eliminado con exito.")
            sleep(2)
        else:
            print(Fore.RED + "No ha sido eliminado.")
            sleep(2)

    elif om == "4":
        os.system("cls")
        cambiar = input("Editar: ")
        if edit_data(cambiar, key):
            print(Fore.GREEN + "Editado con exito!")
            sleep(2)
        else:
            print(Fore.RED + "No fue editado.")
            sleep(2)
    else:
        pass
