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
Crear proyecto de Django
``` bash
django-admin startproject tasks .
```
Editamos settings.py
``` python
LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'
```
``` python
STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'
```
``` python
ALLOWED_HOSTS = ['localhost']
```
Enlazamos bbdd (no usar esa bbdd en produccion):
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Creamos en inicializamos la bbdd:
``` bash
python manage.py migrate

```
Inicialmos el servidor:
``` bash
python manage.py runserver

```
Entramos en el proyecto mediante http://localhost:8000

## Crear Applicación

``` bash
python manage.py startapp task
```
``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task',
]
```