import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from random import choice

# The base process was grabbed from the Docs:
# https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet


def encrypt(data, password):
    """ Proceso de encriptado """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"g\xe0\\F\x90\x15Dr\x1e-\xa8u\xd9Y\x0c\x82",
        iterations=100000,
        backend=default_backend(),
    )
    # Generación de llave mediante la contraseña dada
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    EncryptedToken = f.encrypt(data.encode())
    return EncryptedToken.decode()


def decrypt(data, password):
    """ Decrypts the data given by the user """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"g\xe0\\F\x90\x15Dr\x1e-\xa8u\xd9Y\x0c\x82",
        iterations=100000,
        backend=default_backend(),
    )
    # Generación de llave mediante la contraseña dada
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    DecryptedToken = f.decrypt(data.encode())
    return DecryptedToken.decode()


def mnemotecnica():

    """ Generación de clave para recuperación """

    palabra = ""

    with open("words.txt", "r") as texto:
        palabras = texto.read().split("\n")

    for i in range(0, 9):
        palabra += f"{choice(palabras)} "

    return palabra


if __name__ == "__main__":
    mnemotecnica()
