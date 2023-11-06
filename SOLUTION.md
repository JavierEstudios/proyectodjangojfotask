# PASOS

## Pasos iniciales

Lo primero es crear un entorno virtual:
``` bash
virtualenv tastsvenv
```
Acceder al entorno:
``` bash
source tastsvenv/bin/activate
```
Salir del entorno:
``` bash
deactivate
```
Actualizamos pip (dentro del entorno virtual):
``` bash
python -m pip install --upgrade pip
```
Creamos requirements.txt con las dependencias a instalar (Django en este caso):
``` bash
Django~=3.2.23
```
Instalamos dichas dependencias:
``` bash
pip install -r requirements.txt
```
