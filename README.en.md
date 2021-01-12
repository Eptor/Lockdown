# Lockdown

<p align="center">
<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/Eptor/Lockdown?color=yellow&label=Commits&style=for-the-badge">
<a href="https://github.com/Eptor/Lockdown/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Eptor/Lockdown?color=red&label=Stars&style=for-the-badge"></a>
<a href="https://github.com/Eptor/Lockdown/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Eptor/Lockdown?color=black&label=Licence&style=for-the-badge"></a>
<a href="https://github.com/Eptor/Lockdown/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/Eptor/Lockdown?label=Issues&style=for-the-badge"></a>
</p>

<p align="center">
<img src=img/lockdown.png height=100>
</p>

Lockdown is a password manager without an internet connection, which facilitates trust in the user since nothing is being sent to anyone.

This is the menu

<img src=etc/menu.png height=300>

## Installation

### Install requirements

```sh
pip install -r requirements.txt
```

### Install database

<img src=etc/menu_instalacion.png>

You must run the _install.py_ file as follows:

```sh
install.py
```

A menu will open where you can choose whether to:

1. restore a database using its .lockdown file
2. do a clean install

## How safe is it?

Lockdown uses the Fernet encryption method, which is a symmetric encryption method, so your passwords are safe.

<img src=etc/datos.png height=300>

Here's the text on the database

<img src=etc/not_fb.png height=300>

## Did you forget your password?

Don't worry, when you install the database, a mnemonic key is generated for you to use in case of a necessary recovery.
To access the recovery function you must select Options in the login window and follow the instructions.

## Do you have a backup that you want to restore?

As in the password recovery, you will select "Options" in the login window to follow the instructions.

## Updates

### v1.0 (31/12/2020)

- First version

### V1.5 (3/01/2021)

- GUI installation

### V1.5.5 (4/01/2021)

- Error correction
- Copy link changed to open link
  (Open link opens the saved link and copy the password)

### V2.0 (5/01/2021)

- Functional backup generator
- Errors with the installation fixed

### V3.0 (6/01/2021)

- Morse code encoder and decoder

### Small update 1 (7/01/2021)

- Morse symbology added
- Comments in the code

### Integration with Hides # 1 (01/08/2021)

- A [new branch] (https://github.com/Eptor/Lockdown/tree/Hides) was created to test the integration with [Hides] (https://github.com/Eptor/Hides), <s>A merge with the main branch (GUI) is expected within the next week.</s> It was decided to keep Hides in a separate branch from the main one, at least for now.

## Executable for Windows

### Download executable

You can download the executable from the "Releases" section, although it is not always on par with the most current version.

### Generate executable

It is possible to create an executable for both the installer and the main program, for this you will use Pyinstaler.
You must use the .spec files that come in the Pyinstaller_specs folder

Move **Lockdown.spec** files and **Lockdown_installer.spec** to the root folder and use them as follows:

```sh
pyinstaller Lockdown.spec
```

Move the .exe file to another directory and run

```sh
pyinstaller Lockdown_instalador.spec
```

And in the same way, move the .exe to the folder where you will install Lockdown.

Then move the files **words.txt** and **styles.css** to the destination folder and you can run both .exe without problem.

Note: After installation, you can remove the installer and the words.txt file

## Donations

Any amount is infinitely appreciated ❤

- Paypal: [Hector Espinoza](http://www.paypal.me/espinoza7854)

- Bitcoin: 3MaZtzzJSY2Pw6v3WMu5qvzyaFstPKUX2J

  <img src="etc/btc_qr.png" height=100>

- Monero: 47egPTVGs3Eiq7gPYEmw6zat8dqLL8phYK61Hud937tvRbusGfd2TmUZW8eag6jb38Q3bQyKUns13SKjwHhPV4fXMnNCxxF

## contribute

### At the moment, contributing is only available to Spanish speakers, but it is planned to open the opportunity to everyone in the coming months.

<s>Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar tan increíble para aprender, inspirar y crear. Cualquier contribución que haga es **grandemete apreciada**.

Para contribuir, sigue las siguientes instrucciones:

1. Haz un **fork** del proyecto
2. Crea una rama (branch) con tus añadidos, por ejemplo (`git checkout -b característica_nueva`)
3. Haz un commit con tus cambios (`git commit -m 'Caracteristica X añadida'`)
4. Haz un push a la rama (`git push origin característica_nueva`)
5. Abre una Pull Request

</s>

## Credits

- Blurr image: [ianbarnard.co.uk](http://www.ianbarnard.co.uk/wp-content/uploads/2013/09/free-blurred-web-backgrounds-09.jpg)
- Logo: [iconscout](https://iconscout.com/icon/lockdown-2318925) by [Nithinan Tatah](https://iconscout.com/contributors/nithinan-tatah)
- Copy icon: [iconscout](https://iconscout.com/icon/copy-197)
- Refresh icon: [iconscout](https://iconscout.com/icon/refresh-reload-recycle-synchronize-retry)
- Translate icon: [iconscout](https://iconscout.com/icons/arrow) by [Chameleon Design](https://iconscout.com/contributors/chamedesign)
- Arrows: [iconscout - Unicons Font](https://iconscout.com/icon-pack/arrows-57)
- Installer icon: [iconscout - Vincent Le Moign](https://iconscout.com/icons/download)

## Licene

Distributed under the [GPL v3](https://www.gnu.org/licenses/gpl-3.0) license. See `LICENSE` for more information.
