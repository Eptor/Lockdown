from modules.crypto import encrypt, decrypt
from modules.data_handler import *
import os
from getpass import getpass
from prettytable import PrettyTable, from_db_cursor

table = PrettyTable()


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
    print("\n1) - Añadir registro")


while True:
    user = input("Usuario: ")
    key = getpass("Contraseña: ")
    if key == decrypt(get_user_data(user), key):
        break
    else:
        continue

while True:
    menu()
    om = int(input("> "))
    if om == 1:
        os.system("cls")
        insert_data(key)
