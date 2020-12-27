# Lockdown

> Keep your data safe and locked away


Lockdown es el sucesor espiritual de Padlock, el primer administrador de contraseñas que hice.

![](etc/menu.png)

## Instalación

Instalar requerimientos

```sh
pip install -r requirements.txt
```

Instalar base de datos

```sh
modules/install.py
```


## Que tan seguro es?

Lockdown utiliza el metodo de encriptado Fernet, el cual es un metodo de encriptado simetrico, por lo que tus contraseñas están seguras.


![](https://media.giphy.com/media/TUeaUjG3tOkffSkw6O/giphy.gif)

Y asi está el texto en la base de datos

![](etc/not_fb.png)

## Olvidaste tu contraseña?

No te preocupes, al instalar la base de datos, se te genera una clave mnemotécnica para utilizar en caso de un recovery necesario.
Para acceder a la funcion de recovery deberás:

- a) En usuario escribir "help"

- b) Dejar la contraseña en blanco

- c) Presionar Enter

- d) Introducir tu mnemotécnica

## Tienes un backup que quieres restaurar?

En el inicio de sesión has lo siguiente:

- a) En usuario escribir "backup"

- b) Dejar la contraseña en blanco

- c) Introduce la contraseña

## Actualizaciones

### v1.0 (08/11/2020)
 - Primer version

### V1.5 (9/11/2020)
 - Respaldo
 - Generador de contraseñas

### V2.0 (27/12/2020)
 - Errores corregidos
 - Backup se hace con la contraseña y no con la clave mnemotécnica
 - La clave mnemotécnica es de solo 3 palabras en lugar de 9
## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

- Copyright 2020 © Eptor.
