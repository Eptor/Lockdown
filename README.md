# Lockdown

<p align="center">
<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/Eptor/Lockdown?color=yellow&label=Actividad&style=for-the-badge">
<a href="https://github.com/Eptor/Lockdown/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Eptor/Lockdown?color=red&label=estrellas&style=for-the-badge"></a>
<a href="https://github.com/Eptor/Lockdown/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Eptor/Lockdown?color=black&label=Licencia&style=for-the-badge"></a>
<a href="https://github.com/Eptor/Lockdown/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/Eptor/Lockdown?label=problemas&style=for-the-badge"></a>
</p>

<p align="center">
<img src=img/lockdown.png height=100>
</p>

Lockdown es un administrador de contraseñas sin conexión a internet, lo que facilita la confianza en el usuario pues nada está siendo enviado a nadie.

<img src=etc/menu.png height=300>

## Instalación

### Instalar requerimientos

```sh
pip install -r requirements.txt
```

### Instalar base de datos

<img src=etc/menu_instalacion.png>

Debes de correr el archivo _install.py_ de la siguiente manera:

```sh
install.py
```

Se abrirá un menú dónde podrá elegir si:

1. restaurar una base de datos mediante su archivo .lockdown
2. hacer una instalación limpia

## Que tan seguro es?

Lockdown utiliza el metodo de encriptado Fernet, el cual es un metodo de encriptado simetrico, por lo que tus contraseñas están seguras.

<img src=etc/datos.png height=300>

Y asi está el texto en la base de datos

<img src=etc/not_fb.png height=300>

## Olvidaste tu contraseña?

No te preocupes, al instalar la base de datos, se te genera una clave mnemotécnica para utilizar en caso de un recovery necesario.
Para acceder a la funcion de recovery deberás seleccionar Opciones en la ventana del login y seguir las instrucciones.

## Tienes un backup que quieres restaurar?

Al igual que en la recuperación de la contraseña, seleccionaras "Opciones" en la ventana de login para seguir las instrucciones.

## Actualizaciones

### v1.0 (31/12/2020)

- Primer version

### V1.5 (3/01/2021)

- Instalación mediante GUI

### V1.5.5 (4/01/2021)

- Corrección de errores
- Copiar enlace se cambió a abrir enlace
  (Abrir enlace abre el enlace guardado y copia la contraseña)

### V2.0 (5/01/2021)

- Generador de respaldos funcional
- Errores con la instalación corregidos

### V3.0 (6/01/2021)

- Codificador y decodificador de codigo morse

### Pequeña actualización 1

- Simbología en morse añadida
- Comentarios en el código

### V3.5 (8/01/2021)

- Integración con [Hides](https://github.com/Eptor/Hides)
  > Con Hides puedes ocultar tus archivos dentro de una imagen, haciendolos invisibles.

## Ejecutable para Windows

### Descargar ejecutable

Puedes descargar el ejecutable desde la seccion "Releases", aunque no siempre está a la par con la versión más actual.

### Generar ejecutable

Es posible crear un ejecutable tanto del instalador como del programa principal, para esto usaras Pyinstaler.
Deberás utilizar los archivos .spec que vienen en la carpeta Pyinstaller_specs

Mueve los archivos **main.pyw** e **install.pyw** a la carpeta Pyinstaller_specs y usalos de la siguiente manera:

```sh
pyinstaller Lockdown.spec
```

y

```sh
pyinstaller Lockdown_instalador.spec
```

Despues mueve los dos ejecutables a un folder junto a los archivos **words.txt** y **styles.css** y
podrás ejecutarlos sin problema.

## Donaciones

Cualquier cantidad es infinitamente agradecida ❤

- Paypal: [Hector Espinoza](http://www.paypal.me/espinoza7854)

- Bitcoin: 3MaZtzzJSY2Pw6v3WMu5qvzyaFstPKUX2J

  <img src="etc/btc_qr.png" height=100>

- Monero: 47egPTVGs3Eiq7gPYEmw6zat8dqLL8phYK61Hud937tvRbusGfd2TmUZW8eag6jb38Q3bQyKUns13SKjwHhPV4fXMnNCxxF

## Contribuir

Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar tan increíble para aprender, inspirar y crear. Cualquier contribución que haga es **grandemete apreciada**.

Para contribuir, sigue las siguientes instrucciones:

1. Haz un **fork** del proyecto
2. Crea una rama (branch) con tus añadidos, por ejemplo (`git checkout -b característica_nueva`)
3. Haz un commit con tus cambios (`git commit -m 'Caracteristica X añadida'`)
4. Haz un push a la rama (`git push origin característica_nueva`)
5. Abre una Pull Request

## Creditos

- Imagen blurr / background: [ianbarnard.co.uk](http://www.ianbarnard.co.uk/wp-content/uploads/2013/09/free-blurred-web-backgrounds-09.jpg)
- Logo sacado de: [iconscout](https://iconscout.com/icon/lockdown-2318925), fue creado por [Nithinan Tatah](https://iconscout.com/contributors/nithinan-tatah)
- Icono copiar: [iconscout](https://iconscout.com/icon/copy-197)
- Icono refresh: [iconscout](https://iconscout.com/icon/refresh-reload-recycle-synchronize-retry)
- Icono convertir: [iconscout](https://iconscout.com/icons/arrow), fue creado por by [Chameleon Design](https://iconscout.com/contributors/chamedesign)
- Iconos flechas: [iconscout - Unicons Font](https://iconscout.com/icon-pack/arrows-57)
- Icono de Hides: [Favicon.io](https://favicon.io/)
- Iconos usados en Hides: [iconscout - Files Icon Pack](https://iconscout.com/icon/file-264)

## Licencia

Distribuido bajo la licencia [GPL v3](https://www.gnu.org/licenses/gpl-3.0). Mira `LICENSE` para más información.
